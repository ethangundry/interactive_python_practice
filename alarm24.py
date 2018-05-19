def alarm24(current_time, alarm_time):
	return (current_time+alarm_time)%24

print(alarm24(10,50))