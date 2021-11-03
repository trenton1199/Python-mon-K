import random 
while True:
	x = random.randint(1,3)
	choice = input("rock paper sciscors r for rock p for paper s for sciscors ")
	if x == 1:
		print("computer chose rock")
	elif x == 2:
		print("computer chose paper")
	elif x == 3:
		print("computer chose sciscors")
	else:
		print("")
	if x == 1 and choice == "r":
		print("you chose 🪨: tie")
	elif x == 2 and choice == "r":
		print("you chose 🪨: computer wins!")
	elif x == 3 and choice == "r":
		print("you chose 🪨: you win!")
	else:
		print("")
	if x == 1 and choice == "p":
		print("you chose 📜: you win!")
	elif x == 2 and choice == "p":
		print("you chose 📜: tie")
	elif x == 3 and choice == "p":
		print("you chose 📜: computer wins! ")
	else:
		print("")
	if x == 1 and choice == "s":
		print("you chose ✂: computer wins!")
	elif x == 2 and choice == "s":
		print("you chose ✂️: you win!")
	elif x == 3 and choice == "s":
		print("you chose ✂️: tie")
	else:
		print("")
	if choice != "r" and choice != "p" and choice != "s":
		print("*** Unexpected Error ***")
	a = input("do you want to play again y/n").lower()
	if a == "y":
		print("")
	elif a == "n":
		break
		 
