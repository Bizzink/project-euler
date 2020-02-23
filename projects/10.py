"""Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million."""
from math import ceil, sqrt


def check_prime(num):
    if num % 2 == 0:
        return False

    for i in range(3, ceil(sqrt(num)) + 1, 2):
        if num % i == 0:
            return False

    return True


num = 2000000
total = 2

for i in range(3, num, 2):
    if check_prime(i):
        total += i

print(total)
