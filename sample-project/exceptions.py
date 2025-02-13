# try:
#     raise NameError('HiThere')
# except NameError:
#     print('An exception flew by!')
#     raise

# try:
#     open("database.sqlite")
# except OSError:
#     raise RuntimeError("unable to handle error")

# def divide(x, y):
#     try:
#         result = x / y
#     except ZeroDivisionError:
#         print("division by zero!")
#     else:
#         print("result is", result)
#     finally:
#         print("executing finally clause")

# divide(2, 1)
# divide(2, 0)
# divide("2", "1")

excs = []
for test in tests:
    try:
        test.run()
    except Exception as e:
        excs.append(e)

if excs:
   raise ExceptionGroup("Test Failures", excs)