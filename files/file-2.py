f = open("sample.txt", "r")
x = f.read()
print(x)
f.close()


print("-----------------------------")
f = open("sample.txt", "r")
print(f.readlines())
f.close()

print("-----------------------------")
f = open("sample.txt", 'rt')
for line in f:
    print(line.strip("\n"))
f.close()

print("-------------------------------")
f = open("sample.txt", "r")
line = f.readline()
while line:
    print(line.strip("\n"))
    line = f.readline()
f.close()

print("---------------------------------")
with open("sample.txt", "rt", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

print(f.closed)

print("-------------------------")
f = open("sample.txt", "rt")
f.seek(3)
print(f.read())
