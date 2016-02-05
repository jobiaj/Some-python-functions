def current_date_time(format):
	import datetime
	return datetime.date.today().strftime(format)
print current_date_time("%B %d, %Y")
print current_date_time("%I:%M%p on %B %d, %Y")
