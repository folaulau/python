from datetime import  date, datetime, timedelta

current_utc_datetime = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

print(current_utc_datetime)

todays_Date = datetime.now()
 
# Calling the isoformat() function over the
# today's date and time
print("isoformat: {}".format(todays_Date.isoformat()))

dto = datetime.strptime("2022-05-20T15:45:08Z", '%Y-%m-%dT%H:%M:%SZ')
print("dto: {}".format(dto))


# print(datetime.fromisoformat("2022-06-30T18:58:18.131"))

# now = datetime.now()
# print(now)
# dt_out = now.strftime("%Y-%m-%dT%H:%M:%SZ")
# print(dt_out)  # 2021-03-07T07:39:22Z


### convert str to datetime to epoch

# input string
date_string = '2023-03-13T20:13:48Z'

# convert string to datetime object
datetime_obj = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%SZ')

# convert datetime object to epoch timestamp
epoch = int(datetime_obj.timestamp())

# print the epoch timestamp
print("epoch:{}".format(epoch))