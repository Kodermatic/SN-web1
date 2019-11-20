# Plan:
# User enters a number between 1 and 100
# FizzBuzz program starts to count to that number (it prints them in the Terminal). 
# In case the number is divisible with 3, it prints "fizz" instead of the number. 
# If the number is divisible with 5, it prints "buzz". 
# If it's divisible with both 3 and 5, it prints "fizzbuzz".

low_no = 1
high_no = 100
high_no = int(input(f"Please enter number between {low_no} and {high_no}:  "))
first_devider = 3
second_devider = 5

for number in range(low_no, high_no+1):
  if number % first_devider == 0 and number % second_devider == 0:
    print("fizzbuzz")
  elif number % first_devider == 0:
    print("fizz")
  elif number % second_devider == 0:
    print("buzz")
  else:
    print(number)
