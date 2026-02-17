num = int(input("Enter a number: "))
print("Square is:", num * num)
# rows =6
# for num of range (rows):
# for i in range (num):
#     print(num end=" ")
#     print("  ")

# rows=0
# b = 0
# for i in range(rows,u,-1):
# b1=1
# for j in range(1,i,+1):
#      print(b,end=" ")
#      print('\r')
     
rows = 5   # You can change this number

b = 0

for i in range(rows, 0, -1):
    b1 = 1
    for j in range(1, i + 1):
        print(b, end=" ")
    print()   # Move to next line
     
     
