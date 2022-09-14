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
valid_genres = ["Hiphop", "Pop", "Edm", "Rock", "Metal"]
valid_letters = ["Y", "N"]


def get_personal_info():
    """
    Runs other methods in order to collect genre, name,
    age and gender. Thise data is then returned and appended
    to corresponding genre worksheet.
    """
    print()
    print("Please choose one of the following genre options:")
    print("Type Hiphop, Pop, Edm, Rock or Metal\n")

    genre = validate_genre()

    print()
    print("Please enter your full name.")
    print("Name must only include letters. No numbers or symbols.\n")

    name = validate_name()
    user_info.append(name)

    print()
    print("Please enter your age.")
    print("Age must consist of numbers only. No letters or symbols.")

    age = validate_age()
    user_info.append(age)

    print()
    print("Please enter your gender identity.")
    print("Choose Male, Female or Prefer not to say.")

    gender = validate_gender()
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
    artist = input("Type your favourite artist or band here:\n").capitalize().strip()
    user_info.append(artist)

    print()
    song = input(f"Enter your favourite song by {artist} here:\n").capitalize().strip()
    user_info.append(song)


def check_user_genre():
    """
    Asks the user to verify they picked the correct genre. If yes, the program
    continues. If no, they can go back and choose the genre they want to use.
    """
    while True:
        double_check_genre = input("Is this right? Y yes or N No\n").upper().strip()
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
    while True:
        genre = input("Choose Hiphop, Pop, Edm, Rock or Metal.\n").capitalize().strip()
        if genre not in valid_genres:
            print("That value was invalid. Please type one of the options")
            continue
        else:
            print(f"You chose {genre}")
            return genre

    check_user_genre()


def update_genre_worksheet(user_info):
    """
    Uses returned genre to access corresponding worksheet and updates
    it with user_info data by appending it to a row.
    """
    if genre == "Hiphop":
        worksheet = hiphop_worksheet
    elif genre == "Pop":
        worksheet = pop_worksheet
    elif genre == "Edm":
        worksheet = edm_worksheet
    elif genre == "Rock":
        worksheet = rock_worksheet
    else:
        worksheet = metal_worksheet

    print(f"Accessing {genre.capitalize()} worksheet...\n")
    worksheet.append_row(user_info)
    print(f"{genre.capitalize()} worksheet updated successfully!\n")


def validate_name():
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


def validate_age():
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


def validate_gender():
    """
    Allows the user to choose one of three options and the appends
    that data to a variable to update genre worksheet later.
    """
    while True:
        gender = input("Enter your gender here:\n").capitalize().strip()
        if gender not in valid_genders:
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
                             "N for no\n").capitalize().strip()

        if answer_again not in valid_letters:
            print("""Sorry but that value was unacceptable. Please type Y
            for yes or N for no""")
            continue
        elif answer_again == "Y":
            print()
            print("You have chosen to complete this survey again and we " +
                  "thankyou for your input. Users may only add info " +
                  "once per genre. You will no longer be to use any genres " +
                  "you have already answered for.")
            get_personal_info()
        else:
            print("Thankyou again for participating in our survey. SuperMic " +
                  "Productions is very greatful. Have a great day and we " +
                  "hope to see you again in our future survey's!\n")
            print("Goodbye.")
            break


def duplicate_info_check():
    """
    Checks that name, age and gender are not all in a worksheet already.
    Prevents users from adding information to the same genre more than once.
    """


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
survey and choose other genres but you will not be able to do the same genre
more than once.\n""")

if __name__ == "__main__":
    main()
