"""Problem 28

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?"""


size = 1001
diagonal_sum = 1

# on each layer, increase sum by corner numbers
for i in range(3, size + 1, 2):
    diagonal_sum += i ** 2
    diagonal_sum += (i ** 2) - (i - 1)
    diagonal_sum += (i ** 2) - (2 * (i - 1))
    diagonal_sum += (i ** 2) - (3 * (i - 1))

print(diagonal_sum)
