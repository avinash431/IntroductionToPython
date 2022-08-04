import multiprocessing
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
    time.sleep(30)


t1 = multiprocessing.Process(target=square_number, args=(12,))
t2 = multiprocessing.Process(target=cube_num, args=(12,))
t3 = multiprocessing.Process(target=print_hello_world)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("this is main thread")
