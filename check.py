#!/usr/bin/env python3
"""
File containing all functions used to check if data in the Preorders table is valid.
"""
import sqlite3 as sql


def is_game_preorder_valid (user_id: int, game_id: int):
	"""
    Function used to check if a game preorder is valid. A game preorder is considered valid if:
    1. The user's ID exists
    2. The game's ID exists
    3. The user has paid.
	4. The user has selected a game.

	:param user_id: Integer representing a user's unique identifier within the Customers table.
	:param game_id: Integer representing a game's unique identifier within the Games table.

	:raise ValueError: Raised if user_id or game_id are incorrect

	:return bool: True if preorder is valid, false otherwise

	"""
	con = sql.connect("games_store.db")
	cur = con.cursor()

	cur.execute("""SELECT * FROM Customers WHERE ID = (?)""", (user_id,))

	if not cur.fetchone():  # If user's ID isn't in table
		raise ValueError(f"Customer ID '{user_id}' does not exist")  # Better to ask for forgiveness than permission
	
	cur.execute("""SELECT * FROM Games WHERE ID = (?)""", (game_id,))

	if not cur.fetchall():
		raise ValueError(f"Game ID '{game_id}' does not exist")

	# By this point we know that the user and game are registered in the database

	cur.execute("""SELECT * FROM Preorders WHERE GAMEID = (?) AND CUSTOMERID = (?) AND PAYMENT = (1) """, (game_id, user_id))

	if cur.fetchone():
		return True
	else:
		return False

	
