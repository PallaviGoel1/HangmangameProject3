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
    print(Fore.CYAN + " Would you like to play again?\n")
    ans = input(Fore.CYAN + " If Yes, Press 'y' else 'n: ")
    if ans == "y":
        hangman()
    elif ans == "n":
        print(Fore.BLUE + "***********************************************\n")
        print(" Thanks for Playing!\n")
        print(Fore.BLUE + "***********************************************\n")
        exit()
    else:
        print(Fore.BLUE + "\n *Sorry, Incorrect Input. Try again please\n")
        restart_game()


# function to run the game
def hangman():
    word = get_word()
    turn = 6
    guessmade = ''
    # Loop to validate input and design hangman accordingly
    while turn > 0:
        main_word = ""
        for letter in word:
            if letter in guessmade:
                main_word = main_word + letter
            else:
                main_word = main_word + "_ "

        # Declare win when word is complete
        if main_word == word:
            print(Fore.GREEN + "******************************************\n")
            print(" Hurray, YOU WON !!\n")
            print("--------------", word, "-------------- was the answer\n")
            print(Fore.GREEN + "******************************************\n")
            time.sleep(1)
            restart_game()

        guess = check_letter(main_word)
        guessmade = guessmade + guess

        # Reduce turn counter by 1 on each wrong input and print hangman
        if guess not in word:
            turn = turn-1
            if turn == 5:
                print(" Number of wrong attempts left: ", turn)
                print(Fore.GREEN + "-------------------")
                print(Fore.GREEN + "|                  |")
                print(Fore.GREEN + "|                  o")
                print(Fore.GREEN + "|                   ")
                print(Fore.GREEN + "|                   ")
                print(Fore.GREEN + "|                   ")
                print(Fore.GREEN + "|                   ")
                print(Fore.GREEN + "|                   ")
                print(Fore.GREEN + "|                   ")
                print(Fore.GREEN + "--------------------")
            if turn == 4:
                print(" Number of wrong attempts left: ", turn)
                print(Fore.GREEN + "-------------------")
                print(Fore.GREEN + "|                  |")
                print(Fore.GREEN + "|                  o")
                print(Fore.GREEN + "|                  |")
                print(Fore.GREEN + "|                   ")
                print(Fore.GREEN + "|                   ")
                print(Fore.GREEN + "|                   ")
                print(Fore.GREEN + "|                   ")
                print(Fore.GREEN + "|                  ")
                print(Fore.GREEN + "-------------------")
            if turn == 3:
                print(" Number of wrong attempts left: ", turn)
                print(Fore.GREEN + "-------------------")
                print(Fore.GREEN + "|                  |")
                print(Fore.GREEN + "|                  o")
                print(Fore.GREEN + "|                  |")
                print(Fore.GREEN + "|                / |")
                print(Fore.GREEN + "|                   ")
                print(Fore.GREEN + "|                   ")
                print(Fore.GREEN + "|                   ")
                print(Fore.GREEN + "|                  ")
                print(Fore.GREEN + "-------------------")
            if turn == 2:
                print(" Number of wrong attempts left: ", turn)
                print(Fore.GREEN + "-------------------")
                print(Fore.GREEN + "|                  |")
                print(Fore.GREEN + "|                  o")
                print(Fore.GREEN + "|                  |")
                str = r"\ "
                print(Fore.GREEN + "|                / |", Fore.GREEN + str)
                print(Fore.GREEN + "|                  ")
                print(Fore.GREEN + "|                 ")
                print(Fore.GREEN + "|                  ")
                print(Fore.GREEN + "|                  ")
                print(Fore.GREEN + "|                   ")
                print(Fore.GREEN + "|                  ")
                print(Fore.GREEN + "-------------------")
            if turn == 1:
                print(" Number of wrong attempts left: ", turn)
                print(Fore.GREEN + "-------------------")
                print(Fore.GREEN + "|                  |")
                print(Fore.GREEN + "|                  o")
                print(Fore.GREEN + "|                  |")
                str = r"\ "
                print(Fore.GREEN + "|                / |", Fore.GREEN + str)
                print(Fore.GREEN + "|                  |")
                print(Fore.GREEN + "|                /  ")
                print(Fore.GREEN + "|                   ")
                print(Fore.GREEN + "|                  ")
                print(Fore.GREEN + "|                   ")
                print(Fore.GREEN + "|                  ")
                print(Fore.GREEN + "-------------------")
            # Max limit for wrong inputs reached and player lost the game
            if turn == 0:
                print(" Number of wrong attempts left: ", turn)
                print(Fore.GREEN + "-------------------")
                print(Fore.GREEN + "|                   |")
                print(Fore.GREEN + "|                   o")
                print(Fore.GREEN + "|                   |")
                str = r"\ "
                print(Fore.GREEN + "|                 / |", Fore.GREEN + str)
                print(Fore.GREEN + "|                   |")
                print(Fore.GREEN + "|                 /  ", Fore.GREEN + str)
                print(Fore.GREEN + "|                  ")
                print(Fore.GREEN + "|                  ")
                print(Fore.GREEN + "|                   ")
                print(Fore.GREEN + "|                  ")
                print(Fore.GREEN + "-------------------")
                print("***************************************************\n")
                str = " SORRY, YOU LOST THE GAME! Better "
                print(Fore.BLUE + str, Fore.BLUE + "luck next time!\n")
                print("***************************************************\n")
                str = "------------------"
                str1 = str + " was the answer"
                print(Fore.BLUE + str, word, Fore.BLUE + str1)
                print("\n")
                restart_game()


