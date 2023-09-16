import random
import time


# Ask if user want to play again
def restart_game():
    str = """
    **************************************
    Would you like to play again?
    If Yes, Press 'y' else 'n': """
    print(str)
    ans = input()
    if ans == "y":
        hangman()
    elif ans == "n":
        str = """**************************************
        Thanks for Playing!
        ***************************************"""
        print(str)
        exit()
    else:
        print("\n*** Sorry, Incorrect Input. Try again please ***\n")
        restart_game()


# define a hangman function for game run
def hangman():
    # make words list according to different levels
    word_list_1 = ["lion", "moon", "sun", "butterfly"]
    word = random.choice(word_list_1)
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
            print("Number of attempts left: ", turn)
            print("-------------------")  # here,start draw hangman
            print("|                  |")
            print("|                  ")
            print("|                  ")
            print("|                  ")
            print("|                  ")
            print("|                  ")
            print("|                  ")
            print("|                  ")
            print("-------------------")

            if turn == 5:
                print("Number of attempts left: ", turn)
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
                print("Number of attempts left: ", turn)
                print("-------------------")
                print("|                  |")
                print("|                  o")
                print("|                  |")
                print("|                  ")
                print("|                   ")
                print("|                   ")
                print("|                   ")
                print("|                  ")
                print("-------------------")
            if turn == 3:
                print("Number of attempts left: ", turn)
                print("-------------------")
                print("|                  |")
                print("|                  o")
                print("|                  |")
                print("|                 /| ")
                print("|                   ")
                print("|                   ")
                print("|                   ")
                print("|                  ")
                print("-------------------")
            if turn == 2:
                print("Number of attempts left: ", turn)
                print("-------------------")
                print("|                  |")
                print("|                  o")
                print("|                  |")
                str = r"\ "
                print("|                 /|", str)
                print("|                  ")
                print("|                 ")
                print("|                  ")
                print("|                  ")
                print("|                   ")
                print("|                  ")
                print("-------------------")
            if turn == 1:
                print("Number of attempts left: ", turn)
                print("-------------------")
                print("|                  |")
                print("|                  o")
                print("|                  |")
                str = r"\ "
                print("|                 /|", str)
                print("|                  |")
                print("|                 /")
                print("|                   ")
                print("|                  ")
                print("|                   ")
                print("|                  ")
                print("-------------------")
            # here,finish hangman pic if your turn 0 then you loose game
            if turn == 0:
                print("Number of attempts left: ", turn)
                print("-------------------")
                print("|                  |")
                print("|                  o")
                print("|                  |")
                str = r"\ "
                print("|                 /|", str)
                print("|                  |")
                print("|                 / ", str)
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
    print("Number of attempts: 6\n")
    time.sleep(1)
    hangman()


# Starting message of the program
print("Welcome to the Hangman Game!")
print("**************************************\n")
main()
