print("<<< | Welcome to rock, paper, scissors remasterd | >>>")

#gör så vi kan använda random funktionen
import random

menu = 0
player = 0
ai = 0

#loopar allt tills man trycker "2"
while menu != 2:

    print("\n<<<| Main menu |>>>")
    print("\n1. Versus AI")
    print("2. Quit") 

#try används för att programmet inte ska krasha, om man skriver in en bokstav istället för siffra
    try: 
        menu = int(input("\nChoose a alternativ:"))
    except: 
        print("\nPick a number!\n")

    if menu == 1:
        while player != 4:
            print("\n1. Rock")
            print("2. Paper")
            print("3. Scissors")
            print("4. Return to main menu")
        
            try:
                player = int(input("\nChoose: "))
            except:
                print("\nPick a number!\n")
            
            import os
            os.system("cls")

            if player == 1 and ai == 1:
                print("You picked: ", player)
                print("AI picked: ", ai)
                print("Draw")
            elif player == 1 and ai == 2:
                print("You picked: ", player)
                print("AI picked: ", ai)
                print("AI wins!")
            elif player == 1 and ai == 3:
                print("You picked: ", player)
                print("AI picked: ", ai)
                print("You win!")
            elif player == 2 and ai == 1:
                print("You picked: ", player)
                print("AI picked: ", ai)
                print("You win!")
            elif player == 2 and ai == 2:
                print("You picked: ", player)
                print("AI picked: ", ai)
                print("Draw!")
            elif player == 2 and ai == 3:
                print("You picked: ", player)
                print("AI picked: ", ai)
                print("AI win!")
            elif player == 3 and ai == 1:
                print("You picked: ", player)
                print("AI picked: ", ai)
                print("AI win!")
            elif player == 3 and ai == 2:
                print("You picked: ", player)
                print("AI picked: ", ai)
                print("You win!")
            elif player == 3 and ai == 3:
                print("You picked: ", player)
                print("AI picked: ", ai)
                print("Draw!")
            elif player == 4:
                print("")
            else:
                print("Incorrect choice, pick again! ")
