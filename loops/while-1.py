"""
Sample while loop program to print numbers from 1 to 10
"""

index = 1
while index < 11:
    print(index)
    index += 1


index = 10
while index > 0:
    print(index)
    index -= 1

"""
A sample program for break use-case
"""
index = 1
i = 1
while True:
    if index % 2 == 0 and index % 5 == 0:
        if i == 5:
            break
        i += 1
        print(index, end=" ")
    index += 1
print(index)


# print from 10 to 1 in reverse
# pyramid triangle
# print 2 to 10 tables in the format 2 * 1 = 2
# print stars pattern
# sum of all the numbers' user has entered only if user hasn't entered 0 otherwise clear the entire list
# sort all the numbers in ascending order



