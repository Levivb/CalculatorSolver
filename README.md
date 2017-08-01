# Calculator: The Game Solver

## What is it?
A script to find the solutions of the puzzles in "Calculator: The Game"

## But... why?
During the summer holiday of 2017 my brother was playing "Calculator: The Game" on his phone ([iOS](https://itunes.apple.com/us/app/calculator-the-game/id1243055750?mt=8), [Android](https://play.google.com/store/apps/details?id=com.sm.calculateme)).
Soon after looking over his shoulder pretty much the whole family had this wicked game installed (which was no small feat given the tedious slow internet 2200 meters up in the mountains) and we were all all to busy solving the puzzles.
Instead of choosing the path of least resistance and just bashing all possible combinations on the screen in order to proceed to the next level, I took it as a challenge to make an automated solver.


## And so
Implementation went pretty smooth. Due to my brother-in-law leaping way ahead of me ingame I knew which buttons I would come across as I slayed (read: mindlessly bashed the script) puzzle after puzzle.
The biggest challenge was due to the "save button"... Not only had I keep track of some random number which the script might cross at any point in walking through each possible combination, the storing of the number could be executed as often as one might want, without it costing a move. Which caused a real issue in the initial setup. In the end, I'm not to unpleased with the solution (by using an extra `combinateWithStore` function), but it does make the code taste somewhat like spaghetti. Good thing everyone likes [Italian](https://www.youtube.com/watch?v=JAFQFvSPhQ8).

## What is it not?
A well written, bugfree, input sanitized, world hunger solution generator...
Seriously, it's hurdled with bugs, but as my challenge completed after finishing every single puzzle in the game solely by using this script, my job was done.
Negative numbers will mess up the script sometimes and the portals near the end of the game are not very well tested. I fixed what I encountered, but no doubt not all crashes are fixed.
Also... I clearly don't understand the scoping in python as I couldn't get the code in `libs/functions.py` to work while importing it in `__init__.py`. Didn't bother to look into it yet.

## Requirements
* python3: brew install python3.<br>
* Terminal: /Applications/Utilities/Terminal.app

## Usage
1. clone or download this project
1. open Terminal
1. cd to this directory
1. run `chmod u+x main.py`
1. run `./main.py` (or `python3 main.py` if you skipped previous step)
1. follow the onscreen instructions.

The solver consists of three main input parts:
1. The game: here you define the game parameters: start, goal, moves, portals and whether to show all solutions or break on first hit. Logically breaking on first hit is the fastest, but it's interesting to see the amount of solutions are possible even for puzzles with only 4 moves and 3 buttons.
1. The main menu: here you can choose whether you want to add a button (0), start solving (1) or exit (2).
1. The button menu: When choosing to add a button in the main menu you'll be shown a list of possible buttons. Choose the number of the button you want to add and enter the required value if needed.

## Disclaimer
I'm by no means very knowledgeable in python. I merily threw this piece of software together in 2 holiday days in order to understand python a bit more. I tried to keep responsibilities seperate and the code as dynamic as possible. Hence the string to class generation in `solver.py`, but I failed to get the automated imports of the actions classes in `solver.py` to work while also keeping the string to class generation functional. Mainly because I've no idea in which scope the dynamically imported modules end up and how to retrieve them.

## Author
[Levivb](https://github.com/Levivb)
