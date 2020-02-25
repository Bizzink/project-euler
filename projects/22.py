"""Problem 22

Using names.txt, a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order.
Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
What is the total of all the name scores in the file?"""


def worth(string):
    """get sum of char position values of string"""
    total = 0

    for char in string.lower():
        total += ord(char) - 96

    return total


data = open("resources/22_names.txt")
names = data.read().split(",")
data.close()

total = 0
sorted_names = {}

for name in names:
    name = name.strip('"')
    sorted_names[name] = worth(name)

for order, name in enumerate(sorted(sorted_names.keys())):
    total += (order + 1) * sorted_names[name]

print(total)
