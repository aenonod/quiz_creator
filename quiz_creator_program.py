# Ask for user input
# Store data into text file
def quiz_creator():
    with open("quiz.txt", "w") as file:
        # Input question
        print("=========== QUIZ CREATOR ==========")
        question = input("Input a question: ")
        file.write(f"\nQuestion: {question}")

        # Input possible answers
        print("\nNote: No need to put letters in the choices. Let the quiz creator run it's magic!✨")
        choices_a = input("Possible answer: ").lower()
        file.write(f"\na) {choices_a}")
        choices_b = input("Possible answer: ").lower()
        file.write(f"\nb) {choices_b}")
        choices_c = input("Possible answer: ").lower()
        file.write(f"\nc) {choices_c}")
        choices_d = input("Possible answer: ").lower()
        file.write(f"\nd) {choices_d}")
            
        # Input correct answer
        correct_ans = input(f"\nCorrect answer: ").lower()

        letter = ""
        if correct_ans == choices_a:
            letter = 'a)'
        elif correct_ans == choices_b:
            letter = 'b)'
        elif correct_ans == choices_c:
            letter = 'c)'
        elif correct_ans == choices_d:
            letter = 'd)'

        file.write(f"\nCorrect answer: {letter} {correct_ans}")

    file.close()

    file = open("Quiz.txt", "r")
    print(file.read())
    file.close()

quiz_creator()

### Ask another input until user chooses to exit