# SuperMic Productions Survey

## About

This a survey conducted by a made-up company called SuperMic Productions. Since there has been much growth over the past 10 years for number of artists, bands and musicians, the company cannot represent or publish everyones songs. Due to this increase in musical potential, the company needs a survey that will collect information from users. The survey will also allow users to request data from genre worksheets so they can see various information such as "Which genders prefer metal music" and so on.

## User experience reserch and design

### Strategy

SuperMic Productions is in need of a survey that will efficiently collect data from users to see which artist and bands are the most popular. This information will prove paramount when deciding which artists to represent.

The application should be able to successfully collect and process data into easily understandable and readable data. As to not have duplicate data, it will not allow a user to enter data for a genre if they have already done so. This is to keep results as true as possible otherwise, the company could make incorrect decisions based on false data. 

The benefits of creating a user friendly survey that is very accessable online are as follows:
- Program will not accept ridiculous answers sich as curse words or obviously wrong inputs like age as 1000 or 4
- It will allow users to add info for each genre if they wish because users can have favourites from different genres
- As it is an online survey, users need not worry about writing down their answers on paper and sending off the information
- users personal information is protected and will not be shared to third party companys

#### Leading User Stories

As a user:

- I want to be able to input my favourite artists and songs into the survey so I will be more likely to hear music from them in the future.
- I want to be able to choose whether I want to share my gender identity.
- I want to be able to share information for as many genres that are available.
- I want my personal information (Name, Age, Gender) to be protected amd not shared to third party companys for advertisement.
- I want to be able to request specific data from the survey so I can see what other people are listening to as to explore music further.

As the owner:

- I want to provide a survey that is quickly completed as to not take up lots of users time.
- I want to collect data from users so I can make better decisions for who I should represent proffesionally in the music industry.
- I want users to trust this survey will not share personal information with third party companys so they are more likely to participate in future surveys.
- I want to be able to allow users to glean over other users data as to find recommendations for themselves.

#### Strategy goals for the website

- The application will be provide an easily accessable survey to efficiently collect information from users.
- The questions in the survey will be easy to follow and only able to accept valid data
- Users who enjoyed this survey and found it wuick and easy to complete will participate in other future surveys or questionaires we create.

### Features

#### Features Currently Used

- A welcome message

![Welcome-Message](/images/greeting_message.png)

- Double check correct genre choice as to prevent accidental input from user

![Genre-Check](/images/genre_validation_check.png)

- Collects name and age and gender identity

![Personal-Info](/images/name_age_gender_validation.png)

- Collects users artist and song choice

![Survey-Question-Data](/images/artist_song_input.png)

- Allows user to complete survey again for another genre

![Survey-End](/images/end_survey.png)

- Pass information to survey spreadsheet

![Survey-spreadsheet-data](/images/data_collection.png)

#### Non-Existant Features (Future Surveys)

- Develop program to be phone and tablet friendly
- Request users email to be sent future surveys
- Allow users to create valid genres to add to spreadsheet
- Ask the user for the address which would not be shared with anyone

### Structure

The site will follow these strcutural guidelines:

1. The user will be greeted and guided to how to answer the survey's questions
2. They will then be asked to choose a genre they would like to provide information for
3. If they have already used a genre, they will be told they cannot use a genre more than once
4. Then will be asked to provide there first and last name, age and gender identity(an option is available to prefer not to say)
5. Then be thanked for their personal info and assure the user it will remain protected from third party companys
6. Asked to give their favorite artist and the artists song in their specified genre
7. Notify the user that the worksheet of data is being updated and has done successfully
8. User is finally asked if they want to provide information for another genre. If yes the program runs again, if no, The user is thanked again and the program bids goodbye

### Flowchart

A flowchart providing an easy step by step view of how the program will primarily run:

![Flowchart](/images/supermic_survey_flowchart.jpeg)





# Bugs/Issues encountered 
- Whilst trying to validate the name variable inside of the get_info method, kept getting the error message "name is not defined". I think it's related to the scope of where I'm defining name. Tried using the global attribute in front of the name variable but did not fix it, currently stuck. ! Fixed the issue by using the global attribute correctly. I placed it in front of the name variable but i needed to give the variable global scope before defining it. not at the same time.
- Attempting to validate the value of name to check it is only using alphabetical letters. if name != str():. This did not work so tried to use isalpha() but prints error message regardless of which characters are used when inputting name value. Also tried using a for loop that would iterate through each character of the value of name and use isalpha() to check for letters but did not work either. ! Fixed by removing the try statement and using a while True statement to check the entire value at once inside of name. Credit to sean at code institute tutor session for help with this solve.
- caused issue where the code would not print ValueError message within validate_name method. I decided to add the question for name into validate_name method and use while True, try: statement. ValueError wasnt showing up when i tested with an incorrect value so I tried removing it entirely which cause an infinite loop to occur. So decided to leave ValueError in the except argument and an if statement and just print a string to the user telling them their value was invalid. CURRENTLY UNFIXED
- I created a method called update genre worksheet that would check the genre the user chose and pass all their info into the corresponding worksheet but during testing was met with a massive error that was inconcievable to me. After a short discussion, I realized that inside of the find_genre_worksheet if statement, I put the genre variable inside of the append_row() method when I needed to put in user_info as that variable holds all the users inputs.
- While looking at my validate_name() method, I realized that it only accepted a first name as a space would cause isalpha() to be false. I created 2 variables called fname and lname. name = fname + ' ' + lname didnt work and printed my error message. So i tried inserting the fname and lname variables into my if statement and used or so if one of them used something other than a letter, it would print the error message. Then a created one more variable called space and gave it an empty string and placed it between fname and lname in the name variable. Looking like this name = fname + space + lname. This worked without issue.
- Inside the validate_age method, I wanted to restrict the users age to between 16 and 80 so the user cannot enter false data that is absurd such as 1000 or 2. I tried if age > 80 or age < 16: but an error showed up which stated "not supported between instances of str and int". This was because the value of age was a string. So inside of the if statement, i used int(age) to convert the value to an integer so the condition would work, which it did.
- The validate_age method would bring an error and end the program if the user entered a decimal number or "float". I tried adding ->   and age.float() to the if statement that restricts input number size but didnt work because i entered float as an attribute of age which was wrong. solved by using elif float(age). This means if the age value can be converted to float, then do this code. I also had to place this above the elif (int(age)==age) statement as it would pass ValueError invalid literal for int() with base10: 'value'. But if the user enters something like 2.d2, It states that it could not convert the string to float and the closes the program. Unsure how to fix this yet.
- validate_age after fixing the previous issue, would then print my error message "Must be a whole number" when I typed 22. This was because I converted age to a float. I fixed this immediately by making it ->   elif age == float(age). solved without further issue.
- Replaced my list of accepted genres with a dict with the format of 1: hiphop, 2: pop etc. but everytime I ran the program, it would update the metal worksheet regardless of genre chosen by the user.



# Issues unsolved

- If the user enters a value like 2.d2, The program brings up an error as it cant be converted to float so they if statement cannot be run.
- When replacing list of valid genres with dict of valid genres, causes program to always update metal worksheet regardless of user input.
