from functools import reduce
n = int(input("Please Enter any Number"))

# THE ONE-LINER
factorial = reduce(lambda x, y: x * y, range(1, n+1))

# THE RESULT
print("The factorial of {} is".format(n),factorial)