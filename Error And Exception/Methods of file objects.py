# # with open("example.txt", "r", encoding="utf-8") as f:
# #     data = f.read(2)
# #     print(data)


# # with open("example.txt", "r", encoding="utf-8") as f:
# #     print(f.readline())
# #     print(f.readline())

# # with open("example.txt", "r", encoding="utf-8") as f:
# #     for line in f:
# #         print(line, end="")

# # with open("write.txt", "w", encoding="utf-8") as f:
# #     count = f.write("This is a test\n")
# #     print("Characters written:", count)

# # with open("example.txt", "r", encoding="utf-8") as f:
# #     print(f.tell())
# #     f.read(5)
# #     print(f.tell())

# with open("example.txt","r",encoding="utf-8") as f:
#     print("Position before reading:",f.tell())
    
#     content = f.read(10)
#     print("Read content",content)
    
#     print("Postion after reading:",f.tell())

# ------------------------------
# FILE HANDLING COMPLETE DEMO
# ------------------------------

print("1️⃣ Writing to file (write mode)")
with open("demo.txt", "w", encoding="utf-8") as f:
    f.write("This is the first line.\n")
    f.write("This is the second line.\n")
    f.write("This is the third line.\n")

# ------------------------------

print("\n2️⃣ Reading full file (read)")
with open("demo.txt", "r", encoding="utf-8") as f:
    print(f.read())

# # ------------------------------

print("\n3️⃣ Reading partial content (read 10 chars)")
with open("demo.txt", "r", encoding="utf-8") as f:
    print(f.read(10))

# # ------------------------------

print("\n4️⃣ Reading line by line (readline)")
with open("demo.txt", "r", encoding="utf-8") as f:
    print(f.readline(), end="")
    print(f.readline(), end="")
    print(f.readline(), end="")
    print("After file end:", f.readline())  # empty string

# # ------------------------------

print("\n5️⃣ Reading using loop (best practice)")
with open("demo.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

# # ------------------------------

print("\n6️⃣ readlines() example")
with open("demo.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(lines)

# # ------------------------------

print("\n7️⃣ Writing non-string object")
value = ("Answer", 42)
with open("demo.txt", "a", encoding="utf-8") as f:
    f.write(str(value) + "\n")

# # ------------------------------

print("\n8️⃣ tell() example")
with open("demo.txt", "r", encoding="utf-8") as f:
    print("Initial position:", f.tell())
    f.read(5)
    print("Position after reading 5 chars:", f.tell())

# ------------------------------

print("\n9️⃣ seek() example (binary mode)")
with open("binary_demo.bin", "wb+") as f:
    f.write(b"0123456789abcdef")

    f.seek(5)
    print("Byte at position 5:", f.read(1))

    f.seek(-3, 2)
    print("3rd byte before end:", f.read(1))

# ------------------------------

print("\n🔟 truncate() example")
with open("truncate_demo.txt", "w", encoding="utf-8") as f:
    f.write("Hello Python World")

with open("truncate_demo.txt", "r+") as f:
    f.truncate(5)

with open("truncate_demo.txt", "r", encoding="utf-8") as f:
    print("After truncate:", f.read())

# ------------------------------

print("\n1️⃣1️⃣ isatty() example")
with open("demo.txt", "r", encoding="utf-8") as f:
    print("Is connected to terminal?", f.isatty())

print("\n✅ All file operations completed successfully!")
