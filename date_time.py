
from datetime import  date, datetime, timedelta


# taking input as the current date
# today() method is supported by date 
# class in datetime module
Begindatestring = date.today()
  
# print begin date
print("Beginning date")
print(Begindatestring)
  
# calculating end date by adding 4 days
Enddate = Begindatestring - timedelta(days=4)
  
# printing end date
print("Ending date")
print(Enddate)