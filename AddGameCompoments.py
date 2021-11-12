
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

from os import system
import random


class programNumbers:
    def __init__(self, number1, number2, number3, number4):
        self.number1 = number1
        self.number2 = number2
        self.number3 = number3
        self.number4 = number4

    def randomcard(self):
        card_points = ['A', 'K', 'Q', 'J', '2',
                       '3', '4', '5', '6', '7', '8', '9', '10']
        card_signs = ['H', 'C', 'D', 'S']
        random_point = random.choice(card_points)
        random_sign = random.choice(card_signs)
        random_card = random_point+random_sign
        return random_card

    def displayNumbers(self):
        print(self.number1, self.number2, self.number3, self.number4)

    def instruction(self):
        print("Memorize a card and I will make it disappear.")
        input("Please enter to continue.")

    def askQuestion(self):
        print("Did I remove the card you thought of?")

    def answerPlaye(self):
        answerplayer = input("Please enter Y/N:  ").upper()
        if answerplayer == "Y":
            print("I'm the best mind reader and I have just blown your mind!")
        else:
            print("Try again")


# keep playing until the user donst wnat to play anymore
while True:
    # create a new instance of the class
    new_game = programNumbers("4H", "8C", "10S", "AS")
    # display the numbers
    new_game.displayNumbers()
    # display the instructions
    new_game.instruction()

    num_ran1 = new_game.randomcard()
    num_ran2 = new_game.randomcard()
    num_ran3 = new_game.randomcard()

    firstnumbers2 = programNumbers(num_ran1, "4H", num_ran2, num_ran3)
    firstnumbers2.displayNumbers()
    firstnumbers2.askQuestion()
    firstnumbers2.answerPlaye()
    print('\n' * 2)
    # ask if the user wants to play again
    play_again = input("Do you want to play again? (Y/N): ").upper()
    if play_again == "Y":
        system("clear")
    else:
        print("Thank you for playing!")
        break
# end of the program