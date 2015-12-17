from datetime import date
import datetime
def new_date(start_date, howmany):
	if (type(start_date) == str):
		date_1 = datetime.datetime.strptime(start_date, "%d/%m/%Y")
		endDate = date(date_1.year + int(howmany), date_1.month, date_1.day)
		print  endDate  
		#end_date = (date_1 + datetime.timedelta(6*365/12)).isoformat()
	elif('datetime' in str(type(start_date))):
		date_1 = start_date
		end_date = (date_1 + datetime.timedelta(6*365/12)).isoformat()
		print end_date
new_date('11/10/2015', 10)
