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
valid_genders = ["Male", "Female", "Prefer not to say"]
valid_genres = ["hiphop", "pop", "edm", "rock", "metal"]

def get_personal_info():
    """
    First asks the user which genre they would like to use.
    Then adds inputted name, age and gender values to 
    relevant genre worksheet.
    """
    print("Please choose one of the following genre options:")

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
    print("Choose Male, Female or Prefer not to say.")

    validate_gender()
    user_info.append(gender)
    print(user_info)

    get_musician_data()
    update_genre_worksheet()

    

def get_musician_data():
    """
    Asks the user their favourite artist or band and song in their 
    specified genre and forks the answer over to genre worksheet.
    """
    while True:
        print(f"The genre you have chosen is {genre}")
        valid_letters = ["Y", "N"]
        double_check_genre = input("Is this correct? Y for yes or N for No").upper()
        if double_check_genre not in valid_letters:
            print("That value cannot be accepted. Please choose Y or N")
            continue
        else:
            break


def validate_genre():
    """
    Gives the user a choice from five genres to provide 
    data for and then validates the input only allowing 
    the strict choices but allowing only lowercase.
    """
    while True:
        global genre
        genre = input("Choose Hiphop, Pop, Edm, Rock or Metal.\n").lower()
        if genre not in valid_genres:
            print("That value was invalid. Please type one of the options")
            continue
        else:
            break

def update_genre_worksheet():
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
            fname = input("Enter your first name here:\n")
            lname = input("Enter your last name here:\n")
            space = ' '
            name = fname + space + lname
            if not fname.isalpha() or not lname.isalpha():
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


def main():
    get_personal_info()
    get_musician_data()
print("Hello there!\n")
print("Welcome to our survey created by and for SuperMic Productions.\n")
print("You will be asked to choose a genre you want to give information for.\n")
print("""Keep in mind that you can only choose one, so if you'd like to do 
an additional genre, you will have to do the survey again.\n""")
print("Please be honest and input artists that belong in your chosen genre.\n")

main()