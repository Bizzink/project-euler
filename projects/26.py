"""Problem 26

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part."""
import decimal


def div(num, den, precision=20):
    # set precision
    with decimal.localcontext() as prec:
        prec.prec = precision
        return decimal.Decimal(num) / decimal.Decimal(den)


def get_recurring_cycle(num):
    cycle_check_count = 3
    num = list(str(num)[2:])
    cycle = []

    for char in num:
        cycle.append(char)

        for i in range(1, cycle_check_count + 1):
            if num[len(cycle) * i: len(cycle) * (i + 1)] != cycle:
                break

        else:
            return len(cycle)

    return 0


longest_cycle = 0

print(div(1, 983, 5000))

for i in range(2, 1001):
    num = div(1, i, 5000)
    cycle = get_recurring_cycle(num)

    if cycle > longest_cycle:
        print(i, cycle)
        longest_cycle = cycle

print(longest_cycle)
