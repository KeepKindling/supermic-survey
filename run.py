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

hip_hop_worksheet = SHEET.worksheet('hip-hop')
pop_worksheet = SHEET.worksheet('pop')
edm_worksheet = SHEET.worksheet('edm')
rock_worksheet = SHEET.worksheet('rock')
metal_worksheet = SHEET.worksheet('metal')

user_info = []
valid_genders = ["M", "F", "N"]
def get_info():
    """
    First asks the user which genre they would like to use.
    Then adds inputted name, age and gender values to relevant genre worksheet.
    """
    print("Please choose one of the following genre options")

    genre global
    genre = input("Choose Hip-hop, Pop, Edm, Rock or Metal:\n")


    print()
    print("Please enter your full name.")
    print("Name must only include letters. No numbers or symbols.\n")

    validate_name()
    user_info.append(name)
    print(user_info)

    print()
    print("Please enter your age.")
    print("Age must consist of numbers only. No letters or symbols.")

    validate_age()
    user_info.append(age)
    print(user_info)

    print()
    print("Please enter your gender identity.")
    print("Choose M for Male, F for Female or N for Not applicable")

    validate_gender()
    user_info.append(gender)
    print(user_info)


def validate_name():
    """
    Asks user to input name and runs an infinite loop
    if they use invalid characters until they use letters only.
    """
    while True:
        try:
            global name
            name = input("Enter your name here: \n")
            if not name.isalpha():
                raise ValueError(
                    f"You can only use letters for your name. You entered {name}."
                )
        except ValueError:
            print("That value was invalid. Please try again.")
            continue
        else:
            break


def validate_age():
    """
    Takes an input from the user, checks that it is an 
    integer and converts it into a int because it is a number
    inside of a string
    """
    while True:
        try:
            global age
            age = input("Enter your age here:\n")
            if (int(age)==age):
                raise ValueError(
                    f"You can only use letters for your name. You entered {name}."
                )
        except ValueError:
            print("That value was invalid. Please use whole numbers.")
            continue
        else:
            break


def validate_gender():
    """
    Asks the user what there gender is, checks that the 
    value is strictly one of the three options and will pass 
    it into relevant genre worksheet
    """
    while True:
        global gender
        gender = input("Enter your gender here:\n").capitalize()
        if gender not in valid_genders:
            print("That value was invalid. Please choose one of the options.")
            continue
        else:
            break
                

print("Hello there!")
print("Welcome to our survey created by and for SuperMic Productions.\n")
print("You will be asked to choose genre options you want to give information for.")
print("You can choose one, or all of the genres if you'd like!\n")
print("Please be honest and input artists that belong in your chosen genres.\n")

get_info()