import os
import defs

class Python():
  
  def __init__(self):
    global name
    os.system("clear")
    if os.path.isfile("database/user") == False:
      print "Hello. My name is Python."
      name = self.ask_name()
      print name + "! That is a beautful name. I'll remember that. And just in case I forget I'll even write it down."
      if os.path.isdir("database") == False:
        os.makedirs("database")
      user = open("database/user", "w")
      user.write(name + "\n")
      user.close()
      confirm()
      defs.main_menu()
    else:
      name = defs.read_name()
      print "Welcome back, " + name
      defs.main_menu()
    
  def ask_name(self):
    name = raw_input("What is your name?") 
    if name == "":
      self.ask_name()
    else:
      return name
    