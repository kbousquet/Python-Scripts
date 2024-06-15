# This script simulates a dice game called PIG.
# 2 to 4 players take turns rolling a dice. While rolling, the value of the dice gets added onto the current player's
# total score. Rolling a 1 will end that player's turn. When a player reaches at least a score of 50, their turn will
# end and all remaining players will be able to do a turn that round. Once all players have played that round,
# the player with the maximum points wins.

import random


def roll():
	min_value = 1
	max_value = 6
	value = random.randint(min_value, max_value)

	return value


while True:
	players = input("Enter the number of players (2 - 4): ")
	if players.isdigit():
		players = int(players)
		if 2 <= players <= 4:
			break
		else:
			print("Must be between 2 - 4 players.")

	else:
		print("Invalid, try again.")


max_s = 50
player_scores = [0 for _ in range(players)]


while max(player_scores) < max_s:

	for player in range(players):
		print("\nPlayer", player + 1, "'s turn has just started!")
		print("Your total score is:", player_scores[player], "\n")
		current_score = 0

		while True:
			should_roll = input("Would you like to roll (y)? ")
			if should_roll.lower() != "y":
				break

			value = roll()
			if value == 1:
				print("You rolled a 1! End of turn.")
				break
			else:
				current_score += value
				print("You rolled a: ", value)

			print("Your score is: ", current_score)

		player_scores[player] += current_score
		print("Your total score is: ", player_scores[player])

	max_score = max(player_scores)
	winning_index = player_scores.index(max_score)
	print("Player", winning_index + 1, "won with a score of:", max_score)

