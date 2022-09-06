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

hiphop_worksheet = SHEET.worksheet('hiphop')
pop_worksheet = SHEET.worksheet('pop')
edm_worksheet = SHEET.worksheet('edm')
rock_worksheet = SHEET.worksheet('rock')
metal_worksheet = SHEET.worksheet('metal')

user_info = []
valid_genders = ["M", "F", "N"]
valid_genres = ["hiphop", "pop", "edm", "rock", "metal"]

def get_info():
    """
    First asks the user which genre they would like to use.
    Then adds inputted name, age and gender values to relevant genre worksheet.
    """
    print("Please choose one of the following genre options")

    validate_genre()
    print(f"You have chosen {genre}")

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

    find_genre_worksheet()


def validate_genre():
    """
    Gives the user a choice from five genres to provide 
    data for and then validates the input only allowing 
    the strict choices but allowing only lowercase.
    """
    while True:
        global genre
        genre = input("Choose Hiphop, Pop, Edm, Rock or Metal:\n").lower()
        if genre not in valid_genres:
            print("That value was invalid. Please type one of the five options")
            continue
        else:
            break

def find_genre_worksheet():
    """
    Check which genre the user chose and appends the users personal 
    info to the relevant worksheet.
    """
    if genre == "hiphop":
        print("Accessing hip hop worksheet...")
        hiphop_worksheet.append_row(user_info)
        print("Hip hop worksheet updated successfully!")
    elif genre == "pop":
        print("Accessing pop worksheet...")
        pop_worksheet.append_row(user_info)
        print("Pop worksheet updated successfully!")
    elif genre == "edm":
        print("Accessing edm worksheet...")
        edm_worksheet.append_row(user_info)
        print("Edm worksheet updated successfully!")
    elif genre == "rock":
        print("Accessing rock worksheet...")
        rock_worksheet.append_row(user_info)
        print("Rock worksheet updated successfully!")
    else:
        print("Accessing metal worksheet...")
        metal_worksheet.append_row(user_info)
        print("Metal worksheet updated successfully!")

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