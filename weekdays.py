def weekdays(day_left, day_returned):
	# Tells you what the day will be when you get back, if given the day you left and the amount of time you're leaving for.
	day_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
	return day_list[(day_left+day_returned)%7]

print(weekdays(0,7))