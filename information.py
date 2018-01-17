"""Returns information on file for a member."""

from load import loadMeta, loadPersons
from state import mem_time_code

def info():
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
				print("-- " + day + ": " + "No availabilities for this day.\n")
			else:
				print("-- " + day + ": " + ", ".join(availabilities) + ".\n")
