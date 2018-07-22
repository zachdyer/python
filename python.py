import random
import os

def revealnumber(number, guess):
  print "I was thinking of the number " + str(number) + " and you said " + guess 
  if number == int(guess):
    print name + " WINS!!!"
  else:
    print "Python WINS!!!"
    
def score():
  global pythonscore, playerscore, name
  print "SCORE"
  print "Python: " + str(pythonscore) + "      " + name + ": " + str(playerscore)

def guessgame():
  global playerscore
  global pythonscore
  print "If you can guess the number I'm thinking of between 1 and 5 you win. If you get it wrong you lose."
  number = random.randint(1,5)
  guess = raw_input("What number am I thinking of?")
  if number == int(guess):
    playerscore = playerscore + 1
    revealnumber(number, guess)
    score()
    print "Perfect! You win!!! *Final Fantasy Fanvar music plays*"
  else :
    pythonscore = pythonscore + 1
    revealnumber(number, guess)
    score()
    again = raw_input("Would you like to play again?")
    if again == "yes":
      guessgame()
    elif again == "no":
      score()
      print "Thanks for playing! Goodbye, " + name
      raw_input("Press enter to continue...")
      init()
    else:
      print "I only understand yes or no thanks to my creator."
      init()

def rolldice():
  
  def score(player, python):
    os.system("clear")
    print "You rolled a " + str(player) + " and I rolled a " + str(python) + "."
    raw_input()
  
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
    raw_input("Press enter to continue...")
    rolldice()
  elif input == "2":
    player = random.randint(1,6)
    python = random.randint(1,6)
    if player == python:
      score(player, python)
      print "We both rolled a " + str(player) + ". You tied me."
      raw_input()
      rolldice()
    elif player > python:
      score(player, python)
      print "You win!"
      raw_input()
      rolldice()
    else:
      score(player, python)
      print "I win!"
      raw_input()
      rolldice()
  elif input == "3":
    os.system("clear")
    init()
  else:
    rolldice()
    
def play():
  global game
  global pythonscore 
  global playerscore
  
  os.system("clear")
  if game == "yes":
    guessgame()
  elif game == "no":
    print "And you wonder why you have no friends."
    return
  else:
    print "I only understand yes or no. I'm pretty dumb thanks to my creator. So if i make a mistake it's his fault."
    loop()
    
def init():
  global game
  
  os.system("clear")
  
  print("What would you like to do, " + name + "?")
  print("1. Play the guessing game")
  print("2. Roll dice")
  print("3. Quit")
  game = raw_input();
  if game == "1":
    guessgame()
  elif game == "2":
    rolldice()
  elif game == "3":
    print "And you wonder why you have no friends."
  else:
    print "I only understand yes or no. I'm pretty dumb thanks to my creator. So if i make a mistake it's his fault."
    init()

os.system("clear")
print "Hello. My name is Python."
name = raw_input("What is your name?") 
print name + "! That is a beautful name. I'll remember that."
raw_input()
game = None 
pythonscore = 0
playerscore = 0
init()

