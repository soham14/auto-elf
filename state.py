"""Maintains the state of the program."""

"""Default seven shift talk event logistics template."""
single_speaker_schedule = [
	["Cage Oversight", ["FILL_IN", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK"]],
	["Cage Transport", ["FILL_IN", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK"]],
	["Cage Transport", ["FILL_IN", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK"]],
	["Stage Set Up", ["BLANK", "FILL_IN", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK"]],
	["Stage Set Up", ["BLANK", "FILL_IN", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK"]],
	["Registration Set Up", ["BLANK", "FILL_IN", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK"]],
	["Registration Check In", ["BLANK", "BLANK", "FILL_IN", "BLANK", "BLANK", "BLANK", "BLANK"]],
	["Registration Check In", ["BLANK", "BLANK", "FILL_IN", "BLANK", "BLANK", "BLANK", "BLANK"]],
	["Registration Usher", ["BLANK", "BLANK", "FILL_IN", "BLANK", "BLANK", "BLANK", "BLANK"]],
	["Late Registration Check In", ["BLANK", "BLANK", "BLANK", "FILL_IN", "FILL_IN", "BLANK", "BLANK"]],
	["Tech Oversight/Set Up", ["BLANK", "FILL_IN", "FILL_IN", "FILL_IN", "FILL_IN", "FILL_IN", "BLANK"]],
	["Photographer", ["BLANK", "BLANK", "FILL_IN", "FILL_IN", "FILL_IN", "FILL_IN", "BLANK"]],
	["Social Media", ["BLANK", "BLANK", "BLANK", "FILL_IN", "FILL_IN", "BLANK", "BLANK"]],
	["Utility", ["BLANK", "BLANK", "FILL_IN", "FILL_IN", "FILL_IN", "FILL_IN", "BLANK"]],
	["Cage Oversight", ["BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "FILL_IN", "BLANK"]],
	["Cage Transport", ["BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "FILL_IN", "BLANK"]],
	["Cage Transport", ["BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "FILL_IN", "BLANK"]],
        ["Poster Printing", ["FILL_IN", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK"]]
]

"""Default seven shift debate/panel event logistics template."""
multi_speaker_schedule = [
	["Cage Oversight", ["FILL_IN", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK"]],
	["Cage Transport", ["FILL_IN", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK"]],
	["Cage Transport", ["FILL_IN", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK"]],
	["Stage Set Up", ["BLANK", "FILL_IN", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK"]],
	["Stage Set Up", ["BLANK", "FILL_IN", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK"]],
	["Registration Set Up", ["BLANK", "FILL_IN", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK"]],
	["Registration Check In", ["BLANK", "BLANK", "FILL_IN", "BLANK", "BLANK", "BLANK", "BLANK"]],
	["Registration Check In", ["BLANK", "BLANK", "FILL_IN", "BLANK", "BLANK", "BLANK", "BLANK"]],
	["Registration Usher", ["BLANK", "BLANK", "FILL_IN", "BLANK", "BLANK", "BLANK", "BLANK"]],
	["Late Registration Check In", ["BLANK", "BLANK", "BLANK", "FILL_IN", "FILL_IN", "FILL_IN", "BLANK"]],
	["Tech Oversight/Set Up", ["BLANK", "FILL_IN", "FILL_IN", "FILL_IN", "FILL_IN", "FILL_IN", "FILL_IN"]],
	["Photographer", ["BLANK", "BLANK", "FILL_IN", "FILL_IN", "FILL_IN", "FILL_IN", "FILL_IN"]],
	["Social Media", ["BLANK", "BLANK", "BLANK", "FILL_IN", "FILL_IN", "FILL_IN", "BLANK"]],
	["Utility", ["BLANK", "BLANK", "FILL_IN", "FILL_IN", "FILL_IN", "FILL_IN", "FILL_IN"]],
	["Cage Oversight", ["BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "FILL_IN"]],
	["Cage Transport", ["BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "FILL_IN"]],
	["Cage Transport", ["BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "FILL_IN"]],
        ["Poster Printing", ["FILL_IN", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK"]]
]

"""Default start time for all members' schedules. Currently set to 9:00 AM."""
mem_start_hour = 9
mem_start_min = 0
mem_start_meridian = "AM"
mem_time_code = ((0 if mem_start_hour == 12 else mem_start_hour) \
			  + (12 if mem_start_meridian == "PM" else 0)) * 2 \
			  + (1 if mem_start_min == 30 else 0)

"""Returns a single speaker schedule template transformed to a more consistently linear format."""
single_transform = [
	["Cage Oversight", ["FILL_IN", "FILL_IN", "FILL_IN", "BLANK", "BLANK", "BLANK", "BLANK"]],
	["Cage Transport", ["FILL_IN", "FILL_IN", "FILL_IN", "BLANK", "BLANK", "BLANK", "BLANK"]],
	["Cage Transport", ["FILL_IN", "FILL_IN", "FILL_IN", "FILL_IN", "FILL_IN", "FILL_IN", "BLANK"]],
	["Stage Set Up", ["BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK"]],
	["Stage Set Up", ["BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK"]],
	["Registration Set Up", ["BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK"]],
	["Registration Check In", ["BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK"]],
	["Registration Check In", ["BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK"]],
	["Registration Usher", ["BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK"]],
	["Late Registration Check In", ["BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK"]],
	["Tech Oversight/Set Up", ["BLANK", "FILL_IN", "FILL_IN", "FILL_IN", "FILL_IN", "FILL_IN", "BLANK"]],
	["Photographer", ["BLANK", "BLANK", "FILL_IN", "FILL_IN", "FILL_IN", "FILL_IN", "BLANK"]],
	["Social Media", ["BLANK", "BLANK", "BLANK", "FILL_IN", "FILL_IN", "FILL_IN", "BLANK"]],
	["Utility", ["BLANK", "BLANK", "FILL_IN", "FILL_IN", "FILL_IN", "FILL_IN", "BLANK"]],
	["Cage Oversight", ["BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "FILL_IN", "BLANK"]],
	["Cage Transport", ["BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK"]],
	["Cage Transport", ["BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK"]]
]

"""Transforms single speaker schedule back to default format."""
def single_inverse(schedule):
	col_1 = [row[1][1] for row in schedule]
	schedule[0][1][1] = "BLANK"
	schedule[1][1][1] = "BLANK"
	schedule[2][1][1] = "BLANK"
	schedule[3][1][1] = col_1[0]
	schedule[4][1][1] = col_1[1]
	schedule[5][1][1] = col_1[2]
	col_2 = [row[1][2] for row in schedule]
	schedule[0][1][2] = "BLANK"
	schedule[1][1][2] = "BLANK"
	schedule[2][1][2] = "BLANK"
	schedule[6][1][2] = col_2[0]
	schedule[7][1][2] = col_2[1]
	schedule[8][1][2] = col_2[2]
	col_3 = [row[1][3] for row in schedule]
	schedule[2][1][3] = "BLANK"
	schedule[9][1][3] = col_3[2]
	col_4 = [row[1][4] for row in schedule]
	schedule[2][1][4] = "BLANK"
	schedule[9][1][4] = col_4[2]
	col_5 = [row[1][5] for row in schedule]
	schedule[2][1][5] = "BLANK"
	schedule[12][1][5] = "BLANK"
	schedule[15][1][5] = col_5[2]
	schedule[16][1][5] = col_5[12]
	return schedule

"""Returns a multiple speaker schedule template transformed to a more consistently linear format."""
multiple_transform = [
	["Cage Oversight", ["FILL_IN", "FILL_IN", "FILL_IN", "BLANK", "BLANK", "BLANK", "BLANK"]],
	["Cage Transport", ["FILL_IN", "FILL_IN", "FILL_IN", "BLANK", "BLANK", "BLANK", "BLANK"]],
	["Cage Transport", ["FILL_IN", "FILL_IN", "FILL_IN", "FILL_IN", "FILL_IN", "FILL_IN", "FILL_IN"]],
	["Stage Set Up", ["BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK"]],
	["Stage Set Up", ["BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK"]],
	["Registration Set Up", ["BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK"]],
	["Registration Check In", ["BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK"]],
	["Registration Check In", ["BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK"]],
	["Registration Usher", ["BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK"]],
	["Late Registration Check In", ["BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK"]],
	["Tech Oversight/Set Up", ["BLANK", "FILL_IN", "FILL_IN", "FILL_IN", "FILL_IN", "FILL_IN", "FILL_IN"]],
	["Photographer", ["BLANK", "BLANK", "FILL_IN", "FILL_IN", "FILL_IN", "FILL_IN", "FILL_IN"]],
	["Social Media", ["BLANK", "BLANK", "BLANK", "FILL_IN", "FILL_IN", "FILL_IN", "FILL_IN"]],
	["Utility", ["BLANK", "BLANK", "FILL_IN", "FILL_IN", "FILL_IN", "FILL_IN", "FILL_IN"]],
	["Cage Oversight", ["BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "FILL_IN"]],
	["Cage Transport", ["BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK"]],
	["Cage Transport", ["BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK", "BLANK"]]
]

"""Transforms single speaker schedule back to default format."""
def multiple_inverse(schedule):
	col_1 = [row[1][1] for row in schedule]
	schedule[0][1][1] = "BLANK"
	schedule[1][1][1] = "BLANK"
	schedule[2][1][1] = "BLANK"
	schedule[3][1][1] = col_1[0]
	schedule[4][1][1] = col_1[1]
	schedule[5][1][1] = col_1[2]
	col_2 = [row[1][2] for row in schedule]
	schedule[0][1][2] = "BLANK"
	schedule[1][1][2] = "BLANK"
	schedule[2][1][2] = "BLANK"
	schedule[6][1][2] = col_2[0]
	schedule[7][1][2] = col_2[1]
	schedule[8][1][2] = col_2[2]
	col_3 = [row[1][3] for row in schedule]
	schedule[2][1][3] = "BLANK"
	schedule[9][1][3] = col_3[2]
	col_4 = [row[1][4] for row in schedule]
	schedule[2][1][4] = "BLANK"
	schedule[9][1][4] = col_4[2]
	col_5 = [row[1][5] for row in schedule]
	schedule[2][1][5] = "BLANK"
	schedule[9][1][5] = col_5[2]
	col_6 = [row[1][6] for row in schedule]
	schedule[2][1][6] = "BLANK"
	schedule[12][1][6] = "BLANK"
	schedule[15][1][6] = col_6[2]
	schedule[16][1][6] = col_6[12]
	return schedule


