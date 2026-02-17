import fibo

# Call first function
print("Using fib():")
fibo.fib(1000)

# Call second function
print("\nUsing fib2():")
numbers = fibo.fib2(100)
print(numbers)

# Print module name
print("\nModule name is:")
print(fibo.__name__)
