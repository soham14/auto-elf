from schedule import Schedule
from load import loadMeta, loadPersons
from random import randint
from os import path, mkdir

def generate():
	unusable_chars = ["#", "%", "&", "{", "}", "\\", "<", ">",
					  "*", "?", "/", "$", "!", "'", "\"", ":",
					  "@", "+", "`", "|", "="]

	title = input("\nWhat is the title of the event? (format: Alan Turing at the Berkeley Forum)\n>>> ")

	def charCheck(new_title):
		for character in unusable_chars:
			if character in new_title:
				return False
		return True

	while not charCheck(title):
		print("\nPlease enter a title without the following characters: " + ", ".join(unusable_chars) + ".\n")
		title = input("What is the title of the event? (format: Alan Turing at the Berkeley Forum)\n>>> " )

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

	day = input("\nWhat is the day of the event? (format: Monday, Tuesday, etc.)\n>>> ")
	valid_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

	while day not in valid_days:
		print("\nPlease enter a valid day.\n")
		day = input("What is the day of the event? (format: Monday, Tuesday, etc.)\n>>> ")

	hour = 0
	minute = 0
	meridian = "XM"

	while minute not in [0, 30] or meridian not in ["AM", "PM"] or (hour < 1 or hour > 12):
		time = input("\nWhat is the time of the event? (format: 5:00 PM, 6:30 PM, etc.)\n>>> ")
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
			  - mem_time_code \
			  - 3

	elf = Schedule(title, time_code)
	new_schedule = elf.getWrittenSchedule()

	meta_information = loadMeta()
	people = loadPersons(meta_information)

	excluded = []

	excluded_prompt = input("\nAre there any exclusions? (format: Alan Turing, Grace Hopper, etc.)\n>>> ")

	if excluded_prompt != "":
		excluded_names = excluded_prompt.split(",")
		for name in excluded_names:
			excluded.append(name.strip())

	def createELF():
		slots_completed = []
		people_assigned = []
		slot = randint(0, len(new_schedule)-1)
		while len(new_schedule) != len(slots_completed):
			while (slot in slots_completed):
				slot = randint(0, len(new_schedule)-1)
			slots_completed.append(slot)
			shifts = new_schedule[slot][1]
			index = 0
			while shifts[index] == "BLANK":
				index += 1
			while index != len(shifts) and shifts[index] == "FILL_IN":
				if time_code + index > 23:
					shifts[index] = "NONE_AVAILABLE"
					index += 1
					continue
				if index != 0 and shifts[index-1] != "BLANK" and shifts[index-1] != "NONE_AVAILABLE":
					prev = list(filter(lambda person: person.getName() == shifts[index-1], people[:]))
					if prev[0].getSchedule()[day][time_code + index]:
						shifts[index] = prev[0].getName()
						index += 1
						continue
				available_people = list(filter(lambda person: person.getSchedule()[day][time_code + index] \
											   and person not in people_assigned \
											   and person.getName() not in excluded, people[:]))
				if len(available_people) == 0:
					shifts[index] = "NONE_AVAILABLE"
					index += 1
					continue
				min_events_attended = min([person.getEventsAttended() for person in available_people])
				available_people = list(filter(lambda person: person.getEventsAttended() == min_events_attended, available_people))
				chosen_one = available_people[randint(0, len(available_people)-1)]
				shifts[index] = chosen_one.getName()
				people_assigned.append(chosen_one)
				index += 1
		elf.setWrittenSchedule(new_schedule)
		return elf

	elf = createELF()

	def writeFile():
		"""Creates the heading times for the schedule."""
		local_time = ((0 if hour == 12 else hour) \
			  + (12 if meridian == "PM" else 0)) * 2 \
			  + (1 if minute == 30 else 0) \
			  - 3
		local_times = []
		local_times.append("")
		for i in range(7):
			local_times.append(("12" if (int((local_time + i) / 2) % 12 == 0) else str(int((local_time + i) / 2) % 12)) + ":" \
							 + ("00" if ((local_time + i) % 2 == 0) else "30") \
							 + (" AM" if (local_time + i) < 24 else " PM"))
		"""Creates the directory for the ELF files."""
		dir_name = title
		if path.exists("./ELFs/" + dir_name):
			i = 1
			title_copy = dir_name
			while path.exists("./ELFs/" + dir_name):
				dir_name = title_copy + " (" + str(i) + ")"
				i += 1
		mkdir("./ELFs/" + dir_name)
		"""Creates the CSV file that holds the generated schedule."""
		schedule_file = open("./ELFs/" + dir_name + "/ELF.csv", "w")
		schedule_file.write(",".join(local_times))
		schedule_file.write("\n")
		for slot in elf.getWrittenSchedule():
			schedule_file.write(",".join([slot[0]] + slot[1]))
			schedule_file.write("\n")
		schedule_file.close()
		return dir_name
		
	def writeTable(dir_name):
		names_found = {}
		name_to_position = {}
		for slot in elf.getWrittenSchedule():
			shifts = slot[1]
			index = 0
			name_found = "BLANK"
			for shift in shifts:
				if shift != "BLANK" and shift != "NONE_AVAILABLE":
					name_found = shift
					name_to_position[name_found] = slot[0]
					if name_found not in names_found.keys():
						names_found[name_found] = [index]
					else:
						names_found[name_found].append(index)
				index += 1
		name_keys = sorted(names_found.keys())
		table = []
		for name in name_keys:
			position_name = name_to_position[name]
			start_time = names_found[name][0] + time_code + mem_time_code
			start_shift = ("12" if (int((start_time) / 2) % 12 == 0) else str(int((start_time) / 2) % 12)) + ":" \
						+ ("00" if ((start_time) % 2 == 0) else "30") \
						+ (" AM" if (start_time) < 24 else " PM")
			end_time = names_found[name][len(names_found[name])-1] + time_code + mem_time_code + 1
			end_shift = ("12" if (int((end_time) / 2) % 12 == 0) else str(int((end_time) / 2) % 12)) + ":" \
						+ ("00" if ((end_time) % 2 == 0) else "30") \
						+ (" AM" if (end_time) < 24 else " PM")
			email = list(filter(lambda person: person.getName() == name, people))[0].getEmail()
			entry = [name, position_name, start_shift, end_shift, email]
			table.append(entry)
		table_file = open("./ELFs/" + dir_name + "/table.csv", "w")
		table_file.write(",".join(["Name", "Position", "Shift Start Time", "Shift End Time", "Email"]))
		table_file.write("\n")
		for entry in table:
			table_file.write(",".join(entry))
			table_file.write("\n")
		table_file.close()

	dir_name = writeFile()
	writeTable(dir_name)

	print("\nSchedule generated successfully.\n")
