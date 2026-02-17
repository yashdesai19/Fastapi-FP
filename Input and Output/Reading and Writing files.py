# # Writing to file
# with open("example.txt", "w", encoding="utf-8") as f:
#     f.write("Hello Yash\n")
#     f.write("Python File Handling")

# Reading file
with open("example.txt", "r", encoding="utf-8") as f:
    c = f.read()
    print(c)

# # Check closed
# print("File closed:", f.closed)
