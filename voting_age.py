age = int(input("How old are you? "))
if age >= 18:
	print("You are old enough to vote!")
	answer = input("Have you registered to vote yet?")
	if answer.lower() == "y" or answer.lower() == "yes":
		print("That's great!")
	elif answer.lower() == "n" or answer.lower() == "no":
		print("That's too bad, you definitely should. Every vote counts!")
	else:
		print("Don't change the subject!")

else:
	print("You need to be at least 18 years old to vote.")