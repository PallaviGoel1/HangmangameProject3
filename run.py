import os
import random
import time
import word_1
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


# Ask if user want to play again
def restart_game():
    print("**************************************\n")
    print("Would you like to play again?\n")
    print("If Yes, Press 'y' else 'n': ")
    ans = input()
    if ans == "y":
        hangman()
    elif ans == "n":
        print("**************************************\n")
        print("Thanks for Playing!\n")
        print("***************************************\n")
        exit()
    else:
        print("\n*** Sorry, Incorrect Input. Try again please ***\n")
        restart_game()


# define a hangman function for game run
def hangman():
    # make words list according to different levels
    word = get_word()
    turn = 6
    guessmade = ''
    # define valid inputs
    valid_entry = set("abcdefghijklmnopqrstuvwxyz")
    # while use for turn (whole the program run on turn)
    while turn > 0:
        main_word = ""
        for letter in word:
            if letter in guessmade:
                main_word = main_word + letter
            else:
                main_word = main_word + "_ "

        # Declare win when word is complete
        if main_word == word:
            print(main_word)
            print("**************************************\n")
            print("Hurray, YOU WON !!\n")
            print("**************************************\n")
            time.sleep(1)
            restart_game()

        # print main word on correct postion
        print("\nWrite a letter for the word", main_word)
        guess = input()

        if guess in valid_entry:
            guessmade = guessmade + guess
        else:
            print("enter valid letters \n")
            guess = input()

        # Reduce turn if input is wrong and print hangman
        if guess not in word:
            turn = turn-1
            if turn == 5:
                print("Number of wrong attempts left: ", turn)
                print("-------------------")
                print("|                  |")
                print("|                  o")
                print("|                  ")
                print("|                  ")
                print("|                  ")
                print("|                  ")
                print("|                   ")
                print("|                  ")
                print("-------------------")
            if turn == 4:
                print("Number of wrong attempts left: ", turn)
                print("-------------------")
                print("|                  |")
                print("|                  o")
                print("|                  |")
                print("|                   ")
                print("|                   ")
                print("|                   ")
                print("|                   ")
                print("|                  ")
                print("-------------------")
            if turn == 3:
                print("Number of wrong attempts left: ", turn)
                print("-------------------")
                print("|                  |")
                print("|                  o")
                print("|                  |")
                print("|                / |")
                print("|                   ")
                print("|                   ")
                print("|                   ")
                print("|                  ")
                print("-------------------")
            if turn == 2:
                print("Number of wrong attempts left: ", turn)
                print("-------------------")
                print("|                  |")
                print("|                  o")
                print("|                  |")
                str = r"\ "
                print("|                / |", str)
                print("|                  ")
                print("|                 ")
                print("|                  ")
                print("|                  ")
                print("|                   ")
                print("|                  ")
                print("-------------------")
            if turn == 1:
                print("Number of wrong attempts left: ", turn)
                print("-------------------")
                print("|                  |")
                print("|                  o")
                print("|                  |")
                str = r"\ "
                print("|                / |", str)
                print("|                  |")
                print("|                /  ")
                print("|                   ")
                print("|                  ")
                print("|                   ")
                print("|                  ")
                print("-------------------")
            # here,finish hangman pic if your turn 0 then you loose game
            if turn == 0:
                print("Number of wrong attempts left: ", turn)
                print("-------------------")
                print("|                   |")
                print("|                   o")
                print("|                   |")
                str = r"\ "
                print("|                 / |", str)
                print("|                   |")
                print("|                 /    ", str)
                print("|                  ")
                print("|                  ")
                print("|                   ")
                print("|                  ")
                print("-------------------")
                print("**************************************\n")
                print("SORRY, YOU LOST THE GAME! Better luck next time!\n")
                print("**************************************\n")
                restart_game()


# Main function to start the game
def main():
    a = input("Please enter your name: ")
    print("\n**************************************\n")
    print("Hello my friend "+a, ", Let's start the game!\n")
    print("Number of wrong attempts: 6\n")
    time.sleep(1)
    hangman()


# Select random word from list according to different levels
def get_word():
    # word_list_1 = ["lion", "moon", "sun", "cake", "cave", "dark", "earth"]
    # r_word = random.choice(word_list_1)
    # word_list_2 = ["accuse", "cuddle", "careless", "butterfly",
    # "certificate"]
    # word_list_3 = ["abirritant", "aftershave", "cavitation",
    # ""]
    lvl = 1
    if lvl == 1:
        word = random.choice(word_1.word_list_1)
        return word


# Starting message of the program
print("Welcome to the Hangman Game!")
print("**************************************\n")
print("---------------------------------------\n")
print("------------- HOW TO PLAY-------------\n")
print("---------------------------------------\n")
print(Fore.BLUE + "1-Start the game with your enter name\n")
print(Fore.BLUE + "2-You need to guess the word one at a time\n")
print("3-Enter the letter and press the enter key\n")
print("4-If Your letter is right,Your letter will show on the correct place\n")
print("5-If your letter is wrong,Hangman visible and show,step by step\n")
print("6-keep write until the correct word or you exit the game\n")
main()
