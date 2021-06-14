# Itzel Munoz Monroy PSID: 1888446
print("Age Calculator")
month = int(input("Please enter the current month as a number (no zeros on the left): "))
day = int(input("Please enter the current day (as a number): "))
year = int(input("Please enter the current year (as a number): "))
bmonth = int(input("Please enter your birthday month (no zeros on the left): "))
bday = int(input("Please enter your birthday day (as a number): "))
byear = int(input("Please enter your birthday year (as a number): "))
if month > bmonth or (month == bmonth and day >= bday):
    age = year - byear
else:
    age = year - byear - 1
print("You are", age, "years old.")
