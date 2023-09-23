import calendar

bdy = int(input("Enter your birth year: "))
bdm = int(input("Enter your birth month: "))
bdd = int(input("Enter your birth day: "))
cdy = int(input("Enter the current year: "))
cdm = int(input("Enter the current month: "))
cdd = int(input("Enter the current day: "))

kabise = calendar.leapdays(bdy, cdy)

year = cdy - bdy
month = cdm - bdm
day = cdd - bdd + kabise

if day < 0:
    day += 30
    month -= 1
if month < 0:
    month += 12
    year -= 1

mah = year * 12 + month
rooz = mah * 30 + day
saat = rooz * 24
daghighe = saat * 60
sanie = daghighe * 60

print("The duration of oxygen consumption is:\n{} years\n{} months\n{} days".format(year, month, day))
print("The duration in terms of:\n{} months\n{} days\n{} hours\n{} minutes\n{} seconds".format(mah, rooz, saat, daghighe, sanie))
print("You have experienced {} leap years.".format(kabise))
