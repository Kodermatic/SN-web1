# Plan:
# The program greets user and describes what's the purpose of the program.
# The program asks user to enter number of kilometers.
# User enters the amount of kilometers.
# The program converts these kilometers into miles and prints them.
# The program asks user if s/he'd want to do another conversion.
# If yes, repeat the above process (except the greeting).
# If not, the program says goodbye and stops.
print("Hi, with this program you can convert kilometers into miles.")
another_conversion = "y"
while another_conversion in "[y, yes]":
  number_of_km = float(input("Please input number of kilometers: ").replace(",","."))
  number_of_mi = number_of_km * 0.6213712
  print (f"{number_of_km} km is {number_of_mi} miles! \n \n")
  another_conversion = input("Do you want another conversion (y/n)").lower()
else:
  print("Thank you for using our program. Googbye!")