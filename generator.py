"""Generates an optimal event logistics form."""

from state import mem_time_code, default_schedule
from schedule import Schedule
from load import loadMeta, loadPersons
from random import randint
from os import path, mkdir
from copy import deepcopy
import statistics as stat
import sys

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

	excluded_prompt = input("\nAre there any member exclusions? (format: Alan Turing, Grace Hopper, etc.)\n>>> ")

	if excluded_prompt != "":
		excluded_names = excluded_prompt.split(",")
		for name in excluded_names:
			excluded.append(name.strip())

	text_out = ["# Query Information\n\n", "## Event Information\n\n", "Title: " + title + "\n", "Day: " + day + "\n", "Time: " + time + "\n", \
				"Members Excluded: " + (", ".join(excluded) if len(excluded) != 0 else "None") + "\n\n"]

	def createELF():
		from schedule import Schedule
		new_elf = Schedule(title, time_code)
		created_schedule = deepcopy(default_schedule)
		slots_completed = []
		people_assigned = []
		slot = randint(0, len(created_schedule)-1)
		while len(created_schedule) != len(slots_completed):
			while (slot in slots_completed):
				slot = randint(0, len(created_schedule)-1)
			slots_completed.append(slot)
			shifts = created_schedule[slot][1]
			index = 0
			while shifts[index] == "BLANK":
				index += 1
			while index != len(shifts) and shifts[index] == "FILL_IN":
				if time_code + index < 0 or time_code + index > 23:
					created_schedule[slot][1][index] = "NONE_AVAILABLE"
					index += 1
					continue
				if index != 0 and shifts[index-1] != "BLANK" and shifts[index-1] != "NONE_AVAILABLE":
					prev = list(filter(lambda person: person.getName() == shifts[index-1], people[:]))
					if prev[0].getSchedule()[day][time_code + index]:
						created_schedule[slot][1][index] = prev[0].getName()
						index += 1
						continue
				available_people = list(filter(lambda person: person.getSchedule()[day][time_code + index] \
											   and person not in people_assigned \
											   and person.getName() not in excluded, people[:]))
				if len(available_people) == 0:
					created_schedule[slot][1][index] = "NONE_AVAILABLE"
					index += 1
					continue
				min_events_attended = min([person.getEventsAttended() for person in available_people])
				available_people = list(filter(lambda person: person.getEventsAttended() == min_events_attended, available_people))
				chosen_one = available_people[randint(0, len(available_people)-1)]
				created_schedule[slot][1][index] = chosen_one.getName()
				people_assigned.append(chosen_one)
				index += 1
		new_elf.setWrittenSchedule(created_schedule)
		return new_elf

	def findOptimalELF(iterations=10000):
		nonlocal text_out
		sample_elfs = {}
		excluded_sample_elfs = {}
		excluded_sample_count = 0
		print()
		curr_progress = 0
		sys.stdout.write("Generating " + str(iterations) + " sample schedules: [{0}{1}] 0.0%\r".format("#" * 0, " " * 9))
		sys.stdout.flush()
		for i in range(iterations):
			if curr_progress != int(i / (iterations / 1000)):
				sys.stdout.write("Generating " + str(iterations) + " sample schedules: [{0}{1}] {2}\r".format("#" * int(i / (iterations / 10)), " " * (10 - int(i / (iterations / 10))), str(100 * i/iterations) + "%"))
				sys.stdout.flush()
				curr_progress = int(i / (iterations / 1000))
			if i == iterations-1:
				sys.stdout.write("Generating " + str(iterations) + " sample schedules: [{0}{1}] {2}\r".format("##########", "", "100.0%"))
				sys.stdout.flush()
			sample_elf = createELF()
			sample_people = set([])
			num_unoccupied_shifts = 0
			for slot in sample_elf.getWrittenSchedule():
				for name in slot[1]:
					if name == "NONE_AVAILABLE":
						num_unoccupied_shifts += 1
					if name != "BLANK" and name != "NONE_AVAILABLE":
						sample_people.add(name)
			if num_unoccupied_shifts > 0:
				excluded_sample_count += 1
				if num_unoccupied_shifts not in excluded_sample_elfs.keys():
					excluded_sample_elfs[num_unoccupied_shifts] = [sample_elf.getWrittenSchedule()]
				else:
					excluded_sample_elfs[num_unoccupied_shifts].append(sample_elf.getWrittenSchedule())
			else:
				if len(sample_people) not in sample_elfs.keys():
					sample_elfs[len(sample_people)] = [sample_elf.getWrittenSchedule()]
				else:
					sample_elfs[len(sample_people)].append(sample_elf.getWrittenSchedule())
		key_list = []
		for key in sample_elfs.keys():
			for values in sample_elfs[key]:
				key_list.append(key)
		excluded_key_list = []
		for key in excluded_sample_elfs.keys():
			for values in excluded_sample_elfs[key]:
				excluded_key_list.append(key)
		print("\n\n" + str(excluded_sample_count) + " samples had inoccupiable shifts and were excluded.")
		text_out.append("\n" + str(excluded_sample_count) + " samples had inoccupiable shifts and were excluded.\n")
		if len(sample_elfs.keys()) != 0:
			print("\nStatistics for number of members in " + str(iterations - excluded_sample_count) + " non-excluded sample ELFs:\n")
			print("* Minimum: " + str(min(key_list)))
			print("* Maximum: " + str(max(key_list)))
			print("* Median: " + str(stat.median(key_list)))
			print("* Mean: " + str(stat.mean(key_list)))
			print("* Mode: " + str(stat.mode(key_list)))
			text_out.append("\nStatistics for number of members in " + str(iterations - excluded_sample_count) + " non-excluded sample ELFs:\n\n")
			text_out += ["Minimum: " + str(min(key_list)) + "\n", "Maximum: " + str(max(key_list)) + "\n", "Median: " + str(stat.median(key_list)) + "\n", \
						 "Mean: " + str(stat.mean(key_list)) + "\n", "Mode: " + str(stat.mode(key_list)) + "\n"]
			if len(sample_elfs.keys()) > 1:
				print("* Standard Deviation: " + str(stat.stdev(key_list)))
				print("* Variance: " + str(stat.variance(key_list)) + "\n")
				text_out += ["Standard Deviation: " + str(stat.stdev(key_list)) + "\n", "Variance: " + str(stat.variance(key_list)) + "\n\n"]
			else:
				print()
				text_out.append("\n\n")
			for key in sorted(sample_elfs.keys()):
				stars = int(len(list(filter(lambda k: k == key, key_list))) / (iterations / 100))
				print(str(key) + " = |" + stars * "*")
				text_out.append(str(key) + " = |" + stars * "*" + "\n")
		else:
			print("\nStatistics for number of unoccupied shifts in " + str(excluded_sample_count) + " excluded sample ELFs:\n")
			print("* Minimum: " + str(min(excluded_key_list)))
			print("* Maximum: " + str(max(excluded_key_list)))
			print("* Median: " + str(stat.median(excluded_key_list)))
			print("* Mean: " + str(stat.mean(excluded_key_list)))
			print("* Mode: " + str(stat.mode(excluded_key_list)))
			text_out.append("\nStatistics for number of unoccupied shifts in " + str(excluded_sample_count) + " excluded sample ELFs:\n\n")
			text_out += ["Minimum: " + str(min(excluded_key_list)) + "\n", "Maximum: " + str(max(excluded_key_list)) + "\n", "Median: " + str(stat.median(excluded_key_list)) + "\n", \
						 "Mean: " + str(stat.mean(excluded_key_list)) + "\n", "Mode: " + str(stat.mode(excluded_key_list)) + "\n"]
			if len(excluded_sample_elfs.keys()) > 1:
				print("* Standard Deviation: " + str(stat.stdev(excluded_key_list)))
				print("* Variance: " + str(stat.variance(excluded_key_list)) + "\n")
				text_out += ["Standard Deviation: " + str(stat.stdev(excluded_key_list)) + "\n", "Variance: " + str(stat.variance(excluded_key_list)) + "\n\n"]
			else:
				print()
				text_out.append("\n\n")
			for key in sorted(excluded_sample_elfs.keys()):
				stars = int(len(list(filter(lambda k: k == key, excluded_key_list))) / (iterations / 10))
				print(str(key) + " = |" + stars * "*")
				text_out.append(str(key) + " = |" + stars * "*" + "\n")
		if len(sample_elfs.keys()) != 0:
			if int(stat.median(sample_elfs.keys())) in sample_elfs.keys() and int(stat.median(sample_elfs.keys())) == stat.median(sample_elfs.keys()):
				elf.setWrittenSchedule(sample_elfs[int(stat.median(sample_elfs.keys()))][randint(0,len(sample_elfs[int(stat.median(sample_elfs.keys()))])-1)])
				return elf
			else:
				median = stat.median(sample_elfs.keys())
				median_chosen = 0
				if abs(stat.median(sample_elfs.keys()) - stat.median_low(sample_elfs.keys())) < abs(stat.median(sample_elfs.keys()) - stat.median_high(sample_elfs.keys())):
					median_chosen = stat.median_low(sample_elfs.keys())
				else:
					median_chosen = stat.median_high(sample_elfs.keys())
				elf.setWrittenSchedule(sample_elfs[median_chosen][randint(0,len(sample_elfs[median_chosen])-1)])
				return elf
		else:
			lowest_unoccupied = min(excluded_sample_elfs.keys())
			elf.setWrittenSchedule(excluded_sample_elfs[lowest_unoccupied][randint(0,len(excluded_sample_elfs[lowest_unoccupied])-1)])
			return elf


	iter_input = input("\nHow many sample schedules should be created to find the optimal schedule? (recommended: 10000)\n>>> ")

	text_out.append("## Sampling Information\n\n")
	text_out.append("Schedule Sample Size: " + str(iter_input) + "\n")

	def numCheck(inp):
		try:
			int(inp)
			return True
		except ValueError:
			return False

	while int(iter_input) < 1 and not numCheck(iter_input):
		print("\nPlease enter a nonzero number.\n")
		iter_input = input("\nHow many iterations should be run to find the optimal schedule? (defaults to 10000)\n>>> ")

	elf = findOptimalELF(int(iter_input))

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
		nonlocal text_out
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
		"""Prints the table into the terminal."""
		print("\nAssignments:\n")
		text_out.append("\n## Assignments\n\n")
		for entry in table:
			print(" -- " + entry[0] + " for " + entry[1] + " at " + entry[2] + " - " + entry[3] + ".")
			text_out.append(" -- " + entry[0] + " for " + entry[1] + " at " + entry[2] + " - " + entry[3] + ".\n")
		print("\nSchedule generated successfully. The ELF's location is `ELFs/" + dir_name + "/ELF.csv`.\n")
		text_out.append("\nSchedule generated successfully. The ELF's location is `ELFs/" + dir_name + "/ELF.csv`.\n")

	def writeQueryInfo():
		query_file = open("./ELFs/" + dir_name + "/query.txt", "w")
		for line in text_out:
			query_file.write(line)
		query_file.close()

	dir_name = writeFile()
	writeTable(dir_name)
	writeQueryInfo()
