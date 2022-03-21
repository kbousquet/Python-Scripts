# This script takes in two inputs and determines if they are anagrams of each other.

input_a = input("Input A ")
input_b = input("Input B ")

sorted_a = sorted(input_a.lower())
sorted_b = sorted(input_b.lower())

if sorted_a == sorted_b:
	print(input_a + " and " + input_b + " are anagrams.")

else:
	print(input_a + " and " + input_b + " are not anagrams.")