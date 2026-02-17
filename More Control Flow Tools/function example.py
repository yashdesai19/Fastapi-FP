def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

# Function Calls (each on new line)

standard_arg(10)
standard_arg(arg=20)

pos_only_arg(30)

kwd_only_arg(arg=40)    

combined_example(1, 2, kwd_only=3)

# def total_sum(*numbers):
#     total = 0
#     for n in numbers:
#         total += n
#     return total

# print(total_sum(1, 2, 3))
# print(total_sum(5, 19, 15, 20))
