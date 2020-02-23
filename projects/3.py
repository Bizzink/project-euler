"""Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?"""
from math import sqrt, ceil


def check_prime(num):
    """check if a number is prime"""
    if num % 2 == 0:
        return False

    for i in range(3, ceil(sqrt(num)), 2):
        if num % i == 0:
            return False

    return True


num = 600851475143

# start with the largest factor and decrease (num / i)
for i in range(1, (num // 2) + 1):
    if num % i == 0 and check_prime(num / i):
        # first prime factor found will be largest
        print(int(num / i))
        break
