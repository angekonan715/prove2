# Prove2 asignment : Hilo Game
## Overview

Hilo is a game in which the player guesses 

if the next card drawn by the dealer will be

higher or lower than the previous one.

Points are won or lost based on whether 

or not the player guessed correctly.

## Game Description

* The player starts the game with 300 points.
* Individual cards are represented as a number from 1 to 13.
* The current card is displayed.
* The player guesses if the next one will be higher or lower.
* The the next card is displayed.
* The player earns 100 points if they guessed correctly.
* The player loses 75 points if they guessed incorrectly.
* If a player reaches 0 points the game is over.
* If a player has more than 0 points they decide if they want to keep playing.
* If a player decides not to play again the game is over.

## Objects

The following object names were created to program our game.
## 1. Cards Object
Cards object can be found in cards.py file. 
### Responsabilities
Its main responsibilties are to :
- add individual card to a list 
- generate a random card named current_card from the list of cards
- generate a random card named next_card from the list of cards

## 2. Player Object
Players object can be found in playingGame.py file
###  Attribute
- points (int)
- score (int)
- is_playing (Boolean )
- is_guess (boolean )

###  Methods
- input_guess : Ask the user to guess either the current card is higher/lower than the next card
- keep_playing : Ask teh user if he deires to play again or not
- play_game : run the game

#### Note 
I also made a file called __main__.py that import the player object , instantiate and run the gain.

:+1: Thanks You For Reading Me
