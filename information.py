from load import loadMeta, loadPersons

def info():
	"""
	The start time of all member schedules: 9:00 AM. The following four values can be adjusted
	if a different start time is filled out in the schedules given by members.
	"""
	mem_start_hour = 9
	mem_start_min = 0
	mem_start_meridian = "AM"
	mem_time_code = ((0 if mem_start_hour == 12 else mem_start_hour) \
				  + (12 if mem_start_meridian == "PM" else 0)) * 2 \
				  + (1 if mem_start_min == 30 else 0)

	name = input("\nWhat is the member's name?\n>>> ")
	meta_information = loadMeta()
	people = loadPersons(meta_information)
	person = list(filter(lambda p: p.name == name.strip(), people))

	if len(person) == 0:
		print("\nThe name " + name + " was not found in the directory of members.\n")
	elif len(person) > 1:
		print("\nError: multiple entries have been found for the name: " + name + "\n")
	else:
		member = person[0]
		print("\n* Name: " + member.getName() + "\n")
		print("* Email: " + member.getEmail() + "\n")
		print("* Events Attended: " + str(member.getEventsAttended()) + "\n")
		print("* Availabilities:\n")
		schedule = member.getSchedule()
		valid_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
		for day in valid_days:
			availabilities = []
			for i in range(len(schedule[day])):
				if schedule[day][i]:
					availabilities.append(("12" if (int((mem_time_code + i) / 2) % 12 == 0) else str(int((mem_time_code + i) / 2) % 12)) + ":" \
										+ ("00" if ((mem_time_code + i) % 2 == 0) else "30") \
										+ (" AM" if (mem_time_code + i) < 24 else " PM"))
			if len(availabilities) == 0:
				print("No availabilities for this day.")
			else:
				print("-- " + day + ": " + ", ".join(availabilities) + ".\n")
