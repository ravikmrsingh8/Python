from datetime import time
from datetime import date

if __name__ == "__main__":
    time1 = time(5,25,1)
    print(time1)
    print("{}|{}|{}".format(time1.hour, time1.minute,time1.second ))

    date1 = date(1992,1,12)
    print("Date {}/{}/{}".format(date1.day, date1.month, date1.year))
    print("Today:{}".format(date.today()))

    date2 = date.today()
    timedel = date2 - date1
    print("Time Delta {}".format(timedel))
    date3 = date1 + timedel
    print("{} + {} = {}".format(date1,timedel, date3))