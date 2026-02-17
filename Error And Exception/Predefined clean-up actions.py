# for line in open("myfile.txt"):
#     print(line, end="")

with open("myfile.txt") as f:
    for line in f:
        print(line, end="")

try:
    f = open("myfile.txt")
    data = f.read()
finally:
    f.close()

    