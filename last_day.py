import datetime
def last_day_of_month():
    date = datetime.datetime.today()
    if (date.month == 12):
    	date_1 = date.replace(day=31)
    else:
    	date_1 = date.replace(month=date.month+1, day=1) - datetime.timedelta(days=1)
    return date_1.strftime("%dth %b %Y")
print last_day_of_month()