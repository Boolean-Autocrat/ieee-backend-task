# program to find greatest common divisor of 5 numbers


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def gcd_of_five(a, b, c, d, e):
    return gcd(gcd(gcd(gcd(a, b), c), d), e)


# test cases
print(gcd_of_five(10, 20, 30, 40, 50))  # 10
print(gcd_of_five(10, 20, 30, 40, 60))  # 10


# user input
a, b, c, d, e = map(int, input("Enter 5 numbers: ").split())
print(gcd_of_five(a, b, c, d, e))
