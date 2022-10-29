# Unlimited Arguments
def add(*args):
    # return sum(args)
    sum = 0
    for n in args:
        sum += n
    return sum

# print(add(2, 3, 54, 32, 1))

# Kwargs: Many Keyworded Arguments


def calculate(n, **kwargs):
    # print(kwargs) --> kwargs is a object where sum and multiply are key and 4 and 7 are its value.
    # print(kwargs["sum"])
    n += kwargs["sum"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, sum=4, multiply=7)
