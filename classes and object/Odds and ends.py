# # ----------------------------
# # 1️⃣ DATACLASS EXAMPLE
# # ----------------------------

# from dataclasses import dataclass

# @dataclass
# class Employee:
#     name: str
#     dept: str
#     salary: int

# print("=== Dataclass Example ===")
# john = Employee("John", "Computer Lab", 1000)

# print("Name:", john.name)
# print("Department:", john.dept)
# print("Salary:", john.salary)

# # print()


# # ----------------------------
# # 2️⃣ DUCK TYPING EXAMPLE
# # ----------------------------

# print("=== Duck Typing Example ===")

# # Function expecting a file-like object
# def read_first_line(file_obj):
#     return file_obj.readline()

# # Real file example
# with open("sample.txt", "w") as f:
#     f.write("Hello World\nSecond Line")

# with open("sample.txt", "r") as f:
#     print("From real file:", read_first_line(f))


# # Custom class that behaves like file
# class StringReader:
#     def __init__(self, data):
#         self.lines = data.split("\n")
#         self.index = 0

#     def readline(self):
#         if self.index < len(self.lines):
#             line = self.lines[self.index]
#             self.index += 1
#             return line
#         return ""

# reader = StringReader("Line1\nLine2\nLine3")
# print("From custom class:", read_first_line(reader))

# print()


# # ----------------------------
# # 3️⃣ METHOD OBJECT ATTRIBUTES
# # ----------------------------

print("=== Method Object Attributes Example ===")

class Person:
    def greet(self):
        print("Hello!")

p = Person()

# Get bound method
m = p.greet

# Call method
m()

# Inspect attributes
print("Method __self__:", m.__self__)
print("Method __func__:", m.__func__)
