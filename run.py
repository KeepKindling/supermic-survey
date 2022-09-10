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
valid_genres = {"1": "hiphop", "2": "pop", "3": "edm", "4": "rock", "5": "metal"}

if __name__ == "__name__":
    main()

def get_personal_info():
    """
    Runs other methods in order to collect genre, name, 
    age and gender. Thise data is then returned and appended 
    to corresponding genre worksheet.
    """
    print()
    print("Please choose one of the following genre options:")
    print("Type 1. Hiphop, 2. Pop, 3. Edm, 4. Rock or 5. Metal\n")

    validate_genre()
    print(f"You chose {genre}")

    check_user_genre()

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
    Asks the user to provide their favourite artist and song for 
    previously specified genre. returns this data and appends to a 
    variable which is the passed to genre worksheet.
    """
    print("Thank you for providing your personal details for our survey.")
    print("You will now be asked to input your favourite artists and songs.\n")
    artist = input("Type your favourite artist or band here:\n").capitalize()
    user_info.append(artist)

    print(f"Below here, please enter your favourite song by {artist}")
    print("Remember that being honest is all we ask during this survey\n")
    song = input(f"Enter your favourite song by {artist} here:\n").capitalize()
    user_info.append(song)


def check_user_genre():
    """
    Asks the user to verify they picked the correct genre. If yes, the program 
    continues. If no, they can go back and choose the genre they want to use.
    """
    while True:
        valid_letters = ["Y", "N"]
        double_check_genre = input("Is this correct? Y for yes or N for No\n").upper()
        if double_check_genre not in valid_letters:
            print("That value cannot be accepted. Please choose Y or N")
            continue
        elif double_check_genre == valid_letters[1]:
            get_personal_info()
        else:
            break


def validate_genre():
    """
    Gives the user a choice from five genres to provide data for and then 
    validates the input only allowing the strict choices but allowing only 
    lowercase. Returns genre for later use as to which worksheet to update.
    """
    global genre
    while True:
        genre = input("Choose 1, 2, 3, 4 or 5.\n")
        if genre not in valid_genres:
            print("That value was invalid. Please type one of the options")
            continue
        else:
            break
        

def update_genre_worksheet():
    """
    Uses returned genre to access corresponding worksheet and updates 
    it with user_info data.
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
    Gets the user to input their first and last name seperately.
    This is then appended to a variable for later use.
    """
    global name
    while True:
        fname = input("Enter your first name here:\n").capitalize()
        lname = input("Enter your last name here:\n").capitalize()
        space = ' '
        name = fname + space + lname
        if not fname.isalpha() or not lname.isalpha():
            print("That value was invalid. Please try again.")
            continue
        elif len(fname) > 15 or len(lname) > 15:
            print("Error, first or last name cannot exceed 15 letters.")
            print("Please try again.\n")
            continue
        else:
            break


def validate_age():
    """
    Asks the user for their age and returns the value which is then 
    later appended to a variable for updating worksheets afterwards.
    """
    global age
    while True:
            age = input("Enter your age here:\n")
            if age.isalpha():
                print("That value was invalid. Please try again")
                print("Age must be a numeric value. No letters or symbols.")
            elif age == float(age):
                print("That value was invalid. Please try again.")
                print(f"Your age must be a whole number. you entere {age}.")
                continue
            elif int(age) > 80 or int(age) < 16:
                print("Error, age must be between 16 - 80.")
                print(f"You entered {age}. Please try again.\n")
                continue
            elif (int(age)==age):
                print("That value was invalid. Please use whole numbers.")
                continue
            else:
                break


def validate_gender():
    """
    Allows the user to choose one of three options and the appends 
    that data to a variable to update genre worksheet later on.
    """
    global gender
    while True:
        gender = input("Enter your gender here:\n").capitalize()
        if gender not in valid_genders:
            print("That value was invalid. Please choose one of the options.")
            continue
        else:
            break


def main():
    get_personal_info()

print("Hello there!\n")
print("Welcome to our survey created by and for SuperMic Productions.\n")
print("You will be asked to choose a genre you want to give information for.\n")
print("""Keep in mind that you can only choose one, so if you'd like to do 
an additional genre, you will have to do the survey again.\n""")
print("Please be honest and input artists that belong in your chosen genre.\n")

main()
