from concurrent.futures import ThreadPoolExecutor


def square(num):
    # print(f"Thread {num} square value is {num * num}")
    return num * num


with ThreadPoolExecutor() as t:
    results = t.map(square, range(1, 101))

for result in results:
    print(result)
    