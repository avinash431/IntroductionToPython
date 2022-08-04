import threading

x = 1


def increment():
    global x
    while x < 11:
        print(f"increment x: {x}")
        x += 1


def decrement():
    global x
    while x >= 0:
        print(f"Decrement x: {x}")
        x -= 1


t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=decrement)
t1.start()
t2.start()
