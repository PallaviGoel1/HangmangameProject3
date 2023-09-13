# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
#import wordsforhangman

def hangman():
    
    # word = random.choice(wordsforhangman.word_choice)
    word=["lion","moon","sun","butterfly"]
    word = random.choice(word)
    turn = 6
    guessmade = ''
    valid_entry = set("abcdefghijklmnopqrstuvwxyz")

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

        if guess not in word:
            turn = turn-1
            print(turn) 
            print("-------------------")
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
            if turn == 0:
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
a = input("Your name plz : ")
print(a) 
hangman()

print("If You want to restart the game")
ans = input("Enter y/n: ")
