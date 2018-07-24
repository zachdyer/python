import random
import os
import datetime

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
  global name
  os.system("clear")
  print("What would you like to do, " + name + "? Enter the number of the option.")
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
    main_menu()
      
def confirm():
  raw_input("Press enter to continue...")
  os.system("clear")

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
  
  def __init__(self):
    self.play()
  
  def play(self):
    global name
    os.system("clear")
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
      os.system("clear")
      self.play()
    elif again == "no":
      os.system("clear")
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
    print name + ": " + str(self.player_score) + "       Python: " + str(self.python_score)
    
  def game_over(self):
    if self.player_score == self.python_score:
      print "Thanks for playing. I guess we are evenly matched."
      confirm()
    elif self.player_score > self.python_score:
      print "It's offical. You're better than me. But that's okay because I'll still be here assuming my creator doesn't screw it up."
      confirm()
    else:
      print "See you later loser. Come back when you grow a pair."
      confirm()

class HealthAdvisor():
  
  def __init__(self):
    self.eval()
  
  def calculate_age(self, born):
    born = datetime.datetime.strptime(born, '%Y-%m-%d')
    today = datetime.datetime.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
  
  def eval(self):
    
    def is_year(year):
      if year and year.isdigit():
        if int(year) >=1900 and int(year) <=2020:
          return True
      return False
      
    def is_month(month):
      if month and month.isdigit():
        if int(month) >= 1 and int(month) <= 12:
          return True
      return False
      
    def is_day(day):
      if day and day.isdigit():
        if int(day) >= 1 and int(day) <= 31:
          return True
      return False
    
    def what_year():
      os.system("clear")
      print "What year were you born?"
      year = raw_input()
      if is_year(year) == False:
        print year + " is not year. Your health is no laughing matter " + name + "."
        confirm()
        what_year()
      return int(year)
    
    def what_month():
      os.system("clear")
      print "What month were you born?"
      month = raw_input()
      if is_month(month) == False:
        print month + " is not a month that I understand. Just give me the number of the month and that will be good enough."
        confirm()
        what_month()
      return int(month)
      
    def what_day():
      os.system("clear")
      print "What day were you born on?"
      day = raw_input()
      if is_day(day) == False:
        print day + " is not a calendar day. Try again."
        confirm()
        what_day()
      return int(day)
    
    def get_birthdate():
      year = what_year()
      month = what_month()
      day = what_day()
      birthdate = datetime.date(year, month, day)
      if confirm_birthdate(birthdate):
        print "Now at least I won't forget your birthdate. I'll forget everything else but not your birthdate."
      else:
        print "Well I guess that is all the time I have for you but at least I know your birthdate until you leave."
        print "Then I'll forget we ever had this conversation."
      return birthdate
      
    def confirm_birthdate(birthdate):
      
      def confirm_file():
        print "I tried writing your name and birthdate down in your patient file."
        print "Why don't you check and see if the file is in the folder."
        print "Was it there?"
        check_patient_file = raw_input()
        if check_patient_file == "yes":
          print "Good. You can be confident I know how to write."
          confirm()
          return True
        elif check_patient_file == "no":
          print "I guess I suck at being a doctor"
          return False
        else:
          print "I only understand yes or no. It's a doctor thing."
      
      if str(birthdate) != "":
        print "Where you born on " + str(birthdate) + "?"
        response = raw_input()
        if response == "yes":
          print "I'll write that down as soon as I figure out how to write things down."
          patient = open("patient", "w")
          patient.write(name + "\n")
          patient.write(str(birthdate) + "\n")
          patient.close()
          return confirm_file()
        elif response == "no":
          get_birthdate()
        else:
          print "I know I'm a doctor but I still only understand yes or no."
          confirm_birthdate(birthdate)
      else:
        get_birthdate()
      
    def has_patient_file():
      if os.path.isfile("/root/python/patient"):
        return True
      else:
        return False
    
    os.system("clear")
    if has_patient_file():
      print "I see you have a patient file."
      print "Let's see..."
      with open('patient') as f:
        patient_name = f.readline().rstrip()
        patient_birthdate = f.readline().rstrip()
      print patient_name + "! How are you doing? So you were born on " + patient_birthdate + "."
      print "So that means you're " + str(self.calculate_age(patient_birthdate)) + "."
      print "You're old. Looks like you're screwed. Turns out there is nothing I can do for old age."
    else: 
      print "Hi, " + name + ". My name is Dr. Dyer and I am your Python doctor."
      print "Since this is your first appointment with me I have a few questions to get to know you better."
      birthdate = get_birthdate()
    confirm()
    
init()