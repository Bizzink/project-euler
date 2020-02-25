"""Problem 30

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 14 + 64 + 34 + 44
    8208 = 84 + 24 + 04 + 84
    9474 = 94 + 44 + 74 + 44

As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits."""


def sum_fifth_power(num):
    num = [int(char) for char in str(num)]

    total = 0
    for digit in num:
        total += digit ** 5

    return total


total_valid = 0

for i in range(2, 1000000):
    if sum_fifth_power(i) == i:
        print(i)
        total_valid += i

print(total_valid)