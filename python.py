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
  
def play():
  global game
  global pythonscore 
  global playerscore
  
  os.system("clear")
  if game == "yes":
    print "If you can guess the number I'm thinking of between 1 and 5 you win. If you get it wrong you lose."
    number = random.randint(1, 5)
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
        play()
      elif again == "no":
        score()
        print "Thanks for playing! Goodbye, " + name
        return
      else:
        print "I only understand yes or no thanks to my creator."
        loop()
  elif game == "no":
    print "And you wonder why you have no friends."
    return
  else:
    print "I only understand yes or no. I'm pretty dumb thanks to my creator. So if i make a mistake it's his fault."
    loop()
    
def loop():
  global game
  game = raw_input("Would you like to play a game, " + name + "?");
  if game == "yes":
    play()
  elif game == "no":
    print "And you wonder why you have no friends."
  else:
    print "I only understand yes or no. I'm pretty dumb thanks to my creator. So if i make a mistake it's his fault."
    loop()

os.system("clear")
print "Hello. My name is Python."
name = raw_input("What is your name?") 
print name + "! That is a beautful name. I'll remember that."
game = None 
pythonscore = 0
playerscore = 0
loop()

