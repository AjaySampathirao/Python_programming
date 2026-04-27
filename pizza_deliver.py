#!/bin/python3

print("Welcome to python pizza deliveries")
size = input("What size pizza do you want? S,M or L: ").upper()
pepperonit = input("Do have pepperonit on your pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese on it? Y or N: ").upper()

#todo: work out how much they need to pay based on their size choice.
bill = 0
if size == "S":
 bill += 15
elif size == "M":
 bill += 20
elif size == "L":
 bill += 25
else:
 print("you typed the wrong input.")

#todo: work out how much to add to their bill based on their pepperonit choise.
if pepperonit == "Y":
 if size == "S":
  bill += 2
 else:
  bill += 3

#todo: work out final amount based on weather if they want extra cheese.
if extra_cheese == "Y":
 bill += 1

print(f"The final bill is: ${bill}.")

