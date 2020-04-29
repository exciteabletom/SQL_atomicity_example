#!/usr/bin/env python3
import check
import sys

if __name__ == "__main__":  # If program being run from command prompt
	if len(sys.argv) != 3:
		raise ValueError(
		"""Not enough args passed.

		Example Usage:
		python3 main.py 100 200

		Where 100 is the user's id and 200 is the game's id.""")
		
	user_id = int(sys.argv[1])
	game_id = int(sys.argv[2])

	
	if check.is_game_preorder_valid(user_id, game_id):
		print(f"User {user_id}'s preorder of game {game_id} is correct.")
	else:
		print(f"User {user_id}'s preorder of game {game_id} is not correct.")

