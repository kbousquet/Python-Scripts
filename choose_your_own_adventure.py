name = input("Welcome, adventurer. What is your name? \n")
print(name, "is a good, strong name.\n")
print("As we proceed along this adventure, your answer options will be inside double quotations.")
print("Please know, if you choose an answer other than what is provided, you will suffer a terrible")
print("fate and your journey will end.\n")


answer = input('You are journeying along a dirt road and have stumbled across a fork in the path. Do you go "left" or "right"? \n').lower()

if answer == "left":
	print('You decide to take the left path.\n')
	answer = input('You come to a river. Do you "swim" across the rushing water or "walk" around it? \n')

	if answer == "swim":
		print("Not knowing how far the nearest safe crossing was, you decide to plunge into the cold, dark water and")
		print("begin swimming towards the far shore. Suddenly, you feel the sharp teeth of an alligator clamp down on")
		print("your leg and pull you under.")
		print("You have died.\n")
	elif answer == "walk":
		print("After walking several hours down the riverbank, you stop to catch a fish for dinner. Unbeknownst to you,")
		print("you have come across the territory of a mother bear and her two cubs. She attacks you before you have a")
		print("chance to draw your weapon.")
		print("You have died.\n")
	else:
		print("Invalid response. You spot an old boat in the undergrowth near the bank and decide to try rowing across,")
		print("but just as you're setting off, two highly venomous snakes slither out from under the seat and bite you.")
		print("You have died.\n")

elif answer == "right":
	print('You decide to take the right path.\n')
else:
	print('Invalid response. You decide to attempt casting a detection spell to determine which is the correct path, but')
	print('your lack of magical prowess caused the spell to backfire at you.')
	print("You have died.\n")