# This script takes in two string inputs and determines if they are anagrams of each other.
# Anagrams are when one word or phrase, rearranged, creates a different word or phrase.
# Example: "iceman" and "cinema"

def check_if_anagram(input_a, input_b):
	sorted_a = sorted(input_a.lower())
	sorted_b = sorted(input_b.lower())

	if sorted_a == sorted_b:
		print(input_a + " and " + input_b + " are anagrams.")
	else:
		print(input_a + " and " + input_b + " are not anagrams.")


check_if_anagram("iceman", "cinema")

check_if_anagram("dog", "cat")