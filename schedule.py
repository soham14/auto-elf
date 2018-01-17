"""Defines event logistics forms' state and behavior."""

from state import single_speaker_schedule, multi_speaker_schedule

class Schedule:
	title = "Not Initialized"
	start_time = 0
	written_schedule = []

	"""Takes in a string as a start time and initializes a schedule."""
	def __init__(self, title, start_time, event_type):
		self.title = title
		self.start_time = start_time
		self.written_schedule = (single_speaker_schedule if event_type == "single" else multi_speaker_schedule)

	def setStartTime(self, start_time):
		self.start_time = start_time

	def getStartTime(self):
		return self.start_time

	def setWrittenSchedule(self, written_schedule):
		self.written_schedule = written_schedule

	def getWrittenSchedule(self):
		return self.written_schedule
