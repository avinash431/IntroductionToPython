x = {"a": 1, "b": 2, "c": 3}
# for i in x:
#     print(i, x[i])
#
# for i in x.keys():
#     print(i, x[i])

# for i in x.values():
#     print(i)

for i, j in x.items():
    print(i, j)

numbers = range(1, 11)
# output_dict = {}
# for num in numbers:
#     output_dict[num] = num * num

output_dict = {num: num * num for num in numbers}
print(output_dict)


# sum of all columns in a matrix
# loop zip of different lengths
# foobar -> {'f': 1, 'o': 2, 'b':1, 'a':1, 'r': 1}
# convert numbers = [100,101,102] to their binary, hexadecimal format using list comphrension
# swap key, value pairs in a dictionary
# using list comphresion square even numbers cube odd numbers