# Main function to start the game
def main():
    show_message()
    name = input("\n Please enter your name: ")
    print("\n Hello my friend " + name, ", Let's start the game!\n")
    print(Fore.CYAN + "\n************************************************\n")
    time.sleep(1)
    hangman()


# Validate input for the word
def check_letter(the_word):
    valid_entry = set("abcdefghijklmnopqrstuvwxyz")
    val_in = 0
    while val_in == 0:
        print(Fore.WHITE + "\n Write a letter for the word ", the_word)
        guess = input()
        if guess in valid_entry:
            val_in = 1
            return guess
        else:
            print(Fore.RED + " Please enter a valid input! \n")
            print(" Valid input are: abcdefghijklmnopqrstuvwxyz")


# Select random word from the list
def get_word():
    valid_input = set("123")
    val_in = 0
    # Check if level value input is correct
    while val_in == 0:
        g_lvl = input(" Choose a game level- 1 (easy), 2 (medium), 3 (hard): ")
        if g_lvl in valid_input:
            lvl = int(g_lvl)
            val_in = 1
        else:
            print("Please enter valid input\n")
    # Select word according to level
    if lvl == 1:
        word = random.choice(word_1.word_list_1)
        return word
    elif lvl == 2:
        word = random.choice(word_1.word_list_2)
        return word
    else:
        word = random.choice(word_1.word_list_3)
        return word


# Welcome screen of the program
def show_message():
    print(Fore.GREEN + "    Welcome to the Hangman Game!")
    print("*************************************************\n")
    print("-------------------------------------------------\n")
    print("-------------------")
    print("|                   |")
    print("|                   o")
    print("|                   |")
    str = r"\ "
    print("|                 / |", str)
    print("|                   |")
    print("|                 /  ", str)
    print("|                  ")
    print("|                  ")
    print("|                   ")
    print("|                  ")
    print("-------------------")
    time.sleep(2)
    # imitialalize colorama
    cl.init()
    # clear the terminal screen
    print(cl.ansi.clear_screen())
    # Game instructions for the player
    print(Fore.YELLOW + "\n------------------ HOW TO PLAY ------------------")
    str = " 1- Start the game by entering your name "
    print(Fore.YELLOW + str, Fore.YELLOW + "and select level\n")
    str = " 2- A hidden word will be displayed"
    print(Fore.YELLOW + str, Fore.YELLOW + "as a sequence of '_'\n")
    str = " 3- Number of letters in the word are"
    print(Fore.YELLOW + str, Fore.YELLOW + "same as number of '_'\n")
    str = " 4- You need to guess the word"
    print(Fore.YELLOW + str, Fore.YELLOW + "and enter a letter of that\n")
    str = " 5- (Please use small letters) And"
    print(Fore.YELLOW + str, Fore.YELLOW + "press the enter key\n")
    str = " 6- If the letter is in the word, respective '_' gets replaced"
    print(Fore.YELLOW + str, Fore.YELLOW + "with that letter in hidden word\n")
    str = " 7- If letter is not in the word,"
    print(Fore.YELLOW + str, Fore.YELLOW + "drawing for hangman starts\n")
    print(Fore.YELLOW + " 8- Hangman drawing continues on every wrong input\n")
    str = " 9- If player manage to guess correct word with less than 6 wrong"
    print(Fore.YELLOW + str, Fore.YELLOW + " attempts, player wins\n")
    str = " 10- If it's been 6 wrong attempts, Hangman drawing completes"
    print(Fore.YELLOW + str, Fore.YELLOW + " and player loses the game")
    print(Fore.YELLOW + "------------------------------------------------\n")
    start = input(" Press ENTER to start the game OR q to quit: ")
    if start == "q":
        print("\n Thanks for trying, hope we will see you back!\n")
        exit()
    print(Fore.CYAN + "--------------------------------------------------\n")


print("******************************************************************\n")


main()
