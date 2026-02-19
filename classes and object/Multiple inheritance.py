# # class Father:
# #     def house(self):
# #         print("Father's House")

# # class Mother:
# #     def car(self):
# #         print("Mother's Car")

# # class Child(Father, Mother):
# #     def __init__(self):
# #         print("child name")

# # c = Child()
# # c.house()
# # c.car()
# # class Father:
# #     def skills(self):
# #         print("Driving")

# # class Mother:
# #     def skills(self):
# #         print("Cooking")

# # class Child(Father, Mother):
# #     pass
# # c = Child()
# # c.skills()
# # c.skills()


# class A:
#     def show(self):
#         print("Class A")
        
# class B(A):
#     def show(self):
#         print("Class B")

# class C(A):
#     def show(self):
#         print("Class c")
# class D(B,C):
#     def show(self):
#         print("Class D")

# # d = D()
# # d.show()

# c = C()
# c.show()

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")
        super().show()

class C(A):
    def show(self):
        print("C")
        super().show()

class D(B, C):
    def show(self):
        print("D")
        super().show()
        
d = D()
d.show()

