from datetime import date, timedelta
import datetime
def get_first_day(dt):
    y, m = dt.year + 0, dt.month + 0
    a, m = divmod(m-1, 12)
    print m
    date_1 = datetime.datetime.strptime(str(date(y+a, m+1, 1)), '%Y-%m-%d')
    return date_1.strftime("%dst %B %Y %H:%M:%S")

print get_first_day(datetime.datetime.today())