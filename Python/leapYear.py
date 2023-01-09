# one line func if condition consist of  2 conditions first one for century year and the second for normal year
# it will return true if any of 2 conditions is true else will return False
def is_leap(year):
    return (year % 400 == 0 and year % 100 == 0) or (year % 4 == 0 and year % 100 != 0)


y = int(input("Please Enter A year:"))
print(is_leap(y))
# test Cases
#  # False

# print(is_leap(2000))  # True

# print(is_leap(2400))  # True

# print(is_leap(2500))  # False
