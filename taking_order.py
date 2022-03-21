# This script takes your pizza order and recites it back to you.

available_toppings = ['mushrooms', 'onions', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese','sausage','spinach']
requested_toppings = []
size = input("Would you like a large, medium, or small pizza? ")

ordering = True
while ordering == True:
	topping = input("What topping would you like on your pizza? ")
	if topping.lower() in available_toppings:
		print("Yes, we have that.")
		requested_toppings.append(topping)

	else:
		print("Sorry, we do not have " + topping + ".")

	add_more = False
	while add_more == False:
		answer = input("Would you like to add another topping? Yes or no? ")
		if answer.lower() == "y" or answer.lower() == "yes":
			add_more = True

		elif answer.lower() == "n" or answer.lower() == "no":
			print("Ok, you ordered a {} ".format(size) + "pizza with:")
			for requested_topping in requested_toppings:
				print(requested_topping)
				add_more = True
				ordering = False

		else:
			print("Sorry, I didn't catch that.")
			continue

