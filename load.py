"""Includes methods to load meta-information and information about members' schedules."""

import csv
from person import Person

"""Gets emails and number of events attended from the schedules folder."""
def loadMeta():
	people_meta = []
	with open("schedules/info.csv", newline='') as csvfile:
		filereader = csv.reader(csvfile, delimiter=',', quotechar='|')
		first = 0
		for row in filereader:
			if first == 0:
				first = 1
				continue
			info = []
			info.append(str(row[0]))
			info.append(str(row[1]))
			info.append(int(row[2]))
			people_meta.append(info)
	return people_meta

"""Initializes person objects from csv files in the schedules folder."""
def loadPersons(people_meta):
	people = []
	for meta in people_meta:
		name = meta[0]
		email = meta[1]
		num_events = meta[2]
		with open("./schedules/" + name + ".csv", newline='') as csvfile:
			filereader = csv.reader(csvfile, delimiter=',', quotechar='|')
			first = 0
			schedule_dict = {}
			for row in filereader:
				if first == 0:
					first = 1
					continue
				availabilities = []
				day = 0
				for availability in row:
					if day == 0:
						day = availability
						continue
					if day not in schedule_dict.keys():
						schedule_dict[day] = []
					schedule_dict[day].append(True if str(availability) != "" else False)
			people.append(Person(name, email, schedule_dict, num_events))
	return people
