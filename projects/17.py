"""Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage."""


def letter_count(num):
    num = str(num)
    word_number = ""

    ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    if len(num) == 4:
        word_number += ones[int(num[0]) - 1] + "thousand"
        num = num[1:]

    if len(num) == 3:
        if num[0] != "0":
            word_number += ones[int(num[0]) - 1] + "hundred"

        num = num[1:]

    if int(num) != 0:
        if len(word_number) > 0:
            word_number += "and"

    if len(num) == 2:
        if num[0] == "1":
            word_number += teens[int(num[1])]

        else:
            if num[0] != "0":
                word_number += tens[int(num[0]) - 2]
            num = num[1:]

    if len(num) == 1:
        if num != "0":
            word_number += ones[int(num) - 1]

    return len(word_number)


total = 0

for i in range(1, 1001):
    total += letter_count(i)

print(total)
