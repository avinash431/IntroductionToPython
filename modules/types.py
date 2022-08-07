from typing import List, Tuple


def greeting(name: str) -> str:
    return "hello " + name


def cal_add(x: int, y: int) -> int:
    return x + y


def function_var_args(*args: Tuple) -> None:
    print(args)
