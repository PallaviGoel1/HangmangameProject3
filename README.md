
# HANGMAN GAME
Hangman is a popular word puzzle game among kids. In this game, the player needs to guess the correct 
word based on the number of letters. At the start of the game, the player gets information as to the 
number of letters there are in the word and the hangman picture starts to draw on each incorrect guess.
And after certain incorrect guesses, a so-called man is hanged in the picture and the game ends with a loss.
If a player manages to guess the word correctly, it's a win. 

![hangmanmediaimage](/images/mediascreen.png)

## Features
This is an app to play a word game for a single player. Player has possibility to select the level for the game and repeat the game as many numbers of times.

# Flowchart
The flowchart for this project is created with the help from MS Excel:
![hangmancodeflowchart](/images/flowchart.png)

## Welcome Screen
At the start of game, welcome screen appears for xxx seconds and
after that directly jumps to instructions screen

![welcomescreen](/images/welcomescreen.png)

# Game Instructions
On this screen step by step instructions are mentioned for the player to understand every detail could be required to understand during the game

![Howtoplayimage](/images/howtoplay.png)

# Start Screen
Here player will be asked to enter the name and to select the level of the game, player wants to play with

![startscreenimage](/images/startgame.png)

## In the Game
As soon player choose to start (or restart the game), this screen will show up which is having a hidden word for player to guess. Only known here is the length of word

![Gamescreenimage](/images/gamescreen.png)

## End of Game
The game will end when player wins or loses. At the end of game, player will be asked if he/she wants to play again. If player chooses to restart the game, start game screen will pop up else app will close with thanks message

![playerwinimage](/images/wingame.png)

![Playerlooseimage](/images/lossgame.png)

# Future Roadmap
Though the app is complete and functioning smoothly, there are still few improvement/enhancements can be added later. Few of them are:\
1- More precise definition of different levels can be added\
2- Words list can be linked to a dictionary so that wider range of words could be available for user to guess from\
3- Number of wins and looses can be counted and added to screen every time game ends\
4- Historical records can be displayed\
5- User registration process can be included\
 

# Technologies Used
Following tools and technologies are used for this project:\    
    Language: Python\
    Version Control: GitHub\
    Coding/Debugging: Codeanywhere\
    Deployment: Heroku\

## Deployment
Deployment of this project is done via Heroku. Steps followed are as follows:\
    1- Ensure that latest code changes are pushed to GitHub repository\
    2- Login to Heroku\
    3- Click on “Create New App”\
    4- Choose a unique name for the app and the region\
    5- Add build packs- Python and Nodejs\
    6- Go to 'Deploy' tab\
    7- Select GitHub as deployment method\
    8- Click connect\
    9- Enter GitHub repository name and search\
    10- Click connect\
    11- Click on deploy branch\
    12- Click on view app\
    13- App opened in new screen (https://hangman-pp03-fbf38e318ccb.herokuapp.com/)

# Quality Checks
I tried to perform thorough testing on this from various perspectives to ensure that final product would be a quality app. Some highlights from testing are:

## Validator Tests
All the code parts have been tested through in-built validator in IDE (codeanywhere) and passed the test after few fixes. Files with major code are:\
    1  Run.py\
    2  Word_1.py

## Functional Tests
The flow of the code with various combinations of valid/invalid values has been tested. All test passed at the end and code is working as expected.

## GUI Tests
Many tests were performed from the user interface experience perspective and after few fixes, tests are passed.

## Lighthouse Tests

Lighthouse application tests are here for this app

![performanceandaccessibilityresult](/images/lighthouse.png)

## Bugs
Few issues were noted during testing and could manage to fix all of those before submitting the final app. Few of those are here with respective fixes:\
    1- After entering 'n' at restart query, game was not ending: Exit() function was not placed correctly\
    2- Hangman picture was not placed and visible correctly: Fixed some special characters in the code\
    3- Errors in validator noticed: Extra spaces and length of code in line were causing this

## Credits
I fetched help for coding from tutorial provided by Code Institute, W3 Schools, and Slack community.
















































































































