import defs
import os
import random

class DiceRoller():
  
  player_score = 0
  python_score = 0
  
  def __init__(self):
    self.main_menu()
  
  def main_menu(self):
    os.system("clear")
    print "Welcome to DiceRoller!"
    print "1. 1 player roll a 6 sided die"
    print "2. 2 player roll a 6 sided die against Python."
    print "3. Quit"
    input = raw_input()
    if input == "1":
      os.system("clear")
      roll = random.randint(1,6)
      print("You rolled a " + str(roll))
      defs.confirm()
      self.main_menu()
    elif input == "2":
      self.play_python()
    elif input == "3":
      defs.main_menu()
    else:
      self.main_menu()
      
  def play_python(self):
    os.system("clear")
    player = random.randint(1,6)
    python = random.randint(1,6)
    print "You rolled a " + str(player) + " and I rolled a " + str(python) + "."
    if player == python:
      print "You tied me."
      self.score()
      self.again()
    elif player > python:
      self.player_score = self.player_score + 1
      print "You win!"
      self.score()
      self.again()
    else:
      self.python_score = self.python_score + 1
      print "I win!"
      self.score()
      self.again()
  
  def again(self):
    again = raw_input("Would you like to play again?")
    if again == "yes":
      self.play_python()
    elif again == "no":
      self.game_over()
      self.main_menu()
    else:
      print "I'm sorry but I only understand yes or no. It's not you it's me."
      self.again()
  
  def score(self):
    print "SCORE"
    print defs.read_name() + ": " + str(self.player_score) + "       Python: " + str(self.python_score)
    
  def game_over(self):
    if self.player_score == self.python_score:
      print "Thanks for playing. I guess we are evenly matched."
      defs.confirm()
    elif self.player_score > self.python_score:
      print "It's offical. You're better than me. But that's okay because I'll still be here assuming my creator doesn't screw it up."
      defs.confirm()
    else:
      print "See you later loser. Come back when you grow a pair."
      defs.confirm()