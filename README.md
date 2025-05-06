## quiz_creator

### 📁 quiz_creator_program.py
The quiz creator program prompts the user to enter a question, possible answers (a, b, c, d), and the correct answer. It then writes the collected data to a text file. The program continues to ask for more input until the user chooses to exit.  

Limitations:
* There is no autocorrect feature, so the user should double-check the spelling of their inputs.
* Users cannot delete or remove a question once it's been entered.

### 📁 user_plays_text_based_quiz.py
This program reads the output file and allows the user to answer randomly selected questions and check whether their answers are correct.  

Limitations:
* There is no autocorrect feature, so the user should double-check the spelling of their inputs.
* The program is sensitive to the spelling of both answers and filenames.
* The user must finish the quiz, as exiting midway is not allowed.
