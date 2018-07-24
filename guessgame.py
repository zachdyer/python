import os
import random
import defs

class GuessGame():
  
  player_score = 0
  python_score = 0
  player_roll = None
  python_roll = None
  
  def __init__(self):
    self.play()
  
  def play(self):
    global name
    os.system("clear")
    print "If you can guess the number I'm thinking of between 1 and 5 you win."
    print "If you get it wrong you lose."
    self.python_roll = random.randint(1,5)
    self.player_roll = raw_input("What number am I thinking of?")
    if defs.is_number(self.player_roll) == False:
      print self.player_roll + " is not a number between 1 and 5. Is this a troll?"
      self.play()
    if self.python_roll == int(self.player_roll):
      self.player_score = self.player_score + 1
      self.winner()
      self.score()
      self.again()
    else :
      self.python_score = self.python_score + 1
      self.winner()
      self.score()
      self.again()
  
  def winner(self):
    global name
    os.system("clear")
    print "I was thinking of the number " + str(self.python_roll) + " and you said " + self.player_roll 
    if self.python_roll == int(self.player_roll):
      print name + " wins!"
    else:
      print "I win!"
      
  def score(self):
    global name
    print "SCORE"
    print defs.read_name() + ": " + str(self.player_score) + "        Python: " + str(self.python_score)
    
  def again(self):
    again = raw_input("Would you like to play again?")
    if again == "yes":
      os.system("clear")
      self.play()
    elif again == "no":
      os.system("clear")
      self.score()
      print "Thanks for playing! Goodbye, " + defs.read_name()
      if self.player_score == self.python_score:
        print "We tied " + str(self.player_score) + " " + str(self.python_score) + "! You are great competition!"
      elif self.python_score > self.player_score:
        print "Just for the record I win " + str(self.python_score) + " to " + str(self.player_score) + "." 
        print "Which means I'm better than you. And thanks to my creator I talk shit like this."
      else:
        print "Somehow you beat me even though the odds are in my favor."
      defs.confirm()
      defs.main_menu()
    else:
      print "I only understand yes or no thanks to my all knowing creator"
      self.again()