# auto-elf

## Overview

This program is meant to automate the scheduling of members of the Berkeley Forum to event shifts. It was developed with Python 3.5.2 and its functionalities include generating event logistics forms (ELFs), listing availabilities for a given shift, and displaying availability information for individual members.

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

Note that Cage Oversight and Cage Transport are split between pre-event and post-event transport. The ELF can be found in the `ELFs/[Name of Event]` folder in CSV format, in addition to a CSV file that contains the names, positions, shift times, and emails for all members assigned to the given ELF. If opening the ELF CSV file in Microsoft Excel, it is recommended that the formatting for the ELF file is:

* Set all column widths to size 16
* Conditionally format all cells that contain the text "NONE_AVAILABLE" to "Light Red Fill with Dark Red Text"
* Conditionally format all cells that contain the text "BLANK" to "Custom Format... -> Fill -> Black"

### Find availabilities for a shift slot

This option lists all members who are available for a given day and time. Note that the range of 30 minute shifts that the auto-elf program supports is from **9:00 AM** to **9:00 PM** for every day of the week.

### List information for an individual

This option prints a user's name, email, and time availabilities for every day of the week.

### Exit

This option ends the program with exit code zero. If none of the above options is chosen and the conditional completes to the else clause, the program will end with exit code one.

## Authorship

This program was developed by Soham Kudtarkar for the Berkeley Forum.
