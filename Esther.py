#NAME:KYOMUHENDO ESTHER DIANA
#REGISTRATION NUMBER:16/U/516
#STUDENT NUMBER:216000728
#COMPUTER YEAR ONE
import calendar #imports the calendar module from the python modules
from datetime import datetime
now = datetime.now()#gets the current date and time
age = int(input("Enter your age: "))
year = int(input('Enter year:'))
month = int(input("Enter the month: "))
day = int(input("Enter the day of the month: "))
cal = calendar.weekday(year,month,day)#calculates the day of the week
days = {0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}
print('You were born on',days[cal])#final statement that prints the day of week
