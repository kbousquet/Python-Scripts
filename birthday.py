# This script prompts for the user's birthday, then returns "happy birthday" with the correct number ending.

age = input("What is your age? ")

if age.startswith("1"):
    # for 1
    if age == "1":
        message = "Happy " + str(age) + "st Birthday!"
        print(message)
    # for 11-19
    else:
        message = "Happy " + str(age) + "th Birthday!"
        print(message)

# all other numbers, outside of 1 and 11, that ends with 1
elif age.endswith("1"):
    message = "Happy " + str(age) + "st Birthday!"
    print(message)

elif age.endswith("2"):
    message = "Happy " + str(age) + "nd Birthday!"
    print(message)

elif age.endswith("3"):
    message = "Happy " + str(age) + "rd Birthday!"
    print(message)

# All other numbers, outside of 14-19, that end with 4-9
else:
    message = "Happy " + str(age) + "th Birthday!"
    print(message)
