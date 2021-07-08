print("Number Guessing Game")
print("Guess a number between 0-9")
import random
rand = random.randint(0,10)
chances = 0
while chances < 5 :
	guess = int(input("Type your guess -:"))
	if guess == rand :
		print("You are Correct . CONGRATULATION!!!!")
		break
	elif guess < rand :
		print("You are near to it . Keep Trying :) . Guess higher than ",guess)
	else :
		print("You Went higher . Try Again ! . Guess lower than ",guess)
	chances+=1
if not chances < 5 :
	print("You Lost It :( , The Number is ",rand)