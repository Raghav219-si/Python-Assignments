# **********************************
# Author - Harshit Prasad
# 19.12.2016
# Threading in Python. (important)
# **********************************
import threading

class app(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread.getName())

x = app('Sends the message.')
y = app('Receive the message.')
x.start()
y.start()
# Both x and y will be executed together at the same time.
# This makes the computer performance more powerful.