"""Defines event logistics forms' state and behavior."""

from state import default_schedule

class Schedule:
	title = "Not Initialized"
	start_time = 0
	written_schedule = default_schedule

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
