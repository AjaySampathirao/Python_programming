#!/bin/python3

print("Welcome to rollercoaster game!")

height=int(input("What is your height in CM?\n"))
bill = 0

if height >= 120:
 print("You can ride the rollercoaster")

 age=int(input("What is your age?\n"))

 if age <= 12:
  bill = 5
  print("You have to pay 5 rupees")
 
 elif age <= 18:
  bill = 7
  print("You have to pay 7 rupees")
 
 elif age >= 45 and age <=55:
  print("Everything is going to ok, Have a free ride on us!")

 else:
  bill = 12
  print("You have to pay  12 rupees")
 
 wants_photo=input("Do you want to have a photo take? type y for Yes and n for No\n")
 if wants_photo == "y":
  bill += 5
  print(f"The total bill is:${bill}")

else:
 print("You have to grow taller before you can ride")


