"""Problem 27

Euler discovered the remarkable quadratic formula:

n ** 2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39
. However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41

is clearly divisible by 41.

The incredible formula n ** 2 − 79n + 1601
was discovered, which produces 80 primes for the consecutive values 0≤n≤79

. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

    n ** 2 + an + b

, where |a|<1000 and |b|≤1000

where |n|
is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4

Find the product of the coefficients, a
and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0."""
from math import ceil, sqrt


def check_prime(num):
    if num < 2:
        return False

    if num in [2, 3]:
        return True

    if num % 2 == 0:
        return False

    for i in range(3, ceil(sqrt(num)) + 1, 2):
        if num % i == 0:
            return False

    return True


def check_equation(a, b):
    """check how many consecutive primes the equation produces using variables a & b"""
    i = 0

    while check_prime((i ** 2) + (a * i) + b):
        i += 1

    return i


max_consec_primes = 0
product = 0

for a in range(-1000, 1001):
    for b in range(-1000, 1001):
        consec_primes = check_equation(a, b)

        if consec_primes > max_consec_primes:
            product = a * b
            max_consec_primes = consec_primes

print(product)
