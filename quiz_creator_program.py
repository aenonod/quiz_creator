# General flow of quiz creator program:
# Ask user for input
# Store data into text file
# Loop the program until user chooses to exit
# Work with the output display (fonts, bold, italics, etc.)


def quiz_creator(count):
    with open("quiz.txt", "w") as file:
        # Input question
        print(">>> QUIZ CREATOR <<<")
        question = input(f"Input question {count}: ")

        # Input possible answers
        print("\nNote: No need to put letters in the choices. Let the quiz creator run it's magic!✨")
        choices_a = input("Possible answer: ").lower()
        choices_b = input("Possible answer: ").lower()
        choices_c = input("Possible answer: ").lower()
        choices_d = input("Possible answer: ").lower()

        # Input correct answer
        correct_ans = input("\nCorrect answer: ").lower()

        # Store data into text file
        file.write(f"\nQuestion {count}: {question}")
        file.write(f"\na) {choices_a}")
        file.write(f"\nb) {choices_b}")
        file.write(f"\nc) {choices_c}")
        file.write(f"\nd) {choices_d}")
            
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

# Ask another input until user chooses to exit
while True:
    num = 0
    quiz_creator(+1)
        
    add_input = input("\nDo you want to add more questions? (yes/no): ").lower()
    if add_input == "yes":
        print()
        continue
    else:
        file = open("quiz.txt", "r")
        print(file.read())
        file.close()
        break