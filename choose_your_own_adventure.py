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
	answer = input('You come to a bridge that does not look safe. Do you try to "cross" the bridge or turn "back?"\n')
	if answer == "back":
		print('You turn to head back, only to find yourself face to face with a group of bandits that had been')
		print('tailing you. You are outnumbered and are swiftly taken down.')
		print("You have died.\n")
	elif answer == "cross":
		print("You manage to cross the bridge just in time before the structure collapses. There is no turning back now.\n")
		print('You continue your journey and eventually come across a stranger in your path.')
		answer = input('Do you "talk" to them or "ignore" them?\n')
		if answer == "talk":
			print('The stranger is so happy that you stopped to talk to them that they give you all of their gold!')
			print("You have won!\n")
		elif answer == "ignore":
			print("You give the stranger a wide berth and only realize too late of your offense until their dagger is in your back")
			print("You have died.\n")
	else:
		print("You both hesitate to move and find yourselves in a staring contest that last days on end until you both")
		print("succumb to hunger and thirst.")
		print("You have died.\n")


else:
	print('Invalid response. You decide to attempt casting a detection spell to determine which is the correct path, but')
	print('your lack of magical prowess caused the spell to backfire at you.')
	print("You have died.\n")


print(f"You gave it your best, {name}")