from os import path, mkdir, remove

import sys
import csv

times = ",9:00 AM,9:30 AM,10:00 AM,10:30 AM,11:00 AM,11:30 AM,12:00 PM,12:30 PM,1:00 PM,1:30 PM,2:00 PM,2:30 PM,3:00 PM,3:30 PM,4:00 PM,4:30 PM,5:00 PM,5:30 PM,6:00 PM,6:30 PM,7:00 PM,7:30 PM,8:00 PM,8:30 PM"
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
days_alternative = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

with open("Doodle.csv", newline='') as csvfile:
	filereader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in filereader:
		day_counter = 0
		name = row[0]
		availabilities = {}
		for day in days:
			quotidian = []
			for time in range(24):
				if row[1 + day_counter + day_counter * 24 + time] == "OK":
					quotidian.append("X")
				else:
					quotidian.append("")
			day_counter += 1
			availabilities[day] = quotidian
		if path.exists(name + ".csv"):
			remove(name + ".csv")
		file = open(name + ".csv", "w")
		file.write(times)
		file.write("\n")
		for day in days_alternative:
			file.write(",".join([day] + availabilities[day]))
			file.write("\n")
		file.close()
