f = open("sample.txt", "w")
f.write("10")
f.write("\n")
f.write("12")
f.write("\n")
f.write("13")
f.close()

names2 = ["javascript", "perl", "c", "r"]
with open("names.txt", "w") as f:
    for name in names2:
        # f.write(f"{name}\n")
        print(name, file=f)

print("------------------------------")
names = ["python", "java", "c++", "ruby", ".net"]
with open("names.txt", "r+") as f:
    print(f.read())
    for name in names:
        print(name, file=f)

print("--------------------")
f = open("types.txt", "w")
print(names, file=f)
f.close()




