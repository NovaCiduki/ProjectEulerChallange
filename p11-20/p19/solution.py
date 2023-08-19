# f = k + [(13*m-1)/5] + D + [D/4] + [C/4] – 2*C.
# k is the day of the month. Let’s use January 29, 2064 as an example. For this date, k = 29.
# m is the month number.
# Months have to be counted specially for Zeller’s Rule: March is 1, April is 2, and so on to February, which is 12.
# (This makes the formula simpler, because on leap years February 29 is counted as the last day of the year.)
# Because of this rule, January and February are always counted as the 11th and 12th months of the previous year.
# In our example, m = 11.
# D is the last two digits of the year.
# Because in our example we are using January (see previous bullet) D = 63 even though we are using a date from 2064.
# C stands for century: it’s the first two digits of the year. In our case, C = 20.
# [] is the floor function so [x] = floor(x)

# day number to string = dnts
dnts = {
    0: "Sunday",
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday"
}
# month to number of day
mtnod = {
    1: 31,  # January - 31 days
    2: 28,  # February - 28 days in a common year and 29 days in leap years
    3: 31,  # March - 31 days
    4: 30,  # April - 30 days
    5: 31,  # May - 31 days
    6: 30,  # June - 30 days
    7: 31,  # July - 31 days
    8: 31,  # August - 31 days
    9: 30,  # September - 30 days
    10: 31,  # October - 31 days
    11: 30,  # November - 30 days
    12: 31  # December - 31 days
}
mtnod_leap = {
    1: 31,
    2: 29,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}


def is_leap_year(year):
    if year % 100 == 0:
        return year % 400 == 0
    else:
        return year % 4 == 0


def days_until_date_from_1900(days, months, years):
    leap = is_leap_year(years)
    if days < 1 or months < 1 or years < 1900:
        print("something is too small")
        return -1
    if months > 12:
        print("month is too big")
        return -1
    if leap:
        if days > mtnod_leap[months]:
            print("days it too big")
            return -1
    else:
        if days > mtnod[months]:
            print("days it too big")
            return -1
    tot = 0
    for year in range(1900, years):
        if is_leap_year(year):
            tot += 366
        else:
            tot += 365
    for month in range(1, months):
        if leap:
            tot += mtnod_leap[month]
        else:
            tot += mtnod[month]
    tot += (days - 1)
    return tot


def day_of_week(days, months, years):
    days = days_until_date_from_1900(days, months, years)
    start = 1  # 1 jun 1900 was a monday
    day = (start + days) % 7
    return day


ans = 0
for year in range(1901, 2001):
    for month in range(1, 13):
        if day_of_week(1, month, year) == 0:
            ans += 1
print(ans)