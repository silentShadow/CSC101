#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
#
#

import datetime

# Get users birthday
bday = input("What is your birthday?(mm-dd-yy) ")


# Datetime is called twice here because strptime function is being called
#+ That function is part of the datetime class
#+ Which is also a part of the datetime module
#+ Hence datetime being called twice
bday = datetime.datetime.strptime(bday,"%m-%d-%y").date()

currentDate = datetime.date.today()

days = currentDate - bday
print(days)
print(currentDate)
print(currentDate.strftime('%d %b, %y'))


# Format option 1
print( "Your birth month is " + bday.strftime('%B') )

# Format option 2
print( "Hey, your birth month is {}".format(bday.strftime('%B')) )
