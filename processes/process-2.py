from concurrent.futures import ProcessPoolExecutor


def print_hello_world():
    print("hello world")


def print_name():
    print("name is john")


with ProcessPoolExecutor() as t:
    t.submit(print_name)
    t.submit(print_hello_world)

