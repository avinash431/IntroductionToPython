from string import punctuation
from string import Template
import string

x = "!This is a sentence with an exclamation mark!"
y = "?This is a sentence with an exclamation mark?"

print(x.strip(punctuation))
print(y.strip(punctuation))

s = Template('$name likes $likes')
name = "john"
likes = "tea"
print(f"{name} likes {likes}")
print(s.substitute(name=name, likes=likes))

