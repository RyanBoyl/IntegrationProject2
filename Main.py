#Ryan Boyle
#This program is a Jeopardy-like quiz game.
#Users are asked to identify a certain answer given a prompt.
#There are two topics in the quiz: Geography and Math.

import time
#This imports the time library to the program.
#Any functions in this library can now be used in the program.

def calculate_score(current_score, points_to_add):
#The above line of code defines a function. It is called the function header.
#The subsequent lines of code in the function
#will be executed if the function statement is simply called.
    to_win = 1400

#The function header also includes two parameters.
#This means that a function call will also require two arguments to work.
#In this case, the function calculate_score() will require both the current
#score and the number of points added for a correct answer in the parentheses.
    current_score += int(points_to_add)
#The above line uses the int() function.
#This converts a value to an integer.

#The above line of code also includes a += shortcut operator.
#This will set the variable before the operator equal to the value
#after the operator plus the variable.

#For example, if current_score was 50, then score += 100 would be 100+50 = 150.
#Another way to code this would be current_score = current_score + 100
    print("Your score is:", current_score, "points.")
#The above line of code uses the print() function.
#This outputs a certain message to the user's screen.
    points_left = to_win - current_score
    if(current_score < to_win):
#The above line of code includes an if statement.
#This will execute subsequent lines of code within it if a condition is true.
        
#The above line of code also uses a less than operator.
#This returns true if the value before it is less than the value after it.
        print("You need", points_left, "more points to win.\n")
#The new line character "\n" is used in the above line of code.
#This creates a new text line in its place.
    elif(current_score >= to_win):
#The above line of code includes an elif statement.
#If the condition in the if statement is false, but the condition here is true
#then the subsequent lines of code here will execute.
        
#The above line of code also uses a greater than or equal to operator.
#This returns true if the value before it is greater than or equal to
#the value after it.
        print("You have enough points to win the game!")
        print("Continue playing to see how many points you can get!\n")
    return current_score
#The above line of code includes a return statement.
#This will return the updated score value as the output of the function.

#Essentially, the function calculate_score() will update the player's score
#if they earn points from answering a question.
#It will also notify them how many points they have left until they reach
#the winning score of 1400.
#If they have already reached that point, the function will tell them
#that they have enough points to win the game, but should keep playing.

def main():
    print("Welcome to my Integration Project: Jeopardy!\n")
    time.sleep(3)
#The above line of code will delay the execution of further code
#by a certain amount of seconds.
    print("You will be asked questions in two separate categories:")
    print("Geography and Math. \n")
    time.sleep(3)

    print("Earn at least 1400 points to win!\n")

    time.sleep(3)

    continue_input = input('Type "Ready!" to continue: ')
#The above line of code uses the input() function.
#This allows data to be entered into the program by the user.

    while(continue_input != "Ready!"):
#The above line of code includes a while loop statement.
#This allows subsequent lines of code within it to be repeated
#until a condition is satisfied.

#The above line of code also includes a not equal to operator.
#This returns true if the values before and after it are not equal.

#In this case, the code below loops until continue_input is equal to "Ready!"
        continue_input = input('Ok, type "Ready!" when you want to continue: ')

    score = 0

    print("\nFirst Category: Geography \n")

    time.sleep(3)

    print("Question 1 (100 points):")
    time.sleep(1)
    print("Vienna is the capital of this country.")
    geography_input1 = input("What is... ")
    if(geography_input1 == "Austria"):

#The above line also includes an equal to operator.
#This returns true if the values before and after it are equal.
        print("Correct! The correct answer is: Austria.")
        score = calculate_score(score, 100)
    else:
#The above line of code is an else statement.
#If the condition in the if statement is false, the subsequent lines of code
#here will execute.
        print("That answer is incorrect. The correct answer is: Austria.")
        score = calculate_score(score, 0)

    time.sleep(3)

    print("Question 2 (200 points):")
    time.sleep(1)
    print("This nation owns Greenland, the largest island in the world.")
    geography_input2 = input("What is... ")
    if(geography_input2 == "Denmark"):
        print("Correct! The correct answer is: Denmark.")
        score = calculate_score(score, 200)
    else:
        print("That answer is incorrect. The correct answer is: Denmark.")
        score = calculate_score(score, 0)

    time.sleep(3)

    print("Question 3 (300 points):")
    time.sleep(1)
    print("In French Polynesia, there is a tiny island ", end='')
