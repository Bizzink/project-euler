"""Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers."""


def check_palindrome(num):
    num = str(num)
    rev = "".join(list(reversed(num)))

    return num == rev


largest = 0

for num1 in range(1, 1000):
    for num2 in range(num1, 1000):
        if check_palindrome(num1 * num2):
            if num1 * num2 > largest: largest = num1 * num2

print(largest)
