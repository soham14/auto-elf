# auto-elf

This program is meant to automate the scheduling of members of the Berkeley Forum to event shifts by aggregating member schedules and using sampling to determine optimal shift assignments. The auto-elf program was developed with Python and its functionalities include generating event logistics forms (ELFs), listing availabilities for a given shift, and displaying availability information for individual members. For example outputs, please see `ELFs/Claude Shannon at the Berkeley Forum/` and `ELFs/John McCarthy at the Berkeley Forum/`.

## Set Up

This program was developed using Python 3.5.2. The intialization command is `python auto_elf.py`. The initial view lists the menu options. Member schedules are CSV files that should be put into the `schedules` folder. The range of 30 minute shifts that the auto-elf program supports is from **9:00 AM** to **9:00 PM** for every day of the week. ELFs that are generated can be found in the `ELFs/[Name of Event]` folder.

## Options

### Generate an event logistics form

This option takes into account all schedules in the `schedules` folder, except for those excluded by the user, to create an ELF whose time range is from 1 hour and 30 minutes before the event start time to 2 hours after the event start time, making seven 30 minute shift intervals for the columns of the ELF. The rows are the logisitical positions that include:

* Cage Oversight (x2)
* Cage Transport (x4)
* Stage Set Up (x2)
* Registration Set Up
* Registration Check In (x2)
* Registration Usher
* Tech Oversight/Set Up
* Photographer
* Social Media
* Utility

Note that Cage Oversight and Cage Transport are split between pre-event and post-event transport. The ELF can be found at `ELFs/[Name of Event]/ELF.csv`. The same folder contains a file titled `table.csv` that records the names, positions, shift times, and emails for all members assigned to the given ELF. Finally, the folder also contains a file titled `query.csv` that records information about the query that generated the ELF. If opening `ELF.csv` file in Microsoft Excel, the recommended formatting for the file is:

* Set all column widths to size 16.
* Conditionally format all cells that contain the text "BLANK" to "Custom Format... -> Fill -> Black."
* Conditionally format all cells that contain the text "NONE_AVAILABLE" to "Light Red Fill with Dark Red Text."

The program also asks for a sample size in order to find the optimal schedule. The recommended sample size is 10000 schedules. Cursory statistics will be output by the program, including the mean, median, maximum, minimum, standard deviation, and variance where appropriate. The program selects the schedule that matches the median number of members if the entire sample space is not excluded due to all generated sample schedules containing shifts that are not occupiable due to the other shifts being assigned by the program or other factors. If it is not possible to generate a schedule without unoccupiable shifts, the schedule with the fewest unoccupiable shifts will be chosen.

### Find availabilities for a shift slot

This option lists all members who are available for a given day and time. Note that the range of 30 minute shifts that the auto-elf program supports is from **9:00 AM** to **9:00 PM** for every day of the week.

### List information for an individual

This option prints a user's name, email, and time availabilities for every day of the week.

### Invite members on Google Calendar

Creates invite slots on members' respective Google calendars for their shifts. The event contains information on shift start time, shift end time, assigned position, the venue, and the room number. Every event also has a 15 minute reminder feature. The requirements to run this option are as follows:

* The user needs to have a Google developer account with the Calendar API enabled.
* The user needs to enter their client ID and client secret into the first two variables of the calendar.py file.
* The user needs to install the correct client library using `pip install --upgrade google-api-python-client`.

More information can be found [here](https://developers.google.com/google-apps/calendar/quickstart/python).

### Exit

This option ends the program with exit code zero. If none of the above options is chosen and the conditional completes to the else clause, the program will end with exit code one.

## Authorship

This program was developed by Soham Kudtarkar for the Berkeley Forum.
