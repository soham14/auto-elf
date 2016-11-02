class Schedule:
	title = "Not Initialized"
	start_time = 0
	written_schedule = [
		["Cage Oversight", ["FILL_IN", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK"]],
		["Cage Transport", ["FILL_IN", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK"]],
		["Cage Transport", ["FILL_IN", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK"]],
		["Stage Set Up", ["BLANK", "FILL_IN", "FILL_IN", "BLANK", "BLANK", "BLANK", "BLANK"]],
		["Stage Set Up", ["BLANK", "FILL_IN", "FILL_IN", "BLANK", "BLANK", "BLANK", "BLANK"]],
		["Registration Set Up", ["BLANK", "FILL_IN", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK"]],
		["Registration Check In", ["BLANK", "BLANK", "FILL_IN", "FILL_IN", "BLANK", "BLANK", "BLANK"]],
		["Registration Check In", ["BLANK", "BLANK", "FILL_IN", "FILL_IN", "BLANK", "BLANK", "BLANK"]],
		["Registration Usher", ["BLANK", "BLANK", "FILL_IN", "FILL_IN", "BLANK", "BLANK", "BLANK"]],
		["Tech Oversight/Set Up", ["BLANK", "FILL_IN", "FILL_IN", "FILL_IN", "FILL_IN", "FILL_IN", "BLANK"]],
		["Photographer", ["BLANK", "BLANK", "FILL_IN", "FILL_IN", "FILL_IN", "FILL_IN", "BLANK"]],
		["Social Media", ["BLANK", "BLANK", "BLANK", "FILL_IN", "FILL_IN", "BLANK", "BLANK"]],
		["Utility", ["BLANK", "BLANK", "FILL_IN", "FILL_IN", "FILL_IN", "FILL_IN", "BLANK"]],
		["Cage Oversight", ["BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "FILL_IN", "FILL_IN"]],
		["Cage Transport", ["BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "FILL_IN", "FILL_IN"]],
		["Cage Transport", ["BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "FILL_IN", "FILL_IN"]]
	]

	"""Takes in a string as a start time and initializes a schedule."""
	def __init__(self, title, start_time):
		self.title = title
		self.start_time = start_time

	def setStartTime(self, start_time):
		self.start_time = start_time

	def getStartTime(self):
		return self.start_time

	def setWrittenSchedule(self, written_schedule):
		self.written_schedule = written_schedule

	def getWrittenSchedule(self):
		return self.written_schedule
