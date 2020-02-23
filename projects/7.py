"""Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?"""
from math import ceil, sqrt


def check_prime(num):
    if num % 2 == 0:
        return False

    for i in range(3, ceil(sqrt(num)) + 1, 2):
        if num % i == 0:
            return False

    return True


prime_count = 1
max_count = 10001
num = 1

while prime_count < max_count:
    num += 2

    if check_prime(num):
        prime_count += 1

print(num)
