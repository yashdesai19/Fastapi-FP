# def f():
#     excs = [OSError('error 1'), SystemError('error 2')]
#     raise ExceptionGroup('there were problems', excs)

# f()
# try:
#     f()
# except Exception as e:
#     print(type(e))

# try:
#     f()
# except* OSError:
#     print("There were OSErrors")
# except* SystemError:
#     print("There were SystemErrors")
def f():
    raise ExceptionGroup(
        "group1",
        [
            OSError(1),
            SystemError(2),
            ExceptionGroup(
                "group2",
                [
                    OSError(3),
                    RecursionError(4)
                ]
            )
        ]
    )
