import random

pythonscore = 0
playerscore = 0

def revealnumber(number, guess):
  print "I was thinking of the number " + str(number) + " and you said " + guess 
  
def score():
  global pythonscore 
  global playerscore
  global name
  print "SCORE"
  print "Python: " + str(pythonscore)
  print name + ": " + str(playerscore)
  
def play():
  global game
  global pythonscore 
  global playerscore
  if game == "yes":
    print "If you can guess the number I'm thinking of between 1 and 10 you win. If you get it wrong you lose."
    number = random.randint(1, 10)
    guess = raw_input("What number am I thinking of?")
    if number == guess:
      playerscore = playerscore + 1
      revealnumber(number, guess)
      score()
      print "Perfect! You win!!! *Final Fantasy Fanvar music plays*"
    else :
      pythonscore = pythonscore + 1
      revealnumber(number, guess)
      score()
      again = raw_input("You lose! Would you like to play again?")
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

print "Hello. My name is Python."
name = raw_input("What is your name?") 
print name + "! That is a beautful name. I'll remember that."
game = None 
loop()

