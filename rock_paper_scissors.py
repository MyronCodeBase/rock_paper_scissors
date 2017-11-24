import random

def rock_paper_scissors():
	game = True

	while game:
		user_input = str(raw_input("Enter rock, paper, or scissors: ")).lower()
		cpu_choice = random.choice(['rock', 'paper', 'scissors'])
		while not (user_input == 'rock' or user_input == 'paper' or user_input == 'scissors'):
			print("%s not a valid option." % (user_input))
			user_input = str(raw_input("Please enter rock, paper, or scissors: ")).lower()

		if(user_input == cpu_choice):
			print("Game results in a tie! both users choose %s" % (user_input))
		elif(user_input == 'rock' and cpu_choice == 'scissors'):
			print("User wins! %s beats %s" % (user_input, cpu_choice))
		elif(user_input == 'paper' and cpu_choice == 'rock'):
			print("User wins! %s beats %s" % (user_input, cpu_choice))
		elif(user_input == 'scissors' and cpu_choice == 'paper'):
			print("User wins! %s beats %s" % (user_input, cpu_choice))
		else:
			print("CPU wins %s beats %s" % (cpu_choice, user_input))

		game_choice = raw_input("Would you like to play again? (Yes or Y) ").lower()
		if game_choice not in ('yes','y'):
			print("Ending game!...Thanks for playing")
			game = False
			break
			
rock_paper_scissors()