# class Myclass:
#     """A simple example of class"""
#     i = 12345
    
#     def f(self):
#         return 'hello world'

class Complex:
    def __init__(self,realpart,imagpart):
        self.r = realpart
        self.i = imagpart
        
x = Complex(3.0, -4.5)
print(x.r,x.i)   