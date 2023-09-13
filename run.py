# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

def hangman():
    
    word = random.choice(wordsforhangman.word_choice)
    turn = 7
    guessmade = ''
    valid_entry = set("abcdefghijklmnopqrstuvwxyz")


print("Welcome to the Hangman Game")
print("*****************************")
a = input("Your name plz : ")
print( a ) 

print("If You want to restart the game")
ans = input("Enter y/n: ")
