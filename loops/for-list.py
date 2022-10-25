x = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]

# y = []
# for i in x:
#     for j in i:
#         y.append(j)
#
# print(y)

y = [j for i in x for j in i]
print(y)
