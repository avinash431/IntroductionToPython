import itertools

for i in itertools.repeat("ABCD", 3):
    print(i)

data = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
output_data = []
sum_accumlator = 0
for i in data:
    sum_accumlator += i
    output_data.append(sum_accumlator)
print(output_data)

print(list(itertools.accumulate(data, lambda x1, x2: x1 + x2)))

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

print((list(itertools.product(list1, list2))))
