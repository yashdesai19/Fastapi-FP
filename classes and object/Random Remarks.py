class Warehouse:
   purpose = 'storage'
   region = 'west'

w1 = Warehouse()
print(w1.purpose, w1.region)

w2 = Warehouse()
w2.region = 'east'
print(w2.purpose, w2.region)

# # # class Test:
# # #     def __init__(self):
# # #         self.value = 10

# # # t = Test()
# # # t.value = 999   # client changes it

# # # print(t.value)




# # # class Test:
# # #     def __init__(self):
# # #         self.__value = 10

# # # t = Test()
# # # print(t._Test__value)   # still accessible



# # class Bag:
# #     def __init__(self):
# #         self.data = []
        
# #     def add(self,x):
# #         self.data.append(x)
        
# #     def addtwice(self,x):
# #         self.add(x)
# #         self.add(x)
    

# # b = Bag()
# # b.addtwice(5)
# # print(b.data)

# # class Demo:
# #     def greet(self):
# #         print("Hello")
    
# # d = Demo()
# # d.greet()

# class Calculator:
#     def double(self,x):
#         return x * 2
    
#     def quadruple(self, x):
#         return self.double(x) * 2

# c = Calculator()
# print(c.quadruple(5))
 