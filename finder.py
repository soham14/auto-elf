"""Finds members available given a day and time."""

from load import loadMeta, loadPersons
from state import mem_time_code

def find():
	meta_information = loadMeta()
	people = loadPersons(meta_information)
	valid_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

	"""Finds the day of the event."""
	day = input("\nWhich day is the shift on? (format: Monday, Tuesday, etc.)\n>>> ")
	while day not in valid_days:
		print("\nPlease enter a valid day.\n")
		day = input("What is the day of the shift? (format: Monday, Tuesday, etc.)\n>>> ")
	"""Finds the time of the shift."""
	hour = 0
	minute = 0
	meridian = "XM"
	while minute not in [0, 30] or meridian not in ["AM", "PM"] or (hour < 1 or hour > 12):
		time = input("\nWhat is the time of the shift? (format: 5:00 PM, 6:30 PM, etc.)\n>>> ")
		meridian_split = time.split(" ")
		if len(meridian_split) != 2:
			print("\nPlease enter a valid time in 12 hour notation that is a multiple of 30 minutes.")
			hour = 0
			continue
		meridian = meridian_split[1]
		if meridian not in ["AM", "PM"]:
			print("\nPlease enter a valid time in 12 hour notation that is a multiple of 30 minutes.")
			hour = 0
			continue
		time_check = meridian_split[0].split(":")
		if len(time_check) != 2:
			print("\nPlease enter a valid time in 12 hour notation that is a multiple of 30 minutes.")
			hour = 0
			continue
		hour = int(time_check[0])
		minute = int(time_check[1])
	"""The adjusted time code is calculated to properly index into member availabilities."""
	time_code = ((0 if hour == 12 else hour) \
			  + (12 if meridian == "PM" else 0)) * 2 \
			  + (1 if minute == 30 else 0) \
			  - mem_time_code
	"""Creates and prints the list of members available for the time slot."""
	available_people = []
	if time_code > -1 and time_code < 24:
		available_people = list(filter(lambda person: person.getSchedule()[day][time_code], people[:]))
	if len(available_people) == 0:
		print("\nThere are no members available on " + day + " at " + time + ".")
	else:
		print("\nThe following members are available on " + day + " at " + time + ":")
		for person in available_people:
			print("* " + person.getName())
	print()
