import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('popular_music_survey')

hip_hop = SHEET.worksheet('hip-hop')



print("Hello there!")
print("Welcome to our survey created by and for SuperMic Productions.")
print("You will be asked to choose genre options you want to give infoormation for.")
print("You can choose one, or all of the genres if you'd like!")
print("Please be honest and input artists that belong in your chosen genres.")