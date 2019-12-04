### Imported libraries
import random
import json
import datetime
from os import path

### General parameters settings
my_path = "./10_HW - Python (Classes)"
my_filename = "c-scorelist.txt"
my_path_filename = path.join(my_path, my_filename)
my_no_of_top_scores = 5

### Functions
def write_scores(f_path_filename, f_list):               # Function to write f_list variable into file
  with open(f_path_filename, "w") as f_score_file:
     json.dump(f_list, f_score_file)
 
def read_scores(f_path_filename):
  with open(f_path_filename, "r") as f_score_file:       # Function to read file and load it into variable 
    f_score_list = json.load(f_score_file)               # and return variable with file content
    return f_score_list

def create_file(f_path_filename, f_content):             # Create empty file if does not exist
  if path.exists(f_path_filename) == False:
    with open(f_path_filename, "w") as f_score_file:
      f_score_file.write(f_content)

def top_scores(f_path_filename, f_no_of_top_scores, f_sorted_by="guess_attemps"):      # Function print top x results
  with open(f_path_filename, "r") as f_score_file:                               # - read file and load it into variable 
    f_score_list = json.load(f_score_file)               
  
  f_sorted_lists = sorted(f_score_list, key=lambda k: k[f_sorted_by])               #  - sort list of dictionaries by f_sorted_by variable
  
  n = 1                                                                             #  - put top results in variable
  f_top_scores = ""
  
  for i in f_sorted_lists:
    f_top_scores += f"{n}.)    attemps: {i['guess_attemps']}    player: {i['player_name']}  secret: {i['secret']}    level: {i['play_level']}   date: {i['datetime']}\n"
    if n >= f_no_of_top_scores:
      break
    n += 1
  
  f_top_scores = f"\nTop {n-1} scores are: \n{f_top_scores}"
  return f_top_scores

def choose_level(f_player_name):
  while True:
    level = input(f"Dear {f_player_name}, please select level of game. \n press 1 for 'easy' or press 2 for 'hard': ")
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
  my_attemps = 0
  my_secret = random.randint(1,100)
  while True:
    guess = int(input("Guess my_secret number between 1 and 100: "))
    my_attemps += 1
  
    if guess == my_secret:
      print(f"You have guessed it! Congratulation! It is {my_secret}.\n You did it in {my_attemps} attemp/s!")
      score_list = read_scores(my_path_filename)
      my_play_score = play_score(my_player_name, my_attemps, my_level, my_secret)
      score_list.insert(0, vars(my_play_score))
      write_scores(my_path_filename, score_list)
      break
    
    elif guess > my_secret:
      if my_level == "easy":
        print("You guess is not correct try something smaller.")
      else:
        print("You guess is not correct try something different.")
    
    elif guess < my_secret:
      if my_level == "easy":
        print("You guess is not correct try something bigger.")
      else:
        print("You guess is not correct try something different.") 
    else:
      print("You guess entry is invalid.")
      
def choose_player_name(f_max_length=6):
  while True:
    f_player_name = input("Please input your nickname (max 6 characters): ")
    if len(f_player_name) == 0:
      print("You haven't entered nickname!")
    elif len(f_player_name) > f_max_length:
      print("Your Nickname is bigger than 6 characters!") 
    else:
      while len(f_player_name) < f_max_length:
        f_player_name = f"{f_player_name}_"
      break
  return f_player_name

#### Classes
class play_score():
  def __init__(self, player_name, guess_attemps, play_level, secret):
    self.player_name = player_name
    self.guess_attemps = guess_attemps
    self.play_level = play_level
    self.datetime = str(datetime.datetime.now())
    self.secret = secret

#### Program procedure
create_file(my_path_filename, "[]")        # creates score file if it does not exists
my_player_name = choose_player_name()      # ask for player name and length rules check
my_level = choose_level(my_player_name)
play_again = "y"
while play_again == "y":
  play_game()
  play_again = input("Input 'y' if you want to play again or anything for exit: ").lower()
print(top_scores(my_path_filename, my_no_of_top_scores))
print("Thank you for playing!")