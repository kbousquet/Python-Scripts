import random

max_range = input("Type a number: ")

if max_range.isdigit():
	if max_range.isdigit():
		max_range = int(max_range)

		if max_range <=0:
			print("Please type a number larger than 0 next time.")
			quit()

	else:
		print("Please type a number next time.")
		quit()


random_number = random.randint(1, max_range)
guesses = 0

while True:
	guesses += 1
	user_guess = input(f"Guess a number between 1 and {max_range}: ")
	if user_guess.isdigit():
		user_guess = int(user_guess)
	else:
		print('Please type a number next time.')
		continue

	if user_guess == random_number:
		print("You got it!")
		break
	elif user_guess > random_number:
		print("You were above the number.")
	else:
		print("You were below the number.")

print(f"You got it in {guesses} guesses")
