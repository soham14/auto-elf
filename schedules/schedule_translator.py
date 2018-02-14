from os import path, mkdir, remove

import sys
import csv

times = ",9:00 AM,9:30 AM,10:00 AM,10:30 AM,11:00 AM,11:30 AM,12:00 PM,12:30 PM,1:00 PM,1:30 PM,2:00 PM,2:30 PM,3:00 PM,3:30 PM,4:00 PM,4:30 PM,5:00 PM,5:30 PM,6:00 PM,6:30 PM,7:00 PM,7:30 PM,8:00 PM,8:30 PM,9:00 PM"
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

with open("Auto-ELF Availabilities (Responses) - Form Responses 1.csv", newline='') as csvfile:
	filereader = csv.reader(csvfile, skipinitialspace=True)
	first = True
	for row in filereader:
		if first:
			first = False
			continue
		day_counter = 0
		email, name = row[26], row[27]
		availabilities = {"Sunday": [], "Monday": [], "Tuesday": [],
			"Wednesday": [], "Thursday": [], "Friday": [],
			"Saturday": []}
		for i in range(1, 26):
			days_found = row[i].split(",")
			for j in range(len(days_found)):
				days_found[j] = days_found[j].strip()
			for day in days:
				availabilities[day].append("X" if day in days_found else "")
		if path.exists(name + ".csv"):
			remove(name + ".csv")
		file = open(name + ".csv", "w")
		file.write(times)
		file.write("\n")
		for day in days:
			file.write(",".join([day] + availabilities[day]))
			file.write("\n")
		file.close()
