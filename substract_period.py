from datetime import date
import datetime
from datetime import timedelta 
def sub_delta(date_1, delta, what):
    if ('datetime' in str(type(date))):
        if((what == 'month') or (what == 'months')):
            m, y = (date_1.month-delta) % 12, date_1.year + ((date_1.month)-delta-1) // 12
            if not m: m = 12
            d = min(date_1.day, [31,29 if y%4==0 and not y%400==0 else 28,31,30,31,30,31,31,30,31,30,31][m-1])
            return date_1.replace(day=d,month=m, year=y)
        elif ((what == 'year') or (what == 'years')):
             return date_1 - timedelta(days= int(delta)*365)  

    if (type(date) == str):
        date_2 = datetime.datetime.strptime(date_1, "%d/%m/%Y")
        m, y = (date_2.month-delta) % 12, date_2.year + ((date_2.month)-delta-1) // 12
        if not m: m = 12
        d = min(date_2.day, [31,29 if y%4==0 and not y%400==0 else 28,31,30,31,30,31,31,30,31,30,31][m-1])
        return date_2.replace(day=d,month=m, year=y)
print sub_delta(datetime.datetime.today(), 11, 'month')
