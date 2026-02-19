# class Dog:

#     kind = "canine"   # Class variable (shared)

#     def __init__(self, name):
#         self.name = name   # Instance variable (unique)


# d = Dog("Fido")
# e = Dog("Buddy")

# print(d.kind)   # Shared
# print(e.kind)   # Shared

# print(d.name)   # Unique
# print(e.name)   # Unique

class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []   # ✅ New list per object

    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dog("Fido")
e = Dog("Buddy")

d.add_trick("roll over")
e.add_trick("play dead")

print(d.tricks)
print(e.tricks)
