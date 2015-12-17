from datetime import date
import datetime
def monthdelta(date, delta):
    if ('datetime' in str(type(date))):
        m, y = (date.month-delta) % 12, date.year + ((date.month)-delta-1) // 12
        if not m: m = 12
        d = min(date.day, [31,29 if y%4==0 and not y%400==0 else 28,31,30,31,30,31,31,30,31,30,31][m-1])
        return date.replace(day=d,month=m, year=y)
    if (type(date) == str):
        date_1 = datetime.datetime.strptime(date, "%d/%m/%Y")
        m, y = (date_1.month-delta) % 12, date_1.year + ((date_1.month)-delta-1) // 12
        if not m: m = 12
        d = min(date_1.day, [31,29 if y%4==0 and not y%400==0 else 28,31,30,31,30,31,31,30,31,30,31][m-1])
        return date_1.replace(day=d,month=m, year=y)
print monthdelta('17/12/2015', 11)
