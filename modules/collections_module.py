from collections import ChainMap

x = {"a": 1, "b": 2}
y = {"a": 3, "c": 4}


output = {"a": 3, "b": 2, "c": 4}
x.update(y)
print(x)
assert output == x

import os, argparse

defaults = {'color': 'red', 'user': 'guest'}

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = {k: v for k, v in vars(namespace).items() if v is not None}

combined = ChainMap(command_line_args, os.environ, defaults)
print(combined['color'])
print(combined['user'])

colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
print(set(colors))
list_colors = dict()
for color in set(colors):
    list_colors[color] = colors.count(color)
print(list_colors)

from collections import Counter
print(Counter(colors).most_common(2))

from collections import defaultdict

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
output_s = {"yellow": [1, 3], "blue": [2, 4, 1]}
empty_output_s = dict()
for color, index in s:
    if color not in empty_output_s:
        empty_output_s[color] = [index]
    else:
        empty_output_s[color].append(index)
print(empty_output_s)

default_dict_s = defaultdict(list)
for color, index in s:
    default_dict_s[color].append(index)

print(default_dict_s)

from collections import namedtuple

tuple1 = (1, "john", "john@gmail.com")
student = namedtuple("student", ["id", "name", "email_id"])
s1 = student._make(tuple1)
print(s1.name, s1.id, s1.email_id)
print(student(2, "satish", "satish@yahoo.com"))

from collections import deque
colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
# colors.append("brown")
# colors.insert(0, "white")
deque_colors = deque(colors)
deque_colors.append("brown")
deque_colors.appendleft("white")
print(deque_colors)

import queue
colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
colors_queue = queue.Queue()
# for _ in range(3):
#     x = input("Enter a number: ")
#     colors_queue.put(x)
#
# print(colors_queue.get())
# print(colors_queue.get())
# print(colors_queue.get())

# numbers_queue = queue.LifoQueue()
# for _ in range(3):
#     x = input("Enter a number: ")
#     numbers_queue.put(x)
#
# print(numbers_queue.get())
# print(numbers_queue.get())
# print(numbers_queue.get())

# priority_queue = queue.PriorityQueue()
# priority_queue.put(2, "2rd priority")
# priority_queue.put(3, "3nd priority")
# priority_queue.put(1, "1st priority")
#
# print(priority_queue.get())
# print(priority_queue.get())
# print(priority_queue.get())
#
import concurrent.futures
process_queue = queue.Queue()


def producer():
    for i in range(1, 11):
        process_queue.put(i)


def consumer():
    while not process_queue.empty():
        print(process_queue.get())


with concurrent.futures.ProcessPoolExecutor() as executor:
    executor.submit(producer())
    executor.submit(consumer())




