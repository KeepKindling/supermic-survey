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
pop = SHEET.worksheet('pop')
edm = SHEET.worksheet('edm')
rock = SHEET.worksheet('rock')
metal = SHEET.worksheet('metal')

user_info = []

def get_info():
    print()
    print("Please enter your full name.")
    print("Name must only include letters. No numbers or symbols.\n")

    name = input("Enter your name here:\n")

    user_info.append(name)

    print()
    print("Please enter your age.")
    print("Age must consist of numbers only. No letters or symbols.")

    age = input("Enter your age here:\n")

    user_info.append(age)
    
    print()
    print("Please enter your gender identity.")
    print("Please choose between Male, Female and Prefer not to say.")

    gender = input("Enter your gender here:\n")

    user_info.append(gender)

    return user_info

print("Hello there!")
print("Welcome to our survey created by and for SuperMic Productions.\n")
print("You will be asked to choose genre options you want to give information for.")
print("You can choose one, or all of the genres if you'd like!\n")
print("Please be honest and input artists that belong in your chosen genres.\n")

get_info()