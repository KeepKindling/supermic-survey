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

### Bugs and Issues Encountered

1. Whilst trying to validate the name variable inside of the get_info method, I kept getting an error message "name is not defined". 
- I reserched for a solution and came across the global attribute. I added it in front of name and then defined name below which worked great

2. I was attempting to check that the value of name, only included alphabetical letters by using the following code (if name != str():). 
- This did not work so I added a while true statement to check the whole value at once, then used the .isalpha() method at the end of fname and lname variables in the if statement.

3. While trying to implement a try statement to print a ValueError message to the user, Typing an incorrect value would not cause an error message to pop up.
- Chose to just print an error message to the user using an if: elif: else: statement.

4. I created a method that would check the genre the user chose and pass all of their information into the corresponding worksheet. But during testing, I was met with a massive incomprehensable error. I logged a tutor session with code institute and whilst typing the issue I was having I realized where I went wrong before the tutor could offer assistance.
- I saw that inside the if statement of the update_genre_worksheet() method, I placed the genre variable inside of the append_row() method when I actually needed to place it in the user_info variable because that is where the users inputs are stored.

5. My validate_name() method would only accept a firstname as the isalpha() method would throw an error if the user used a space to seperate first and last names. 
- I created three variables. 'fname' to hold the users first name, 'space' to literally have a single space in it and 'lname' to contain a users last name. I then wrote   name = fname + space + lname. This solved my problem.

6. When testing the validate_age() method, I realized that a user could input a ridiculous number as an age. I tried using:  if age > 80 or age < 16: but that produced an error stating "not supported between instances of str and int". This was because the value of age was a string.
- Inside the if statement, I used int(age) to convert the value to an integer so the condition would work, which it did.

7. During another test, the program would print an error and edn the program if a deciaml (float) number was entered for the age variable. I tried adding  and age.float() to the if statement where the age cannot exceed 80 or be below 16.
- I solved the problem by adding  elif float(age). So the program will print an error message to the user and they will be forced to try again.

8. This bug occured immediatelt after solving issue no. 7. I would be given an error message during testing stating "Must be a whole number" which was because I converted age into a float. 
- The solution was simple. I changed it to  elif age == float(age). Solved without any other issues.


# Issues unsolved

- If the user enters a value like 2.d2, The program brings up an error as it cant be converted to float so they if statement cannot be run.
- When replacing list of valid genres with dict of valid genres, causes program to always update metal worksheet regardless of user input.

### Credits
Sean at code institute for a mentoring session to solve an issue