# 1️⃣ f-string example
year = 2016
event = "Referendum"
print(f"Results of the {year} {event}")

# 2️⃣ format() example
yes_votes = 42572654
total_votes = 85705149
percentage = yes_votes / total_votes

print("{:-9} YES votes {:2.2%}".format(yes_votes, percentage))

# 3️⃣ str() vs repr()
s = "Hello, world."
print("str():", str(s))
print("repr():", repr(s))

# 4️⃣ repr() with newline
hello = "hello, world\n"
print("repr with newline:", repr(hello))

# 5️⃣ repr() with object
x = 32.5
y = 40000
print("repr tuple:", repr((x, y, ("spam", "eggs"))))

# 6️⃣ string.Template example
from string import Template

t = Template("Hello $name")
print(t.substitute(name="Yash"))
