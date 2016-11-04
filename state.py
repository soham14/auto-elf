"""Maintains the state of the program."""

"""Default seven shift event logistics template."""
default_schedule = [
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

"""Default start time for all members' schedules. Currently set to 9:00 AM."""
mem_start_hour = 9
mem_start_min = 0
mem_start_meridian = "AM"
mem_time_code = ((0 if mem_start_hour == 12 else mem_start_hour) \
			  + (12 if mem_start_meridian == "PM" else 0)) * 2 \
			  + (1 if mem_start_min == 30 else 0)