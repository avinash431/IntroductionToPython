import threading
import time


def square_number(num):
    print("This is square number function")
    time.sleep(60)
    print(num * num)


def cube_num(num):
    print("THis is cube number function")
    time.sleep(30)
    print(num * num * num)


def print_hello_world():
    print("hello world")


t1 = threading.Thread(target=square_number, args=(12,))
t2 = threading.Thread(target=cube_num, args=(12,))
t3 = threading.Thread(target=print_hello_world)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("this is main thread")
