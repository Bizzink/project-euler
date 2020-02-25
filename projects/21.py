"""Problem 21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000."""


def divisor_sum(num):
    """get the sum of all divisors of a number"""
    total = 0

    for i in range(1, num // 2 + 1):
        if num % i == 0:
            total += i

    return total


def amicable(num):
    """if num is amicable, return amicable pair"""
    if divisor_sum(divisor_sum(num)) == num and divisor_sum(num) != num:
        return divisor_sum(num)

    return None


amicable_nums = []

for i in range(1, 10000):
    if i not in amicable_nums:
        a = amicable(i)

        if a is not None:
            amicable_nums.append(i)

            if a not in amicable_nums and a < 10000:
                amicable_nums.append(a)

print(sum(amicable_nums))
