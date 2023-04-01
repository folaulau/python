
from datetime import  date, datetime, timedelta
import re
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

## epcho time
print("epoch")
epoch = datetime.now().strftime('%s')
print(epoch)

def generate_insight_avl_event_id(event_time,rule_id):
    numbers = re.findall('\d+', rule_id)
    id_number = numbers[0] if len(numbers) > 0 else 0
    # event_time == avl_event_time
    print("id_number:{}".format(id_number))
    #avl_event_id = <current time> + <event time> + <rule ID> + <row ID> - 16587833011658783305000000181400000002
    return int(datetime.now().strftime('%s')+""+event_time.strftime('%s')+""+str(id_number).zfill(10)+""+str(0).zfill(8))

avl_escalated_event_id = generate_insight_avl_event_id(datetime.now(),'AVL_R2684')

print("type: {}, id={}", type(avl_escalated_event_id).__name__, avl_escalated_event_id)


print("\n\ndatetime comparison")

# Define two datetime objects
date_time_1 = datetime(2023, 3, 24, 10, 30, 0)
date_time_2 = datetime(2023, 3, 25, 10, 30, 0)


# Check if date_time_1 is before date_time_2
if date_time_1 < date_time_2:
    print("date_time_1 is before date_time_2")
elif date_time_1 > date_time_2:
    print("date_time_1 is after date_time_2")
else:
    print("date_time_1 is equal date_time_2")

date_time_3 = datetime(2023, 3, 25, 10, 30, 0)

# Check if date_time_2 is before date_time_3
if date_time_2 < date_time_3:
    print("date_time_2 is before date_time_3")
elif date_time_2 > date_time_3:
    print("date_time_2 is before date_time_3")
else:
    print("date_time_2 is equal date_time_3")