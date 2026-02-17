# create stack
stack = [3, 4, 5]
print("Initial stack:", stack)

# push elements
stack.append(6)
print("After append 6:", stack)

stack.append(7)
print("After append 7:", stack)

# pop element
removed = stack.pop()
print("Popped element:", removed)
print("Stack now:", stack)

# pop again
removed = stack.pop()
print("Popped element:", removed)
print("Stack now:", stack)

# pop again
removed = stack.pop()
print("Popped element:", removed)
print("Stack now:", stack)

# final stack
print("Final stack:", stack)
