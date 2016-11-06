"""
The majority of the code written below relating to the Google Calendar API comes from Google
Calendar API guides. The guides can be found here: https://developers.google.com/google-apps/calendar/overview.
Much of the non-original code was used from this sample from Google as well:
https://developers.google.com/api-client-library/python/samples/authorized_api_cmd_line_calendar.py.
The code from the samples are licensed under the Apache 2.0 License.
"""

import httplib2
import sys
import csv
import path

from apiclient.discovery import build
from oauth2client import tools
from oauth2client.file import Storage
from oauth2client.client import AccessTokenRefreshError
from oauth2client.client import OAuth2WebServerFlow
from os import path
from datetime import datetime

client_id = "NOT_INITIALIZED"
client_secret = "NOT_INITIALIZED"

scope = 'https://www.googleapis.com/auth/calendar'

flow = OAuth2WebServerFlow(client_id, client_secret, scope)

def invite():

  if client_id == "NOT_INITIALIZED" or client_secret == "NOT_INITIALIZED":
    print("\nPlease enter a client ID and client secret before using this option. " + \
          "More information on this can be found in the README file.\n")
    return

  storage = Storage('credentials.dat')

  credentials = storage.get()

  if credentials is None or credentials.invalid:
    credentials = tools.run_flow(flow, storage, tools.argparser.parse_args())

  http = httplib2.Http()
  http = credentials.authorize(http)

  service = build('calendar', 'v3', http=http)

  creator_name = input("What is your name?\n>>> ")

  while creator_name == "":
    print("\nPlease enter your name.\n")
    creator_name = input("What is your name?\n>>> ")

  creator_email = input("\nWhat is your UC Berkeley email?\n>>> ")

  while creator_email == "":
    print("\nPlease enter your UC Berkeley-assigned email.\n")
    creator_email = input("What is your UC Berkeley email?\n>>> ")

  manager_name = input("\nWhat is the name of the event manager?\n>>> ")

  while manager_name == "":
    print("\nPlease enter the event manager's name.\n")
    manager_name = input("What is the event manager's name?\n>>> ")

  manager_email = input("\nWhat is the event manager's UC Berkeley email?\n>>> ")

  while manager_email == "":
    print("\nPlease enter the event manager's UC Berkeley-assigned email.\n")
    manager_email = input("What is the event manager's UC Berkeley-assigned email?\n>>> ")

  ELF_created = input("\nHas the folder containing the table.csv file for the event already been created? (format: yes/no)\n>>> ")

  while ELF_created.lower() not in ["yes", "no", "y", "n"]:
    print("\nPlease answer with a \"yes\" or \"no.\"\n")
    ELF_created = input("Has the folder containing the table.csv file for the event already been created? (format: yes/no)\n>>> ")

  if ELF_created.lower() in ["no", "n"]:
    print("\nPlease create the file using option 1 of the main menu.\n")
    return

  folder_name = input("\nWhat is the name of the folder that contains the relevant table.csv?\n>>> ")

  while not path.exists("ELFs/" + folder_name + "/table.csv"):
    print("\nThe folder " + folder_name + " could not be found.\n")
    exit_prompt = input("Would you like to return to the main menu? (format: yes/no)\n>>> ")
    if exit_prompt in ["yes", "y"]:
      return
    folder_name = input("\nWhat is the name of the folder that contains the relevant table.csv?\n>>> ")

  date = input("\nWhat is the date of the event? (format: MM-DD-YYYY)\n>>> ")

  while len(date.split("-")) != 3:
    print("\nPlease enter a valid date in the MM-DD-YYYY format.\n")
    date = input("What is the date of the event? (format: MM-DD-YYYY)\n>>> ")

  venue_name = input("\nWhat is the name of the venue? (format: Boalt Hall, Wurster Hall, etc.)\n>>> ")

  while venue_name == "":
    print("\nPlease enter the name of the venue.\n")
    venue_name = input("What is the name of the venue? (format: Boalt Hall, Wurster Hall, etc.)\n>>> ")

  room_number = input("\nWhat is the room number? (format: 100, 350B, etc.)\n>>> ")

  while room_number == "":
    print("\nPlease enter the room number.\n")
    room_number = input("What is the room number? (format: 100, 350B, etc.)\n>>> ")

  print("\nThe requested folder and table.csv file were found. Please review the names, times, and shifts for the request.\n")

  invitations = []

  with open("ELFs/" + folder_name + "/table.csv") as csvfile:
    first = 0
    for row in csvfile:
      if first == 0:
        first = 1
        continue
      row = row.split(",")
      print(" -- " + row[0] + " for " + row[1] + " from " + row[2] + " to " + row[3] + ".")
      invitations.append(row)

  name_check = input("\nAre you sure that you want to invite the members above for the given times and shifts? (format: yes/no)\n>>> ")

  if name_check in ["no", "n"]:
      print("\nYou will be returned to the main menu.\n")
      return

  while name_check not in ["yes", "y"]:
    print("\nPlease answer with a \"yes\" or \"no.\"\n")
    if name_check in ["no", "n"]:
      print("\nYou will be returned to the main menu.\n")
      return
    name_check = input("Are you sure that you want to invite the members above for the given times and shifts? (format: yes/no)\n")

  print("Inviting...\n")

  for invite in invitations:
    time_start = invite[2]
    time_end = invite[3]
    datetime_start = datetime.strptime(date + " " + time_start, "%m-%d-%Y %I:%M %p")
    start_temp = str(datetime_start).split(" ")
    datetime_start = start_temp[0] + "T" + start_temp[1] + "-07:00"
    datetime_end = datetime.strptime(date + " " + time_end, "%m-%d-%Y %I:%M %p")
    end_temp = str(datetime_end).split(" ")
    datetime_end = end_temp[0] + "T" + end_temp[1] + "-07:00"
    
    event = {
      "calendarID": invite[4],
      "location": venue_name + ", Berkeley, CA",
      "summary": "[TBF] " + invite[1] + " -- " + room_number + " " + venue_name,
      "start": {
        "dateTime": str(datetime_start),
        "timeZone": "America/Los_Angeles"
      },
      "end": {
        "dateTime": str(datetime_end),
        "timeZone": "America/Los_Angeles"
      },
      "reminders": {
        "useDefault": False,
        "overrides": [
          {"method": "popup", "minutes": 15}
        ]
      },
      "creator": {
        "displayName": creator_name,
        "email": creator_email
      },
      "organizer": {
        "displayName": manager_name,
        "email": manager_email
      }
    }

    try:

      request = service.events().insert(calendarId=invite[4], body=event)
      if request != None:
        response = request.execute()

    except AccessTokenRefreshError:
      print ('The credentials have been revoked or expired, please re-run'
             'the application to re-authorize')

  print("\nMembers invited successfully.\n")
