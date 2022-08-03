import threading
import time


def square_num(num):
    time.sleep(20)
    print(f"Thread: {num} compute value: {num * num}")


# Creating the threads
threads_list = []
for num in range(1, 100):
    threads_list.append(threading.Thread(target=square_num, args=(num,)))

# Start the threads
for thread in threads_list:
    thread.start()

for thread in threads_list:
    thread.join()

print("All threads are completed")
