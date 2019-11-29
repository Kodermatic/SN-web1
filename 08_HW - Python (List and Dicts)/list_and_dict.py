import random
import json
import datetime
from os import path

mypath = "/Users/x/PycharmProjects/GIT/SN-web1/08_HW - Python (List and Dicts)/"
myfilename = "d-scorelist.txt"
secret = random.randint(1,100)
attemps = 0

def write_scores(fpath, ffilename, flist):           # Function to write into file
  with open(fpath + ffilename, "w") as score_file:
     json.dump(flist, score_file)
 
def read_scores(fpath, ffilename):
  with open(fpath + ffilename, "r") as score_file:    # Function to read file and load it into variable
    score_list = json.load(score_file)
    return score_list

def create_file (fpath, ffilename, fcontent):          # Create empty file if does not exist
  if path.exists(fpath + ffilename) == False:
    with open(fpath + ffilename, "w") as score_file:
      score_file.write(fcontent)

create_file(mypath, myfilename, "[]")

while True:
  guess = int(input("Guess secret number between 1 and 100: "))
  attemps += 1
  
  if guess == secret:
    print(f"You have guessed it! Congratulation! It is {secret}.\n You did it in {attemps} attemp/s!")
    score_list = read_scores(mypath, myfilename)
    attemp_data = {"attemps": attemps, "date": str(datetime.datetime.now())}
    score_list.insert(0, attemp_data)
    write_scores(mypath, myfilename, score_list)
    top_scores_limit = 5
    print(f"Top {top_scores_limit} scores:")
    
    newlist = sorted(score_list, key=lambda k: k['attemps'])    #sort list of dictionaries by "attemps"
    
    n = 1 
    for i in newlist:
      print(str(n) + ".)", "    attemps:", i["attemps"], "   date:", i["date"])
      if n >= top_scores_limit:
        break
      n += 1
    break
  
  elif guess > secret:
    print("You guess is not correct try somethink smaller.")
    
  elif guess < secret:
    print("You guess is not correct try somethink bigger.")
  
  else:
     print("You guess entry is invalid.")