import os
import datetime

class HealthAdvisor():
  
  def __init__(self):
    self.eval()
  
  def calculate_age(self, born):
    born = datetime.datetime.strptime(born, '%Y-%m-%d')
    today = datetime.datetime.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
  
  def eval(self):
    
    global confirm
    
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
      print "What year were you born?"
      year = raw_input()
      if is_year(year) == False:
        print year + " is not year. Your health is no laughing matter " + name + "."
        confirm()
        what_year()
      return int(year)
    
    def what_month():
      print "What month were you born?"
      month = raw_input()
      if is_month(month) == False:
        print month + " is not a month that I understand. Just give me the number of the month and that will be good enough."
        confirm()
        what_month()
      return int(month)
      
    def what_day():
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
          patient = open("database/patient", "w")
          patient.write(name)
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
      if os.path.isfile("/root/python/database/patient"):
        return True
      else:
        return False
    
    os.system("clear")
    if has_patient_file():
      print "I see you have a patient file."
      print "Let's see..."
      with open('database/patient') as f:
        patient_name = f.readline().rstrip()
        patient_birthdate = f.readline().rstrip()
      print patient_name + "! How are you doing? So you were born on " + patient_birthdate + "."
      print "So that means you're " + str(self.calculate_age(patient_birthdate)) + "."
      print "You're old. Looks like you're screwed. Turns out there is nothing I can do for old age."
    else: 
      print "Hi, " + patient_name + ". My name is Dr. Dyer and I am your Python doctor."
      print "Since this is your first appointment with me I have a few questions to get to know you better."
      birthdate = get_birthdate()
    raw_input("Press enter to continue...")
