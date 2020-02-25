"""Problem 24

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?"""


def get_next_permutation(digits):
    i = len(digits) - 1
    while i > 0:
        # get section from when digits[i] > digits[i - 1] to end
        if digits[i] > digits[i - 1]:
            ignore_section = digits[:i - 1]
            pivot = digits[i - 1]
            end_section = digits[i:]

            # find smallest number in section greater than digits[i - 1]
            swap = max(end_section)

            for num in end_section:
                if pivot < num < swap:
                    swap = num

            # swap pivot and swap
            end_section.append(pivot)
            pivot = swap
            end_section.remove(swap)

            # sort end section in ascending order
            end_section = sorted(end_section)

            # join sections back together

            ignore_section.append(pivot)
            ignore_section.extend(end_section)

            return ignore_section

        i -= 1


digits = "0123456789"
permutation_num = 1000000

digits = [int(digit) for digit in digits]

for i in range(permutation_num - 1):
    digits = get_next_permutation(digits)

digits = [str(digit) for digit in digits]
print("".join(digits))
