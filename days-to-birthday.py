from datetime import date   

print "Please enter Your birthday (only numbers!):"
year = input("(example: 1992):")
month = input("Month (example: 7):")
day = input("Day In Month (example: 9):")

today = date.today()
birthday = date(today.year, month, day)
days_untill_birthday = birthday - today

print "In " + str(days_untill_birthday.days) + " days you will turn " + str(today.year - year) + ", Mazal Tov!!"


