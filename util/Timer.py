"""
platform: win
env: any
name: Timer.py
simple timer
"""
import time


class Timer:
    def __init__(self):
        self._start = time.time()

    def reset(self):
        self._start = time.time()

    def cut(self, tag=None):
        t = time.time()
        if tag is None:
            print(t - self._start)
        else:
            print("{} for {} seconds".format(tag, t - self._start))
        self._start = t
        return t - self._start
