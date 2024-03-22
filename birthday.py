# This script prompts for the user's birthday, then returns "happy birthday" with the correct suffix.

def print_happy_birthday(age):
    if age.startswith("1"):
        # for 1
        if age == "1":
            suffix = "st"
        # for 11-19
        else:
            suffix = "th"

    # all other numbers, outside of 1 and 11, that ends with 1
    elif age.endswith("1"):
        suffix = "st"

    elif age.endswith("2"):
        suffix = "nd"

    elif age.endswith("3"):
        suffix = "rd"

    # All other numbers, outside of 14-19, that end with 4-9
    else:
        suffix = "th"

    print("Happy " + str(age) + str(suffix) + " Birthday!")

print_happy_birthday("27")
print_happy_birthday("32")
print_happy_birthday("73")


# Output:
# Happy 27th Birthday!
# Happy 32nd Birthday!
# Happy 73rd Birthday!