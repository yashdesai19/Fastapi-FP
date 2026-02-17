users = {"admin": "1234", "yash": "pass"}

username = input("Enter username: ")
password = input("Enter password: ")

if username in users:
    if users[username] == password:
        print("Login Successful!")
    else:
        print("Wrong Password!")
else:
    print("Username not found!")
