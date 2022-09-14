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

HIPHOP_WORKSHEET = SHEET.worksheet('hiphop')
POP_WORKSHEET = SHEET.worksheet('pop')
EDM_WORKSHEET = SHEET.worksheet('edm')
ROCK_WORKSHEET = SHEET.worksheet('rock')
METAL_WORKSHEET = SHEET.worksheet('metal')

user_info = []
VALID_GENDERS = ["Male", "Female", "Prefer not to say"]
VALID_GENRES = ["Hiphop", "Pop", "Edm", "Rock", "Metal"]
VALID_LETTERS = ["Y", "N"]


def get_personal_info():
    """
    Runs other methods in order to collect genre, name,
    age and gender. Thise data is then returned and appended
    to corresponding genre worksheet.
    """
    print()
    print("Please choose one of the following genre options:\n")

    get_genre()

    print()
    print("Please enter your full name.")
    print("Name must only include letters. No numbers or symbols.\n")

    name = get_name()
    user_info.append(name)

    print()
    print("Please enter your age.")
    print("Age must consist of numbers only. No letters or symbols.")

    age = get_age()
    user_info.append(age)

    print()
    print("Please enter your gender identity.")
    print("Choose Male, Female or Prefer not to say.")

    gender = get_gender()
    user_info.append(gender)

    get_musician_data()

    print()
    print("Thankyou for your honest input. We are working to update")
    print("our spreadsheet with the data you have provided for us.\n")
    print("Please wait a moment...\n")
    update_genre_worksheet(user_info)


def get_musician_data():
    """
    Asks the user to provide their favourite artist and song for
    previously specified genre. returns this data and appends to a
    variable which is the passed to genre worksheet.
    """
    print()
    print("Thank you for providing your personal details for our survey.")
    print("You will now be asked to input your favourite artists and songs.\n")
    artist = input("Type your favourite " +
                   "artist or band here:\n").capitalize().strip()

    user_info.append(artist)

    print()
    song = input("Enter your favourite song " +
                 "here:\n").capitalize().strip()

    user_info.append(song)


def check_user_genre():
    """
    Asks the user to verify they picked the correct genre. If yes, the program
    continues. If no, they can go back and choose the genre they want to use.
    """
    while True:
        double_check_genre = input("Is this right? " +
                                   "Y yes or N No\n").upper().strip()
        if double_check_genre not in VALID_LETTERS:
            print("That value cannot be accepted. Please choose Y or N")
            continue
        elif double_check_genre == VALID_LETTERS[1]:
            get_personal_info()
        else:
            break


def get_genre():
    """
    Gives the user a choice from five genres to provide data for and then
    validates the input only allowing the strict choices but allowing only
    lowercase. Returns genre for later use as to which worksheet to update.
    """
    global genre
    while True:
        genre = input("Choose Hiphop, Pop, Edm, " +
                      "Rock or Metal.\n").capitalize().strip()
        if genre not in VALID_GENRES:
            print("That value was invalid. Please type one of the options")
            continue
        else:
            print(f"You chose {genre}")
            break

    check_user_genre()


def update_genre_worksheet(user_info):
    """
    Uses returned genre to access corresponding worksheet and updates
    it with user_info data by appending it to a row.
    """
    if genre == "Hiphop":
        worksheet = HIPHOP_WORKSHEET
    elif genre == "Pop":
        worksheet = POP_WORKSHEET
    elif genre == "Edm":
        worksheet = EDM_WORKSHEET
    elif genre == "Rock":
        worksheet = ROCK_WORKSHEET
    else:
        worksheet = METAL_WORKSHEET

    print(f"Accessing {genre.capitalize()} worksheet...\n")
    worksheet.append_row(user_info)
    print(f"{genre.capitalize()} worksheet updated successfully!\n")


def get_name():
    """
    Gets the user to input their first and last name seperately.
    This is then appended to a variable for later use.
    """
    while True:
        fname = input("Enter your first name here:\n").capitalize().strip()
        lname = input("Enter your last name here:\n").capitalize().strip()
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
            return name


def get_age():
    """
    Asks the user for their age and returns the value which is then
    later appended to a variable for updating worksheets afterwards.
    """
    while True:
        age_input = input("Enter your age here:\n").strip()
        if not age_input.isnumeric():
            print("That value was invalid. Please try again")
            print("Age must be a numeric value. No letters or symbols.")

        age = int(age_input)
        if age > 80 or age < 16:
            print("Error, age must be between 16 - 80.")
            print(f"You entered {age}. Please try again.\n")
            continue
        else:
            return age


def get_gender():
    """
    Allows the user to choose one of three options and the appends
    that data to a variable to update genre worksheet later.
    """
    while True:
        gender = input("Enter your gender here:\n").capitalize().strip()
        if gender not in VALID_GENDERS:
            print("That value was invalid. Please choose one of the options.")
            continue
        else:
            return gender


def restart_survey():
    """
    Asks the user to do the survey again. If yes, runs the program again.
    If no, the program closes and thanks the user for participating.
    """
    print("Thankyou for completing this survey by SuperMic Productions.\n")
    while True:
        answer_again = input("Would you like to do the survey again but for " +
                             "a different genre? Type Y for yes or " +
                             "N for no.\n").capitalize().strip()

        if answer_again not in VALID_LETTERS:
            print("""Sorry but that value was unacceptable. Please type Y
            for yes or N for no""")
            continue
        elif answer_again == "Y":
            print()
            print("You have chosen to complete this survey again and we " +
                  "thankyou for your continued input.")
            get_personal_info()
        else:
            print("Thankyou again for participating in our survey. SuperMic " +
                  "Productions is very greatful. Have a great day and we " +
                  "hope to see you again in our future survey's!\n")
            print("Goodbye.")
            break


def main():
    """
    The main method that incorporate all other methods.
    """
    get_personal_info()
    restart_survey()


print("Hello there!\n")
print("Welcome to our survey created by and for SuperMic Productions.\n")
print("""You will be asked to choose a genre you want to give information
for based on your likes. By helping us collect data with this survey, you
are contributing to keeping your favourite artists in the mix so you can
listen to them as much as you'd like. We appreciate your cooperation!\n""")
print("""For this survey to do what it's supposed to and collect real data,
keep in mind that honesty is paramount and we trust that you and other users
will follow this practice. After all, we just want to represent your
favourite artists and bands.\n""")
print("""With that being said try to name artists that belong in your chosen
genre. That way we have honest data that we can rely on. If you would like
to enter information for more than one genre, you will have to repeat the
survey and choose the genre you want to do.\n""")

if __name__ == "__main__":
    main()
