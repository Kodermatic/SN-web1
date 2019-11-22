# Plan:
# User enters lines of file
# User can exit adding new lines with :q
# User is asked if file shall be saved. If yes file is saved and user is asked if file shall be printed.


path = "./07_HW - Python (write into file)/"
new_line = ""
file_text = ""
while True:
  if new_line != ":q\n":
    file_text = file_text + new_line
    new_line = input("Prease enter line content: ") + "\n"
  else:
    while True:
      save_option = input("Do you want to save entered content? (y/n) :").lower()
      if save_option in ["y", "yes"]:
        filename = input("Please enter name of file :")
        with open(path + filename, "w") as myfile:
          myfile.write(str(file_text + "\n"))
        print("File is saved")
        break
      elif save_option in ["n", "no"]:
        new_line = ""
        file_text = ""
        break
      else:
        print("Entered option is not valid.")
    else:
      while True:
        print_option = input("Do you want to print content of the file? (y/n): ")
        if print_option in ["y", "yes"]:
          with open(path + filename, "r") as myfile:  
            print(myfile.read())
          break
        elif print_option in ["n", "no"]:
          break
        else:
          print("Entered option is not valid.")
    print("Thank you and goodbye!")
    break