import os  # credit to stackoverflow.com
import random  # generates a random number
import time  # This function use for handle time & date
import word_1  # word list .py file
import colorama  # print colored terminal text
import colorama as cl  # cl (clear screen function)
from colorama import Fore  # change the foreground color

colorama.init(autoreset=True)


# Ask if user want to play again
def restart_game():
    print("**************************************\n")
    print(Fore.CYAN + "Would you like to play again?\n")
    print(Fore.CYAN + "If Yes, Press 'y' else 'n': ")
    ans = input()
    if ans == "y":
        hangman()
    elif ans == "n":
        print(Fore.BLUE + "**************************************\n")
        print("Thanks for Playing!\n")
        print(Fore.BLUE + "***************************************\n")
        exit()
    else:
        print(Fore.BLUE + "\n*Sorry, Incorrect Input. Try again please\n")
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
            print(Fore.GREEN + "Hurray, YOU WON !!\n")
            print("**************************************\n")
            time.sleep(1)
            restart_game()

        # print main word on correct postion
        print("\nWrite a letter for the word", main_word)
        guess = input()

        if guess in valid_entry:
            guessmade = guessmade + guess
        else:
            print(Fore.RED + "enter valid letters \n")
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
                print(Fore.RED + "|                / |", Fore.RED + str)
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
                print(Fore.RED + "|                / |", Fore.RED + str)
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
                print(Fore.RED + "|                 / |", Fore.RED + str)
                print(Fore.RED + "|                   |")
                print(Fore.RED + "|                 /    ", Fore.RED + str)
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
    show_message()
    print("\n")
    print("\n**************************************\n")
    a = input(Fore.CYAN + "Please enter your name: ")

    print("Hello my friend "+a " Let's start the game!\n")
    print(Fore.CYAN + "Number of wrong attempts: 6\n")
    print("\n**************************************\n")
    time.sleep(1)
    hangman()


# Select random word from word_1 list
def get_word():
    lvl = 1
    if lvl == 1:
        word = random.choice(word_1.word_list_1)
        return word


# Starting message of the program
def show_message():
    print(Fore.GREEN + "    Welcome to the Hangman Game!")
    print("**************************************\n")
    print("---------------------------------------\n")
    print(Fore.RED + "-------------------")
    print(Fore.RED + "|                   |")
    print(Fore.RED + "|                   o")
    print(Fore.RED + "|                   |")
    str = r"\ "
    print(Fore.RED + "|                 / |", Fore.RED + str)
    print(Fore.RED + "|                   |")
    print(Fore.RED + "|                 /    ", Fore.RED + str)
    print(Fore.RED + "|                  ")
    print(Fore.RED + "|                  ")
    print(Fore.RED + "|                   ")
    print(Fore.RED + "|                  ")
    print(Fore.RED + "-------------------")
    time.sleep(5)
    # imitialalize colorama
    cl.init()
    # clear the terminal screen
    print(cl.ansi.clear_screen())
    print(Fore.YELLOW + "------------- HOW TO PLAY-------------\n")
    print("---------------------------------------\n")
    print(Fore.YELLOW + "1-Start the game with your enter name.\n")
    str = "2-A hidden word will be displayed"
    print(Fore.YELLOW + str, Fore.YELLOW + "as a sequence of '_'.\n")
    str = "3-Number of letters in the word are"
    print(Fore.YELLOW + str, Fore.YELLOW + "same as number of '_'.\n")
    str = "4-You need to guess the word"
    print(Fore.YELLOW + str, Fore.YELLOW + "and enter a letter of that.\n")
    str = "5-(Please use small letters) And"
    print(Fore.YELLOW + str, Fore.YELLOW + "press the enter key.\n")
    str = "6 - If the letter is in the word, respective '_' gets replaced"
    print(Fore.YELLOW + str, Fore.YELLOW + "with that letter in hidden word\n")
    str = "7-If letter is not in the word,"
    print(Fore.YELLOW + str, Fore.YELLOW + "drawing for hangman starts.\n")
    print(Fore.YELLOW + "8- Hangman drawing continues on every wrong input\n")
    str = "9 - If player manage to guess correct word with less than 6 wrong"
    print(Fore.YELLOW + str, Fore.YELLOW + " attempts, player wins\n")
    str = "10 - If it's been 6 wrong attempts, Hangman drawing completes"
    print(Fore.YELLOW + str, Fore.YELLOW + " and player loses the game")
    time.sleep(5)
    # imitialalize colorama
    cl.init()
    # clear the terminal screen
    print(cl.ansi.clear_screen())


print("**************************************\n")


main()
