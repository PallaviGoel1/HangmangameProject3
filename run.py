import os
import random
import time
import word_1
# import colorama
import colorama as cl
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
                print(Fore.RED + "-------------------")
                print(Fore.RED + "|                  |")
                print(Fore.RED + "|                  o")
                print(Fore.RED + "|                   ")
                print(Fore.RED + "|                   ")
                print(Fore.RED + "|                   ")
                print(Fore.RED + "|                   ")
                print(Fore.RED + "|                   ")
                print(Fore.RED + "|                   ")
                print(Fore.RED + "--------------------")
            if turn == 4:
                print("Number of wrong attempts left: ", turn)
                print(Fore.RED + "-------------------")
                print(Fore.RED + "|                  |")
                print(Fore.RED + "|                  o")
                print(Fore.RED + "|                  |")
                print(Fore.RED + "|                   ")
                print(Fore.RED + "|                   ")
                print(Fore.RED + "|                   ")
                print(Fore.RED + "|                   ")
                print(Fore.RED + "|                  ")
                print(Fore.RED + "-------------------")
            if turn == 3:
                print("Number of wrong attempts left: ", turn)
                print(Fore.RED + "-------------------")
                print(Fore.RED + "|                  |")
                print(Fore.RED + "|                  o")
                print(Fore.RED + "|                  |")
                print(Fore.RED + "|                / |")
                print(Fore.RED + "|                   ")
                print(Fore.RED + "|                   ")
                print(Fore.RED + "|                   ")
                print(Fore.RED + "|                  ")
                print(Fore.RED + "-------------------")
            if turn == 2:
                print("Number of wrong attempts left: ", turn)
                print(Fore.RED + "-------------------")
                print(Fore.RED + "|                  |")
                print(Fore.RED + "|                  o")
                print(Fore.RED + "|                  |")
                str = r"\ "
                print(Fore.RED + "|                / |", str)
                print(Fore.RED + "|                  ")
                print(Fore.RED + "|                 ")
                print(Fore.RED + "|                  ")
                print(Fore.RED + "|                  ")
                print(Fore.RED + "|                   ")
                print(Fore.RED + "|                  ")
                print(Fore.RED + "-------------------")
            if turn == 1:
                print("Number of wrong attempts left: ", turn)
                print(Fore.RED + "-------------------")
                print(Fore.RED + "|                  |")
                print(Fore.RED + "|                  o")
                print(Fore.RED + "|                  |")
                str = r"\ "
                print(Fore.RED + "|                / |", str)
                print(Fore.RED + "|                  |")
                print(Fore.RED + "|                /  ")
                print(Fore.RED + "|                   ")
                print(Fore.RED + "|                  ")
                print(Fore.RED + "|                   ")
                print(Fore.RED + "|                  ")
                print(Fore.RED + "-------------------")
            # here,finish hangman pic if your turn 0 then you loose game
            if turn == 0:
                print("Number of wrong attempts left: ", turn)
                print(Fore.RED + "-------------------")
                print(Fore.RED + "|                   |")
                print(Fore.RED + "|                   o")
                print(Fore.RED + "|                   |")
                str = r"\ "
                print(Fore.RED + "|                 / |", str)
                print(Fore.RED + "|                   |")
                print(Fore.RED + "|                 /    ", str)
                print(Fore.RED + "|                  ")
                print(Fore.RED + "|                  ")
                print(Fore.RED + "|                   ")
                print(Fore.RED + "|                  ")
                print(Fore.RED + "-------------------")
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


# Select random word from word_1 list
def get_word():
    lvl = 1
    if lvl == 1:
        word = random.choice(word_1.word_list_1)
        return word


# Starting message of the program
print("**************************************\n")
print(Fore.RED + "    Welcome to the Hangman Game!")
print("**************************************\n")
print("---------------------------------------\n")
print(Fore.RED + "-------------------")
print(Fore.RED + "|                   |")
print(Fore.RED + "|                   o")
print(Fore.RED + "|                   |")
str = r"\ "
print(Fore.RED + "|                 / |", str)
print(Fore.RED + "|                   |")
print(Fore.RED + "|                 /    ", str)
print(Fore.RED + "|                  ")
print(Fore.RED + "|                  ")
print(Fore.RED + "|                   ")
print(Fore.RED + "|                  ")
print(Fore.RED + "-------------------")
time.sleep(1)
# imitialalize colorama
cl.init()
# clear the terminal screen
print(cl.ansi.clear_screen())
print(Fore.RED + "------------- HOW TO PLAY-------------\n")
print("---------------------------------------\n")
print(Fore.YELLOW + " 1-Start the game with your enter name.\n")
print("2-You need to guess the word one at atime.\n")
print("3-Enter the small letter and press the enter key.\n")
print("4-If Your letter is right,it will show on the correct place.\n")
print("5-If your letter is wrong, Hangman will gradually show.\n")
print("6-keep write until the correct word or you exit the game.\n")
time.sleep(1)
# imitialalize colorama
cl.init()
# clear the terminal screen
print(cl.ansi.clear_screen())
main()
