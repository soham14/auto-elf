class Person:
	name = "Name Not Initialized"
	email = "Email Not Initialized"
	schedule_dict = {}
	events_attended = 0

	def __init__(self, name, email, schedule_dict, events_attended):
		self.name = name
		self.email = email
		self.schedule_dict = schedule_dict
		self.events_attended = events_attended

	def printSchedule(self):
		print(self.name + "'s Schedule:\n\n")
		hour = 9
		minute = 0
		for i in range(24):
			print(("12" if hour % 12 == 0 else str(hour % 12)) + ":" + ("00" if minute == 0 else "30") + " " + ("AM" if i < 6 else "PM") + "\t", end="")
			if minute == 0:
				minute = 30
			else:
				hour += 1
				minute = 0
		days = ["Monday", "Tuesday", "Wednesday", \
				"Thursday", "Friday", "Saturday", "Sunday"]
		for day in days:
			print(day + "\t")
			for time in self.schedule_dict[day]:
				print(("X" if time else "") + "\t")
			print("\n")

	def getName(self):
		return self.name

	def setName(self, name):
		self.name = name

	def getEmail(self):
		return self.email

	def setEmail(self, email):
		self.email = email

	def getSchedule(self):
		return self.schedule_dict

	def setSchedule(self, schedule_dict):
		self.schedule_dict = schedule_dict

	def getEventsAttended(self):
		return self.events_attended

	def setEventsAttended(self, events_attended):
		self.events_attended = events_attended
