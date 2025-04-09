# Ask for user input
# Store data into text file
def quiz_creator():
    with open("Quiz.txt", "w") as file:
        # Input question
        question = input("Input a question: ")
        file.write(question)

        # Input possible answers
        choices_a = input("Possible answer: ")
        file.write(choices_a)
        choices_b = input("Possible answer: ")
        file.write(choices_b)
        choices_c = input("Possible answer: ")
        file.write(choices_c)
        choices_d = input("Possible answer: ")
        file.write(choices_d)
            
        # Input correct answer
        correct_ans = input("Correct answer: ")
        file.write(correct_ans)

    file.close()

    file = open("Quiz.txt", "r")
    print(file.read())
    file.close()

# Ask another input until user chooses to exit