#The above line of code uses an "end=" argument.
#This prevents a new line from being made after the end of a print statement.
    print("that has become a world renown vacation spot.")
    print("The name of the island consists of a singular word repeated twice.")
    geography_input3 = input("What is... ")
    island_name = (geography_input3 + " ")*2
#The above line uses the "+" string operator.
#This operator concatenates, or connects, multiple strings together.

#The above line also uses the "*" string operator.
#This repeats a string placed before the operator a certain amount of times.
#It is used here in order to turn the user's response, which is one word
#into what would be the island's name. "Bora" would become "Bora Bora" here.
#A space was concatenated to geography_input3 before multiplying so that the
#string could be "Bora Bora " instead of "BoraBora".
    if(geography_input3 == "Bora"):
        print("Correct! The correct answer is: Bora, ", end='')
        print("referring to the island of Bora Bora.")
        score = calculate_score(score, 300)
    elif(geography_input3 == "Bora Bora"):
        print("You got the right name, but were supposed to enter one word.")
        print("Your answer would now be the name ", island_name, ".", sep='')
#The above line of code uses a "sep=" argument.
#This removes the space created when concatenating variables with a comma.
        print("As a result, you will receive half the points.")
        score = calculate_score(score, 150)
    else:
        print("Sorry, that answer is incorrect. The correct answer is: Bora.")
        print("This results in Bora Bora as the island's name.")
        score = calculate_score(score, 0)

    time.sleep(3)

    print("\nWe will now move on to the next category: Math.\n")

    time.sleep(3)

    print("Question 1 (100 points):")
    time.sleep(1)
    print("This number equals 8 when cubed.")
    print("Enter whole numbers only.")
    math_input1 = input("What is... ")
    math_int1 = int(math_input1)
    math_user_solution1 = (math_int1)**3
#The above line of code uses the "**" numeric operator, or the power operator.
#This raises an integer or float to the power of another integer or float.
#The user's input is being cubed in the above line to see if their input
#results in a value or 8 or not.
    math_answer1 = 8**(1/3)
#In the above line, the cube root of 8 is being taken in order to find
#the solution to the original question, which is 2.
    if(math_int1 == math_answer1):
        print("Correct! The answer is: ", int(math_answer1), ".", sep='')
        score = calculate_score(score, 100)
    else:
        print("Incorrect. The answer is: ", int(math_answer1), ".", sep='')
        print("Your response was: ", math_input1, ".", sep='')
        print("This yields a result of: ", math_user_solution1, ".\n", sep='')
        score = calculate_score(score, 0)

    time.sleep(3)

    print("Question 2 (300 points):")
    time.sleep(1)
    print("In the expression ((x+11)/3)*4, ", end='')
    print("this value of x will result in a solution of 68.")
    print("Enter whole numbers only.")
    math_input2 = input("What is... ")
    math_int2 = int(math_input2)
    math_user_solution2 = (((math_int2)+11)/3)*4
#The above line is plugging in the user's input into the expression.
#This will evaluate what solution their input yields. It should be 68.

#The above line uses the "+" numeric operator, or the addition operator.
#This adds multiple integers or floats together.

#This line also uses the "*" numeric operator, or the multiplication operator.
#This multiplies various integers or floats together.

#Finally, this line uses the "/" numeric operator, or the division operator.
#This finds the quotient of certain integers or floats.
    math_answer2 = ((68/4)*3)-11
#The above line uses the "-" numeric operator, or the subtraction operator.
#This finds the difference between certain integers or floats.
#The expression is being solved backwards here in order to get the value of x.
#This value is 40.

    if(math_int2 == math_answer2):
        print("Correct! The answer is: ", int(math_answer2), ".", sep='')
        score = calculate_score(score, 300)
    else:
        print("Incorrect. The answer is: ", int(math_answer2), ".", sep='')
        print("Your response was: ", math_input2, ".", sep='')
        print("This yields a result of: ", math_user_solution2, ".\n", sep='')
        score = calculate_score(score, 0)

    time.sleep(3)

    print("Question 3 (200 points):")
    time.sleep(1)
    print("After dividing 200 by 7, the remainder is this number.")
    print("Enter whole numbers only.")
    math_input3 = input("What is... ")
    math_int3 = int(math_input3)
    math_answer3 = 200%7
