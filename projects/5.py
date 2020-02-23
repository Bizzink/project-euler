"""Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""


num = 20
val = 0

while True:
    # increase val by num, as it has to be a multiple of the largest value, this will get the answer quickest
    val += num

    for j in range(2, num + 1):
        if val % j != 0:
            break

    else:
        print(val)
        break
