import functools
print("The factorial is {}".format(functools.reduce(lambda x, y: x * y, range(1, int(input("enter the number: "))+1))))
