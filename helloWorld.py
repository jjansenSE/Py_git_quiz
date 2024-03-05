print("Git is awesome!")

number_of_question = 4
right_answers = 0


# Quiz starts - 4 Question quizes
while True:
    take_part = input("Would you like to take part in the GIT quiz: \n1. Yes\n2. No\n: ")
    if take_part == "1":
        print('''Git Quiz:
            answer the 4 multiple choice questions below to test your knowledge on Git ''')

        question_one = input('''A. what is git?
                            1. A remote repository platform.
                            2. A version control system
                            3. A programming language.
                            4. A nickname for GitHub
                            --->''')

        # Counter for correct answers
        if int(question_one) == 2:
            right_answers += 1

        question_two = input('''B. Git is the same as GitHub --->
                            1. True 
                            2. False
                            --->''')

        if int(question_two) == 2:
            right_answers += 1

        question_three = input('''C. What is the command to get the installed version of Git?
                            1. git help version
                            2. gitVersion   
                            3. getGitVersion
                            4. git --version
                            ---> ''')

        if int(question_three) == 4:
            right_answers += 1

        question_four = input('''1. What is the command to set the user email for the current repository?
                            1. git email.user
                            2. git config email
                            3. git config user.email
                            --->''')

        if int(question_four) == 3:
            right_answers += 1

        # Zero division error check
        if int(right_answers) == 0:
            print("Unfortunately you did not get any right, try harder next time.")
        else:
            if int(right_answers) == 1:
                print(f"You scored: {(float(right_answers/number_of_question)*100)}%.  You can do better next time.")
            elif int(right_answers) == 2:
                print(f"You scored: {(float(right_answers/number_of_question)*100)}%. You did good but not good enough.")
            elif int(right_answers) == 3:
                print(f"You scored: {(float(right_answers/number_of_question)*100)}%. Well done, you almost did it.")
            elif int(right_answers) == 4:
                print(f"You scored: {(float(right_answers/number_of_question)*100)}%. Brilliant!!!")
    break
    