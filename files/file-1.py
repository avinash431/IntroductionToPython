# f = open("sample.txt", "w")
# f.write("10")
# f.write("\n")
# f.write("12")
# f.write("\n")
# f.write("13")
# f.close()

# names2 = ["javascript", "perl", "c", "r"]
# with open("names.txt", "w") as f:
#     for name in names2:
#         # f.write(f"{name}\n")
#         print(name, file=f)

# f = open("names.txt", "r")
# print(f.read())
# f.close()

# with open("names.txt", "r") as f:
#     for line in f:
#         print(line.strip("\n"))


f = open("sample.txt", "a")
f.write("14")
f.close()

