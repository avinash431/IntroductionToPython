name = "foobar"

for i in name:
    print(i)

s_ids = [101, 102, 103, 104]

for s_id in s_ids:
    print(s_id)

for i in range(len(name)):
    print(i, name[i])

for index, element in enumerate(name, start=1):
    print(index, element)

ascii_name_list = []
for i in name:
    ascii_name_list.append(ord(i))

ascii_name_list = [ord(i) for i in name]
print(ascii_name_list)
#
numbers = range(1, 11)
square_numbers = (num*num for num in numbers if num % 2 == 0)
# print(square_numbers)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sum_numbers = 0
row_counts = []
for row in matrix:
    for col in row:
        sum_numbers += col
    row_count = sum(row)
    row_counts.append(row_count)
print(sum_numbers)
print(row_counts)

col_sums = []
for all_col in zip(*matrix):
    col_sums.append(sum(all_col))
print(col_sums)

names = ["python", "java", ".net", "c++"]
for i in names:
    for j in i:
        print(j)

for s_id, name in zip(s_ids, names):
    print(s_id, name)
