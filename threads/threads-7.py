import threading
import time

text = "before reading the file"


def read_file():
    global text
    while True:
        with open("read.txt", "r") as f:
            text = f.read()


def print_text():
    global text
    while True:
        print(text)
        time.sleep(5)


t1 = threading.Thread(target=read_file, daemon=True)
t2 = threading.Thread(target=print_text)
t1.start()
t2.start()
t1.join()
t2.join()
print("all threads started")
