import pickle

f = open("collection types.txt", "wb")
pickle.dump(["java", ".net", "c++", "c"], file=f)
f.close()

f = open("collection types.txt", "rb")
x = pickle.load(f)
print(x, type(x))
f.close()
