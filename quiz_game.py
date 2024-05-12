# Run this script to play a short quiz game.

number_points = 10
correct_questions = 0
hint_given = False

print("Welcome to my trivia quiz!\n")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
	quit()

print("Ok! Let's play :D\n")
print("Each question is worth 2 points. You can type 'Hint' to get a hint, at the expense of 1 point.")
print("Can you get all 10 points? Let's find out!\n")

print("Question 1:")
answer = input("What is the capital of Texas? ").lower().strip()
while True:
	if answer == "hint" and not hint_given:
		number_points -= 1
		hint_given = True
		answer = input("The chemical symbol for Gold makes up the first two letters. ")
	elif answer == "hint" and hint_given:
		answer = input("The hint for this question has already been given. ")
	elif answer == "austin":
		hint_given = False
		correct_questions += 1
		print("Correct!\n")
		break
	else:
		hint_given = False
		number_points -= 2
		print("Incorrect\n")
		break


print("Question 2:")
answer = input("What is the smallest planet in our solar system? ").lower().strip()
while True:
	if answer == "hint" and not hint_given:
		number_points -= 1
		hint_given = True
		answer = input("This is the closest planet to the sun. ")
	elif answer == "hint" and hint_given:
		answer = input("The hint for this question has already been given. ")
	elif answer == "mercury":
		hint_given = False
		correct_questions += 1
		print("Correct!\n")
		break
	else:
		hint_given = False
		number_points -= 2
		print("Incorrect\n")
		break


print("Question 3:")
answer = input("What is the human body’s largest organ? ").lower().strip()
while True:
	if answer == "hint" and not hint_given:
		number_points -= 1
		hint_given = True
		answer = input("It protects you from the outside world. ")
	elif answer == "hint" and hint_given:
		answer = input("The hint for this question has already been given. ")
	elif answer == "skin":
		hint_given = False
		correct_questions += 1
		print("Correct!\n")
		break
	else:
		hint_given = False
		number_points -= 2
		print("Incorrect\n")
		break


print("Question 4:")
answer = input("What is the fastest land animal? ").lower().strip()
while True:
	if answer == "hint" and not hint_given:
		number_points -= 1
		hint_given = True
		answer = input("It is the mascot for a popular brand of cheesy chips. ")
	elif answer == "hint" and hint_given:
		answer = input("The hint for this question has already been given. ")
	elif answer == "cheetah":
		hint_given = False
		correct_questions += 1
		print("Correct!\n")
		break
	else:
		hint_given = False
		number_points -= 2
		print("Incorrect\n")
		break


print("Question 5:")
answer = input("What is the only mammal capable of sustained flight? ").lower().strip()
while True:
	if answer == "hint" and not hint_given:
		number_points -= 1
		hint_given = True
		answer = input('A famous fictional vigilante is known for saying "I am the (blank)"  ')
	elif answer == "hint" and hint_given:
		answer = input("The hint for this question has already been given. ")
	elif answer == "bat":
		hint_given = False
		correct_questions += 1
		print("Correct!\n")
		break
	else:
		hint_given = False
		number_points -= 2
		print("Incorrect\n")
		break


# Print user's score
if correct_questions < 1:
	print("Oh no! You got all of the questions wrong. 0/10 points")
else:
	print(f"You answered {correct_questions} questions correct and earned {number_points}/10 points!")
