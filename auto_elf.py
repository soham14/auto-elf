"""Main user interface."""

import os

os.system("cls" if os.name == "nt" else "clear")

while True:
	print("\nAuto-ELF Version 1.0. Developed by Soham Kudtarkar for the Berkeley Forum.\n")
	print("MENU:\n* 1 -> Generate an event logistics form.\n* 2 -> Find availabilities for a shift slot.\n* 3 -> List information for an individual.\n* 4 -> Exit.\n")

	menu_choice = input("Please enter a number to choose a menu option.\n>>> ")

	while menu_choice not in ["1", "2", "3", "4"]:
		os.system("cls" if os.name == "nt" else "clear")
		print("\nAuto-ELF Version 1.0. Developed by Soham Kudtarkar for the Berkeley Forum.\n")
		print("MENU:\n* 1 -> Generate an event logistics form.\n* 2 -> Find availabilities for a shift slot.\n* 3 -> List information for an individual.\n* 4 -> Exit.\n")
		menu_choice = input("Please enter a number to choose a menu option.\n>>> ")

	if menu_choice == "1":
		os.system("cls" if os.name == "nt" else "clear")
		print("\n* 1 -> Generate an event logistics form.")
		from generator import generate
		generate()
		input("Press enter to go back to the menu\n>>> ")
		os.system("cls" if os.name == "nt" else "clear")
	elif menu_choice == "2":
		os.system("cls" if os.name == "nt" else "clear")
		print("\n* 2 -> Find availabilities for a shift slot.")
		from finder import find
		find()
		input("Press enter to go back to the menu\n>>> ")
		os.system("cls" if os.name == "nt" else "clear")
	elif menu_choice == "3":
		os.system("cls" if os.name == "nt" else "clear")
		print("\n* 3 -> List information for an individual.")
		from information import info
		info()
		input("Press enter to go back to the menu\n>>> ")
		os.system("cls" if os.name == "nt" else "clear")
	elif menu_choice == "4":
		os.system("cls" if os.name == "nt" else "clear")
		exit(0)
	else:
		print("\nExited with an error.\n")
		exit(1)
