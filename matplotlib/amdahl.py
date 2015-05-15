import numpy as np
import matplotlib.pyplot as plt

def plot_speedup(percent_serial,axis_obj,symbolcode):
    n = np.arange(1,1000,2)
    T = np.zeros(len(n))
    T[0] = 1000 # serial run time
    for ind,nprocs in enumerate(n):
        T[ind] = T[0]*(percent_serial + (1.0/float(nprocs))*(1-percent_serial))
        
    axis_obj.plot(n,T[0]/T,symbolcode,label=str(100.0*percent_serial)+"% serial")
    axis_obj.set_xlabel("# processors",fontsize=16)
    axis_obj.set_ylabel("Speedup",fontsize=16) 

def main():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plot_speedup(0.05,ax,'ro--')
    #plot_speedup(0.10,ax,'ko--')
    #plot_speedup(0.20,ax,'bo--')
    #ax.legend(fontsize=16,loc = (0.5,0.6))
    ax.grid(color='k', linestyle='--', linewidth=1)
    fig.show()

if __name__ == '__main__':
    main()
