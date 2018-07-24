import os
from python import Python
from healthadviser import HealthAdvisor
from guessgame import GuessGame
from diceroller import DiceRoller

def init():
  global python
  python = Python()

def confirm():
  raw_input("Press enter to continue...")
  os.system("clear")

def is_number(s):
  try:
    int(s)
    return True
  except ValueError:
    return False
  
def read_name():
  user = open("database/user", "r")
  name = user.readline().rstrip()
  user.close()
  return name

def main_menu():
    os.system("clear")
    print("What would you like to do, " + read_name() + "? Enter the number of the option.")
    print("1. Play the guessing game")
    print("2. Roll dice")
    print("3. Talk to your health advisor.")
    print("4. Quit")
    option = raw_input()
    if option == "1":
      GuessGame()
    elif option == "2":
      DiceRoller()
    elif option == "3":
      HealthAdvisor()
    elif option == "4":
      print "And you wonder why you have no friends."
    else:
      print "I only understand the number of the option. I'm pretty dumb thanks to my creator. So if i make a mistake it's his fault."
      self.main_menu()