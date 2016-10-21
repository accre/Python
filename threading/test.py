#!/usr/bin/env python

import threading


def worker():
    """ thread worker function """
    print("Hello")
    print("World!")
    return

threads = []


for i in range(8):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()
