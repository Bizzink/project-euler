"""Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which a**2 + b**2 = c**2

For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""

a = b = c = 1

# if a < 1000 / 3, a + b + c must be > 1000 because a < b < c
while a < 334:
    # b > a
    b = a + 1

    # a < b < c, so a + b cant be greater than 1000 * 2 / 3
    while a + b < 667:
        # a + b + c = 1000
        c = 1000 - (a + b)

        if b > c:
            break

        if a ** 2 + b ** 2 == c ** 2:
            print(a * b * c)

        b += 1

    a += 1