#The above line of code uses the "%" numeric operator, or the modulus operator.
#This finds the remainder after dividing one integer or float by another.

    if(math_int3 == math_answer3):
        print("Correct! The correct answer is: ", math_answer3, ".", sep='')
        score = calculate_score(score, 200)
    else:
        print("Incorrect. The correct answer is: ", math_answer3, ".", sep='')
        print("Your response was: ", math_input3, ".\n", sep='')
        score = calculate_score(score, 0)

    time.sleep(3)

    print("BONUS (200 points):")
    time.sleep(1)
    print("Ignoring the remainder, you get this when dividing 200 by 7.")
    print("In other words, use floor division.")
    print("Enter whole numbers only.")
    bonus_input = input("What is... ")
    bonus_int = int(bonus_input)
    bonus_answer = 200//7
#The above line uses the "//" numeric operator, or the floor division operator.
#This finds the quotient of two numbers while disregarding any remainder.

    if(bonus_int == bonus_answer):
        print("Correct! The correct answer is: ", bonus_answer, ".", sep='')
        score = calculate_score(score, 200)
    else:
        print("Incorrect. The correct answer is: ", bonus_answer, ".", sep='')
        print("Your response was: ", bonus_input, ".\n", sep='')
        score = calculate_score(score, 0)

    time.sleep(3)

    print("It's time for Final Jeopardy! (500 points)")
    time.sleep(2)
    print("The topic for Final Jeopardy will be: History.")
    time.sleep(2)
    print("You will need to enter two answers to get the full 500 points.\n")
    time.sleep(2)
    print("Two Founding Fathers died on July 4th, 1826.")
    print("This date was exactly 50 years after the signing of the ", end='')
    print("Declaration of Independence.")
    print("What were the names of these two Founding Fathers?")
    final1 = input("First Founding Father: Who was... ")
    final2 = input("Second Founding Father: Who was... ")
    JA = "John Adams"
    TJ = "Thomas Jefferson"
    if(not(final1 == final2)):
#The above line of code uses the not Boolean operator.
#This returns true if the statement inside is false.

#The above code ensures that the following lines of code will not execute
#if the same answer is entered twice.
        if(final1 == JA or final1 == TJ) and (final2 == JA or final2 == TJ):
#The above line of code uses the or Boolean operator.
#This returns true if at least one of the conditions given is true.

#The above code returns true if both Thomas Jefferson and John Adams
#are entered in any order.

#The above line of code also uses the and Boolean operator.
#This returns true if both of the conditions given are true.
            print("Congratulations! Your response is correct!")
            score += 500
        elif(final1 == JA or final1 == TJ) or (final2 == JA or final2 == TJ):
#The above line of code returns true if at least one answer is correct.
#It will not execute if both answers are correct as it is an elif statement.
#The if statement before it checks for that.
            print("You only got one of the responses correct.")
            print("The correct responses were " + JA + " and " + TJ + ".")
            print("As a result, you will only receive half of the points.")
            score += 250
        else:
            print("Sorry, that answer is incorrect.")
            print("The correct responses were " + JA + " and " + TJ + ".")
            print("As a result, you will not receive any points.")
    else:
        print("You can't enter the same answer twice!")
        print("Now you will not receive any points.\n")
#Essentially, the user will receive 500 points if they enter both
#Thomas Jefferson and John Adams in any order.
#They will receive 250 points if they enter one of the correct names.
#Finally, they will receive 0 points if they enter no correct answers
#or enter the same answer twice.
    print("Your final score is:", score, "points.\n")

    time.sleep(3)

    to_win = 1400

    if(score >= to_win):
        prize = score*10
        print("Congratulations, you have over 1400 points ", end='')
        print("and have won Jeopardy!")
        print("You will receive $", prize, ".\n", sep='')

    if(score < to_win):
        print("Sorry, you did not reach the winning score of 1400 points!")
        print("You will not receive any money.\n")

    time.sleep(3)

    for x in range(3):
#The above line of code includes a for loop statement.
#This allows subsequent lines of code within it to be repeated
#a specified amount of times.

#The above line of code also includes an in statement.
#This permits the for loop to execute if the variable before it is within
#the list after it

#Finally, the above line includes the range() function.
#This specifies within what range the loop should execute in.

#Simply, this for loop repeats a phrase three times.
        print("Thank you for playing Jeopardy!")

    time.sleep(3)

    print("\nExtra Requirements:")
    number = 5
    number -= 3
#The above line of code includes a -= shortcut operator.
#This will set the variable before the operator equal to this variable
#minus the value after the operator.
    print("5 - 3 is", number)
    number2 = number
    number2 *= 2
#The above line of code includes a *= shortcut operator.
#This will set the variable before the operator equal to the value
#after the operator times the variable.
    print(number, "* 2 is", number2)

main()
#As all of the questions are within the main() function, calling to main()
#will let the game run.
