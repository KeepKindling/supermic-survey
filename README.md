# Bugs/Issues encountered 
- Whilst trying to validate the name variable inside of the get_info method, kept getting the error message "name is not defined". I think it's related to the scope of where I'm defining name. Tried using the global attribute in front of the name variable but did not fix it, currently stuck. ! Fixed the issue by using the global attribute correctly. I placed it in front of the name variable but i needed to give the variable global scope before defining it. not at the same time.
- Attempting to validate the value of name to check it is only using alphabetical letters. if name != str():. This did not work so tried to use isalpha() but prints error message regardless of which characters are used when inputting name value. Also tried using a for loop that would iterate through each character of the value of name and use isalpha() to check for letters but did not work either. ! Fixed by removing the try statement and using a while True statement to check the entire value at once inside of name. Credit to sean at code institute tutor session for help with this solve.
- caused issue where the code would not print ValueError message within validate_name method. I decided to add the question for name into validate_name method and use while True, try: statement. ValueError wasnt showing up when i tested with an incorrect value so I tried removing it entirely which cause an infinite loop to occur. So decided to leave ValueError in the except argument and an if statement and just print a string to the user telling them their value was invalid. CURRENTLY UNFIXED
- I created a method called update genre worksheet that would check the genre the user chose and pass all their info into the corresponding worksheet but during testing was met with a massive error that was inconcievable to me. After a short discussion, I realized that inside of the find_genre_worksheet if statement, I put the genre variable inside of the append_row() method when I needed to put in user_info as that variable holds all the users inputs.
- While looking at my validate_name() method, I realized that it only accepted a first name as a space would cause isalpha() to be false. I created 2 variables called fname and lname. name = fname + ' ' + lname didnt work and printed my error message. So i tried inserting the fname and lname variables into my if statement and used or so if one of them used something other than a letter, it would print the error message. Then a created one more variable called space and gave it an empty string and placed it between fname and lname in the name variable. Looking like this name = fname + space + lname. This worked without issue.
- Inside the validate_age method, I wanted to restrict the users age to between 16 and 80 so the user cannot enter false data that is absurd such as 1000 or 2. I tried if age > 80 or age < 16: but an error showed up which stated "not supported between instances of str and int". This was because the value of age was a string. So inside of the if statement, i used int(age) to convert the value to an integer so the condition would work, which it did.
- The validate_age method would bring an error and end the program if the user entered a decimal number or "float". I tried adding ->   and age.float() to the if statement that restricts input number size but didnt work because i entered float as an attribute of age which was wrong. solved by using elif float(age). This means if the age value can be converted to float, then do this code. I also had to place this above the elif (int(age)==age) statement as it would pass ValueError invalid literal for int() with base10: 'value'. But if the user enters something like 2.d2, It states that it could not convert the string to float and the closes the program. Unsure how to fix this yet.
- validate_age after fixing the previous issue, would then print my error message "Must be a whole number" when I typed 22. This was because I converted age to a float. I fixed this immediately by making it ->   elif age == float(age). solved without further issue.



# Issues unsolved

- If the user enters a value like 2.d2, The program brings up an error as it cant be converted to float so they if statement cannot be run.
