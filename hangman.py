import random


movies=['Omkara','Rustom','Aandhi','Saagar','Simmba','Sholay','Sarkar','Haider','Baaghi','koi mil gaya']

def choose_word():
	word = random.choice(movies)
	play_game(word) 
	#drona: this is bad software design. the flow of the code should be driven by the main code and not from functions. 
	#drona: this function should only return a randomly chosen word from the list movies

def play_game(randomword):
	word = list(randomword)
	blanks = "_" * len(word)
	blanks = list(blanks)
	guessed = []
	incorrect = 6
	
	#drona: without going into the details this doesnt look neat. If you see 3 or more levels of indentation in your code it is time to rethink about the design
	while incorrect > 0:
		print("\nYou have {} chances left.".format(incorrect) + "\nYour word: " + "".join(blanks) + "\nGuessed letters: " + ",".join(guessed))
		letter = input("Your guess: ")
		if len(letter) == 1 and letter.isalpha(): #drona: generally this can be implemented as a simple negative check. no need to keep the complete logic nested in this if
			if letter in word:
				for index,character in enumerate(word):
					blanks = list(blanks)
					if character == letter:
						blanks[index] = letter
						current = "".join(blanks)
						if blanks == word:
							print("\n\nCONGRATULATIONS, YOU WON!!\nYour word was " + ''.join(word) + ".\n")
							exit() #drona: do not exit from loop, use break and exit cleanly from outside the loop
			elif letter not in word: #drona: why not simply use else here? 
				incorrect -= 1
				guessed.append(letter)
		else:
			print("\n\n!Only single letters allowed!\n\n")
	else:
		print("\nSorry " + player + ", your game is over!\nYour word was " + ''.join(word) + ".")
        
		
player = input("Welcome To Hangman! Please type your name :: >")
player = player.title()

print("\nHey, " + player + " You get six incorrect guesses before you Die.")

f=choose_word()
	

