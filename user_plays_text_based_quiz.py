# General flow of quiz creator program:
# a. Ask for the filename (if user wants to create/open another quiz)
#    Ask user for input
#    Store data into text file
#    Loop the program until user chooses to exit
# b. View quiz file
# c. Questions will be randomly answered by the user
#    Program will check if the answer is correct

import random

# Function to set filename var (for creating/opening a file)
def file_naming():
    filename = input("\nInput your filename (w/o extension): ").strip()
    if not filename.endswith(".txt"):
        filename += ".txt"
    return filename

# Function to ask user for input then store the collected data
def quiz_creator(filename):
    with open(filename, "a") as file:
        # Input question
        print("\n>>> QUIZ CREATOR <<<")
        question = input(f"Input question: ")

        # Input possible answers
        print("\nNote: No need to put letters in the choices. Let the quiz creator run it's magic!✨")
        choices_a = input("Possible answer: ").lower()
        choices_b = input("Possible answer: ").lower()
        choices_c = input("Possible answer: ").lower()
        choices_d = input("Possible answer: ").lower()

        # Input correct answer
        correct_ans = input("\nCorrect answer (a/b/c/d): ").lower()

        # Store data into text file
        file.write(f"\nQuestion: {question}")
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

        file.write(f"\nCorrect answer: {letter} {correct_ans}\n")

    file.close()

# Function to add more questions in a file
def add_questions(filename):
    while True:
        quiz_creator(filename)
            
        add_input = input("\nDo you want to add more questions? (yes/no): ").lower()
        if add_input == "yes":
            print()
            continue
        else:
            main_menu()

# Load to quiz from file
def load_quiz(filename):
    with open(filename, "r") as file:
        # to remove empty lines
        lines = [line.strip() for line in file if line.strip()]
        
    quiz = []
    index = 0
    while index < len(lines):
        question = lines[index]
        choices = [lines[index+1], lines[index+2], lines[index+3], lines[index+4]]
        answer = lines[index+5]
        quiz.append({
            "question": question,
            "choices": choices,
            "answer": answer
        })
        index += 6     # move to the next question block
    return quiz

# Run the quiz
def run_quiz(quiz):
    random.shuffle(quiz)     # Shuffle questions
    score = 0

    for entry in quiz:
        print("\n" + entry["question"])
        for choice in entry["choices"]:
            print(choice)
        user_input = input("\nYour answer (a/b/c/d): ").strip().lower()
        
        if user_input == entry["answer"]:
            print("\n✅ Correct +1 point!")
            score += 1
        else:
            print(f"\n❌ Wrong! The answer was {entry['answer']}.")
            
        to_proceed = input("\nDo you want to continue? (yes/no): ").lower()
        if to_proceed == "yes":
            continue
        elif to_proceed == "no":
            print(f"\nYour final score: {score}/{len(quiz)}")
            
        while True:
            try:
                print("\n❗ Entering 'no' will exit the program.")
                back = input("Do you want to go to main menu? (yes/no): ")
                
                if back not in ["yes", "no"]:
                    raise ValueError("Invalid input. Please answer with 'yes' or 'no'.")
                
                if back == "yes":
                    main_menu()
                elif back == "no":
                    break  
            except ValueError as error:
                print(error)

# Function for main menu
def main_menu():
    while True:
        print("""\n===== MAIN MENU =====
👆 Press 1 to start a quiz
👆 Press 2 to create new or edit an existing quiz file
👆 Press 3 to view a quiz file
👆 Press 4 to exit""")

        try:
            choice = int(input("\n⭐ Enter your choice: "))
            
            if choice not in [1, 2, 3, 4]:
                raise ValueError("Invalid input. Try again.")

            if choice == 1:
                while True:
                    try:
                        filename = input("\nEnter filename to open (with extension): ")
                        quiz = load_quiz(filename)
                        run_quiz(quiz)
                        break
                    except FileNotFoundError:
                        print("File not found. Try again.")
                        continue
                
            elif choice == 2:
                filename = file_naming()   # Will ask for a filename
                add_questions(filename)   # Loop to ask user for question/s
                    
            elif choice == 3:
                while True:
                    filename = input("\nEnter filename to open (with extension): ")
                    try:
                        with open(filename, "r") as file:   # Open file to read
                            print(f"\n>>> QUIZ ({filename}) <<<")
                            print(file.read())
                    except FileNotFoundError:
                        print("\nFile not found. Try again.")
                        continue
                    
                    print("\n❗ Entering 'no' will exit the program.")        
                    back = input("Go back to main menu? (yes/no): ").lower()
                    if back == "yes":
                        break
                    else:
                        print("\nExiting...")
                        exit()
            
            elif choice == 4:
                print("\nGoodbye, user!👋")
                break
            
        except ValueError as error:   # Error if user input isn't in the choices
            print(error)
            continue
        
# Start the program
if __name__ == "__main__":
    main_menu()