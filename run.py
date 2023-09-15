import random
#import requirements.txt
#file =open("requirements.txt")
#lines= file.read()
#file.close()
#print(lines)

def hangman(): #define a hangman function for game run
    
    #word = random.choice(requirements.word_choice)
    word=["lion","moon","sun","butterfly"] #make words list for use random function 
    word = random.choice(word) 
    turn = 6
    guessmade = ''
    valid_entry = set("abcdefghijklmnopqrstuvwxyz") #set use for lower letters

    while turn > 0:
        main_word = ""
        # missed = 0

        for letter in word:
            if letter in guessmade:
                main_word = main_word + letter
            else:
                main_word = main_word + "_ "

        if main_word == word:
            print(main_word) 
            print("YOU WIN !!")
            break  

        print("Write the right letter", main_word)
        guess = input()

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

print ("Welcome to the Hangman Game")
print("*****************************")
a = input("Your name plz: \n") # input player name and print 
print(a) 
hangman() #call the define function hangman

print("If You want to restart the game")
ans = input("Enter y/n: \n") #there are choice to play game(restart)
if ans == "y":
    hangman() # again call function according to game play choice
else:
    print("Thankyou Player for Playing")