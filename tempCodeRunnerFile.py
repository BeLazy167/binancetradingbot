from datetime import datetime, date
x = 1618073400000.0//1000
timestamp = datetime.fromtimestamp(x)
print("Date =", timestamp)


print(datetime.fromtimestamp(epoch))
        datetime_object = datetime.now()
        print(datetime_object)
        d2 = datetime.today()
        unixtime2 = time.mktime(d2.timetuple())
        print("Timestamp of now: ", unixtime2)