import random
import time

def restart_game():
    print("If You want to restart the game")
    ans = input("Press y, else any other key: \n") #there are choice to play game(restart)
    if ans == "y":
        hangman() # again call function according to player wants to restart game choice
    else:
        break

def hangman(): #define a hangman function for game run
    word=["lion","moon","sun","butterfly"] #make words list for use random function 
    word = random.choice(word) 
    turn = 6
    guessmade = ''
    valid_entry = set("abcdefghijklmnopqrstuvwxyz") #set use for lower letters

    while turn > 0: #while use for turn (whole the program run on turn)
        main_word = ""
        # missed = 0

        for letter in word: 
            if letter in guessmade:
                main_word = main_word + letter
            else:
                main_word = main_word + "_ "

        if main_word == word: #when word qual to main word then print you win
            print(main_word) 
            print("YOU WIN !!")
            restart_game()

        print("Write the right letter", main_word)
        guess = input() #print main word on correct postion 

        if guess in valid_entry:
            guessmade = guessmade + guess
        else:
            print("enter valid letters \n")
            guess=input()

        if guess not in word: #if command use for hangman print acc to turns if you are enter wrong letter then you loss turns one by one
            turn = turn-1
            print(turn) 
            print("-------------------") # here,start draw hangman 
            print("|                  |") 
            print("|                  ") 
            print("|                  ")
            print("|                  ")
            print("|                  ")
            print("|                  ")
            print("|                  ")
            print("|                  ")
            print("|                  ")
            print("|                  ")
            print("|                  ")
            print("-------------------")

            if turn == 5:
                print(turn)
                print("-------------------")
                print("|                  |") 
                print("|                  o") 
                print("|                  ")
                print("|                  ")
                print("|                  ")
                print("|                  ")
                print("|                   ")
                print("|                  ")
                print("|                  ")
                print("|                  ")
                print("|                  ")
                print("-------------------")
            if turn == 4:
                print(turn)
                print("-------------------")
                print("|                  |") 
                print("|                  o") 
                print("|                  |")
                print("|                  ")
                print("|                   ")
                print("|                   ")
                print("|                   ")
                print("|                  ")
                print("|                  ")
                print("|                  ")
                print("|                  ")
                print("-------------------")
            if turn == 3:
                print(turn)
                print("-------------------")
                print("|                  |") 
                print("|                  o") 
                print("|                  |")
                print("|                 /| ")
                print("|                   ")
                print("|                   ")
                print("|                   ")
                print("|                  ")
                print("|                  ")
                print("|                  ")
                print("|                  ")
                print("-------------------")
            if turn == 2:
                print(turn)
                print("-------------------")
                print("|                  |") 
                print("|                  o") 
                print("|                  |")
                print("|                 /|\ ")
                print("|                  ")
                print("|                 ")
                print("|                  ")
                print("|                  ")
                print("|                   ")
                print("|                  ")
                print("|                  ")
                print("|                  ")
                print("|                  ")
                print("-------------------")
            if turn == 1:
                print(turn)
                print("-------------------")
                print("|                  |") 
                print("|                  o") 
                print("|                  |")
                print("|                 /|\ ")
                print("|                  |")
                print("|                 /")
                print("|                   ")
                print("|                  ")
                print("|                   ")
                print("|                  ")
                print("|                  ")
                print("|                  ")
                print("|                  ")
                print("-------------------")
            if turn == 0: # here,finish hangman pic if your turn 0 then you loose game
                print(turn)
                print("-------------------")
                print("|                  |") 
                print("|                  o") 
                print("|                  |")
                print("|                 /|\ ")
                print("|                  |")
                print("|                 / \ ")
                print("|                  ")
                print("|                  ")
                print("|                   ")
                print("|                  ")
                print("|                  ")
                print("|                  ")
                print("|                  ")
                print("-------------------")
                print ("YOU LOOSE THE GAME")
                restart_game()

print ("Welcome to the Hangman Game")
print("*****************************")
a = input("Please enter your name: \n") # input player name and print 
print(a) 
print("Hello my friend "+ a , ", Time to play game")
time.sleep(1) #wait 1 second
hangman() # now call the define function hangman

restart_game()

print("Thankyou for Playing")
