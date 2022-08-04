import threading
import time

x = 1
lock = threading.Lock()


def increment():
    global x, lock
    lock.acquire()
    while x < 11:
        print(f"increment x: {x}")
        x += 1
        time.sleep(10)
    lock.release()


def decrement():
    global x
    lock.acquire()
    while x >= 0:
        print(f"Decrement x: {x}")
        x -= 1
        time.sleep(10)
    lock.release()


t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=decrement)
t1.start()
t2.start()
