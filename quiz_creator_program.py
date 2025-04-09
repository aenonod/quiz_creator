# General flow of quiz creator program:
# Ask for the filename (if user wants to create/open another quiz)
# Ask user for input
# Store data into text file
# Loop the program until user chooses to exit


def file_naming():
    filename = input("Input your filename (w/o extension): ").strip()
    if not filename.endswith(".txt"):
        filename += ".txt"
    return filename

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
        correct_ans = input("\nCorrect answer: ").lower()

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

# Ask another input until user chooses to exit
def program_main_loop():
    filename = file_naming()
    
    while True:
        quiz_creator(filename)
            
        add_input = input("\nDo you want to add more questions? (yes/no): ").lower()
        if add_input == "yes":
            print()
            continue
        else:
            num_1 = print("-Press 1 to create new quiz file-")
            num_2 = print("-Press 2 to open a quiz file-")
            num_3 = print("-Press 3 to exit-")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Try again.")
            continue

        if choice == 1:
            print("Creating new file...")
            continue
        elif choice == 2:
                filename = input("Enter filename to open (with extension): ")
                try:
                    with open(filename, "r") as file:
                        print(f"\n>>> QUIZ ({filename}) <<<")
                        print(file.read())
                except FileNotFoundError:
                    print("File not found. Try again.")
        elif choice == 3:
            print("Goodbye, user!👋")
        else:
            print("Invalid input. Please choose between 1, 2, or 3.")
        
program_main_loop()     # Start the program