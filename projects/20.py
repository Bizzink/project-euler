"""Problem 20

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!"""


def factorial(num):
    """return the factorial of a number"""
    total = 1

    for i in range(1, num + 1):
        total *= i

    return total


number = 100

number = factorial(number)
total = sum([int(char) for char in str(number)])

print(total)
