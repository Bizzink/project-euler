"""Problem 19

You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?"""


months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

year = 1900
month = 0
day = 1
sundays = 0

while year < 2001:
    while month < 12:
        # increase day by month length
        if year % 4 == 0 and month == 1:
            if year % 100 == 0 and year % 400 != 0:
                day += 28
            else:
                day += 29
        else:
            day += months[month]

        # day % 7 = 0 : day is sunday
        if year > 1900 and day % 7 == 0:
            sundays += 1

        month += 1

    year += 1
    month = 0

print(sundays)
