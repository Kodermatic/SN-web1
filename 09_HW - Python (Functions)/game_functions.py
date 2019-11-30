### Imported libraries
import random
import json
import datetime
from os import path

### General parameters settings
my_path = "/Users/x/PycharmProjects/GIT/SN-web1/09_HW - Python (Functions)/"
my_filename = "f-scorelist.txt"
my_no_of_top_scores = 5

### Functions
def write_scores(f_path, f_filename, f_list):               # Function to write f_list variable into file
  with open(f_path + f_filename, "w") as f_score_file:
     json.dump(f_list, f_score_file)
 
def read_scores(f_path, f_filename):
  with open(f_path + f_filename, "r") as f_score_file:      # Function to read file and load it into variable 
    f_score_list = json.load(f_score_file)                  # and return variable with file content
    return f_score_list

def create_file(f_path, f_filename, f_content):             # Create empty file if does not exist
  if path.exists(f_path + f_filename) == False:
    with open(f_path + f_filename, "w") as f_score_file:
      f_score_file.write(f_content)

def top_scores(f_path, f_filename, f_no_of_top_scores, f_sorted_by="attemps"):      # Function print top x results
  with open(f_path + f_filename, "r") as f_score_file:                              # - read file and load it into variable 
    f_score_list = json.load(f_score_file)               
  
  f_sorted_lists = sorted(f_score_list, key=lambda k: k[f_sorted_by])               #  - sort list of dictionaries by f_sorted_by variable
  
  n = 1                                                                             #  - put top results in variable
  f_top_scores = ""
  for i in f_sorted_lists:
    f_top_scores += str(n) + ".)" + "   attemps:" + str(i["attemps"]) + "   secret:" + str(i["secret"]) + "   level:" + str(i["level"]) + "   date:" + str(i["date"]) + "\n"  # do not use comma instead +
    if n >= f_no_of_top_scores:
      break
    n += 1
  
  f_top_scores = f"\n Top {n-1} scores are: \n" + f_top_scores
  return f_top_scores

def choose_level():
  while True:
    level = input("Please select level of game. \n press 1 for 'easy' or press 2 for 'hard': ")
    if level in ["1", "2"]:
      if level == "1":
        level = "easy"
        break
      elif level == "2":
        level = "hard"
        break
    else:
      print("You have entered invalid value.")
  return level 

def play_game():  #Function that launch 1 cycle of number guessing game
  attemps = 0
  secret = random.randint(1,100)
  while True:
    guess = int(input("Guess secret number between 1 and 100: "))
    attemps += 1
  
    if guess == secret:
      print(f"You have guessed it! Congratulation! It is {secret}.\n You did it in {attemps} attemp/s!")
      score_list = read_scores(my_path, my_filename)
      attemp_data = {"attemps": attemps, "secret": secret, "level": my_level, "date": str(datetime.datetime.now())}
      score_list.insert(0, attemp_data)
      write_scores(my_path, my_filename, score_list)
      break
    
    elif guess > secret:
      if my_level == "easy":
        print("You guess is not correct try something smaller.")
      else:
        print("You guess is not correct try something different.")
    
    elif guess < secret:
      if my_level == "easy":
        print("You guess is not correct try something bigger.")
      else:
        print("You guess is not correct try something different.") 
    else:
      print("You guess entry is invalid.")


#### Program procedure
create_file(my_path, my_filename, "[]")   #creates score file if it does not exists
my_level = choose_level()
play_again = "y"
while play_again == "y":
  play_game()
  play_again = input("Input 'y' if you want to play again or anything for exit: ").lower()
print(top_scores(my_path, my_filename, my_no_of_top_scores))
print("Thank you for playing!")