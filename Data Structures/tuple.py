# create tuple
t = 1,2,3,4,5
print("Tuple t:", type(t), t)

# access first element
print("First element of t:", t[3])

# print whole tuple
print("Full tuple t:", t)

# nested tuple
u = t, (11, 12, 13, 14, 15)
print("Nested tuple u:", u)

# # try to modify tuple (will cause error)
try:
    t[0] = 88888
except TypeError as e:
    print("Error:", e)

print(t)
# tuple with mutable objects (lists)
v = ([1, 2, 3], [3, 2, 1])
print("Tuple with lists v:", v)

# # modify list inside tuple
v[0][0] = 99
print("After modifying inner list:", v)
