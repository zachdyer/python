import random
import os

name = None

def init():
  global name
  os.system("clear")
  print "Hello. My name is Python."
  name = raw_input("What is your name?") 
  print name + "! That is a beautful name. I'll remember that."
  confirm()
  main_menu()

def main_menu():
  os.system("clear")
  print("What would you like to do, " + name + "? Enter the number of the option.")
  print("1. Play the guessing game")
  print("2. Roll dice")
  print("3. Quit")
  option = raw_input()
  if option == "1":
    guessgame = GuessGame()
    guessgame.play()
  elif option == "2":
    diceroller = DiceRoller()
    diceroller.main_menu()
  elif option == "3":
    print "And you wonder why you have no friends."
  else:
    print "I only understand yes or no. I'm pretty dumb thanks to my creator. So if i make a mistake it's his fault."
    main_menu()
    
def confirm():
  raw_input("Press enter to continue...")
  
def is_number(s):
  try:
    int(s)
    return True
  except ValueError:
    return False
    
class GuessGame():
  
  player_score = 0
  python_score = 0
  player_roll = None
  python_roll = None
  
  def play(self):
    global name
    print "If you can guess the number I'm thinking of between 1 and 5 you win."
    print "If you get it wrong you lose."
    self.python_roll = random.randint(1,5)
    self.player_roll = raw_input("What number am I thinking of?")
    if is_number(self.player_roll) == False:
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
    print name + ": " + str(self.player_score) + "        Python: " + str(self.python_score)
    
  def again(self):
    again = raw_input("Would you like to play again?")
    if again == "yes":
      self.play()
    elif again == "no":
      self.score()
      print "Thanks for playing! Goodbye, " + name
      if self.player_score == self.python_score:
        print "We tied " + str(self.player_score) + " " + str(self.python_score) + "! You are great competition!"
      elif self.python_score > self.player_score:
        print "Just for the record I win " + str(self.python_score) + " to " + str(self.player_score) + "." 
        print "Which means I'm better than you. And thanks to my creator I talk shit like this."
      else:
        print "Somehow you beat me even though the odds are in my favor."
      confirm()
      main_menu()
    else:
      print "I only understand yes or no thanks to my all knowing creator"
      self.again()
    
class DiceRoller():
  
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
      confirm()
      self.main_menu()
    elif input == "2":
      self.play_python()
    elif input == "3":
      main_menu()
    else:
      self.main_menu()
      
  def play_python(self):
    os.system("clear")
    player = random.randint(1,6)
    python = random.randint(1,6)
    print "You rolled a " + str(player) + " and I rolled a " + str(python) + "."
    confirm()
    if player == python:
      print "You tied me."
      confirm()
      self.main_menu()
    elif player > python:
      print "You win!"
      confirm()
      self.main_menu()
    else:
      print "I win!"
      confirm()
      self.main_menu()

init()