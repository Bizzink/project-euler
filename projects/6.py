"""Problem 6

The sum of the squares of the first ten natural numbers is,
12+22+...+102=385
The square of the sum of the first ten natural numbers is,
(1+2+...+10)2=552=3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025−385=2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""


num = 100

# sum of squares:
sum_squares = 0
for i in range(1, num + 1):
    sum_squares += i ** 2

# square of sum:
square_sum = 0
for i in range(1, num + 1):
    square_sum += i

square_sum **= 2

print(square_sum - sum_squares)