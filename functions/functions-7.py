def token_generator():
    i = 1
    while True:
        yield i
        i += 1


t = token_generator()
print(t)
for _ in range(3):
    print(next(t))


def token_range_generator():
    for i in range(1, 101):
        yield i


for i in token_range_generator():
    print(i)

map()
