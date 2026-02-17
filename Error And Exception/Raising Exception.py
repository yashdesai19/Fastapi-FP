# try:
#     raise NameError('HiThere')
# except NameError:
#     print('An exception flew by!')
#     raise

# age = -5

# if age < 0:
#     raise ValueError("Age cannot be negative")


# try:
#     1 / 0
# except ZeroDivisionError:
#     int("abc")


# try:
#     int("abc")
# # except ValueError as e:
#     raise TypeError("Conversion failed") from e

# def func():
#     raise ConnectionError

# try:
#     func()
# except ConnectionError as exc:
#     raise RuntimeError('Failed to open database') from exc


# try:
#     open('database.sqlite')
# except OSError:
# #     raise RuntimeError from None

# def open_database():
#     try:
#         open("database.sqlite")
#     except OSError as exc:
#         raise RuntimeError("Database connection failed") from exc

# class AgeError(Exception):
#     pass

# try:
#     age = int(input("Enter age: "))
#     if age < 0:
#         raise AgeError("Age cannot be negative")
# except AgeError as e:
#     print("Custom Error:", e)


# class SalaryError(Exception):
#     def __init__(self, salary):
#         self.salary = salary
#         super().__init__(f"Invalid salary: {salary}")




class InsufficientBalanceError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError("Not enough balance")
    return balance - amount

try:
    withdraw(1000, 2000)
except InsufficientBalanceError as e:
    print("Transaction Failed:", e)
  