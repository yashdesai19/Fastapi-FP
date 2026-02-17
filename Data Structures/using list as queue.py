from collections import deque

# create queue
queue = deque(["Eric", "John", "Michael"])
print("Initial queue:", queue)

# new people arrive
queue.append("Terry")
print("After Terry arrives:", queue)

queue.append("Graham")
print("After Graham arrives:", queue)

# first person leaves
removed = queue.popleft()
print("Removed (served):", removed)
print("Queue now:", queue)

# second person leaves
removed = queue.popleft()
print("Removed (served):", removed)
print("Queue now:", queue)

# final queue
print("Final queue:", queue)
