import random

def rock_paper_scissors():
	game = True

	while game:
		player1_choice = str(raw_input("Player 1 Enter rock, paper, or scissors: ")).lower()
		player2_choice = str(raw_input("Player 2 Enter rock, paper, or scissors: ")).lower()
		while not (player1_choice == 'rock' or player1_choice == 'paper' or player1_choice == 'scissors'):
			print("%s not a valid option Player 1." % (player1_choice))
			user_input = str(raw_input("Please enter rock, paper, or scissors: ")).lower()
		while not (player2_choice == 'rock' or player2_choice == 'paper' or player2_choice == 'scissors'):
			print("%s not a valid option Player 2." % (player2_choice))
			user_input = str(raw_input("Please enter rock, paper, or scissors: ")).lower()

		if(player1_choice == player2_choice):
			print("Game results in a tie! both users choose %s" % (player1_choice))
		elif(player1_choice == 'rock' and player2_choice == 'scissors'):
			print("Player 1 wins! %s beats %s" % (player1_choice, player2_choice))
		elif(player1_choice == 'paper' and player2_choice == 'rock'):
			print("Player 1 wins! %s beats %s" % (player1_choice, player2_choice))
		elif(player1_choice == 'scissors' and player2_choice == 'paper'):
			print("Player 1 wins! %s beats %s" % (player1_choice, player2_choice))
		else:
			print("Player 2 wins %s beats %s" % (player2_choice, player1_choice))

		game_choice = raw_input("Would you like to play again? (Yes or Y) ").lower()
		if game_choice not in ('yes','y'):
			print("Ending game!...Thanks for playing")
			game = False
			break
			
rock_paper_scissors()