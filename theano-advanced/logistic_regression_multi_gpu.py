""" Test script that uses two GPUs, one per sub-process,
via the Python multiprocessing module.  Each GPU fits a logistic regression model. """

from __future__ import print_function
# These imports will not trigger any theano GPU binding
from multiprocessing import Process, Manager
import numpy as np
import os

def f(shared_args,private_args): 
    """ Build and fit a logistic regression model.  Adapted from 
    http://deeplearning.net/software/theano/tutorial/examples.html#a-real-example-logistic-regression
    """

    # Import sandbox.cuda to bind the specified GPU to this subprocess
    # then import the remaining theano and model modules.
    import theano.sandbox.cuda
    theano.sandbox.cuda.use(private_args['gpu'])

    import theano
    import theano.tensor as T
    from theano.tensor.shared_randomstreams import RandomStreams

    rng = np.random    

    # Pull the size of the matrices from 
    shared_args_dict = shared_args[0]
    N = shared_args_dict['N']
    feats = shared_args_dict['n_features']
    D = (rng.randn(N, feats), rng.randint(size=N,low=0, high=2))
    training_steps = shared_args_dict['n_steps']

    # Declare Theano symbolic variables
    x = T.matrix("x")
    y = T.vector("y")
    w = theano.shared(rng.randn(feats), name="w")
    b = theano.shared(0., name="b")
    print("Initial model:")
    print(w.get_value(), b.get_value())

    # Construct Theano expression graph
    p_1 = 1 / (1 + T.exp(-T.dot(x, w) - b))   # Probability that target = 1
    prediction = p_1 > 0.5                    # The prediction thresholded
    xent = -y * T.log(p_1) - (1-y) * T.log(1-p_1) # Cross-entropy loss function
    cost = xent.mean() + 0.01 * (w ** 2).sum()# The cost to minimize
    gw,gb = T.grad(cost, [w, b])              # Compute the gradient of the cost

    # Compile. allow_input_downcast reassures the compiler that we are ok using
    # 64 bit floating point numbers on the cpu, 
    # but only 32 bit floats on the gpu
    train = theano.function(
              inputs=[x,y],
              outputs=[prediction, xent],
              updates=((w, w - 0.1 * gw), (b, b - 0.1 * gb)), 
              allow_input_downcast=True)
    predict = theano.function(inputs=[x], outputs=prediction, 
        allow_input_downcast=True)

    # Train
    for i in range(training_steps):
        pred, err = train(D[0], D[1])

    print("Final model:")
    print(w.get_value(), b.get_value())
    print("target values for D:", D[1])
    print("prediction on D:", predict(D[0]))



if __name__ == '__main__':

    # Construct a dict to hold arguments that can be shared by both processes
    # The Manager class is a convenient to implement this
    # See: http://docs.python.org/2/library/multiprocessing.html#managers
    #
    # Important: managers store information in mutable *proxy* data structures
    # but any mutation of those proxy vars must be explicitly written back to the manager.
    manager = Manager()

    args = manager.list()
    args.append({})
    shared_args = args[0]
    shared_args['N'] = 400
    shared_args['n_features'] = 784
    shared_args['n_steps'] = 10000
    args[0] = shared_args       

    # Construct the specific args for each of the two processes
    p_args = {}
    q_args = {}

    p_args['gpu'] = 'gpu0'
    q_args['gpu'] = 'gpu1'

    # Run both sub-processes
    p = Process(target=f, args=(args,p_args,))
    q = Process(target=f, args=(args,q_args,))
    p.start()
    q.start()
    p.join()
    q.join()
