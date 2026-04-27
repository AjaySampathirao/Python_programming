#!/bin/python3

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to treasure Island")
print("Your mission is to find the treasure")

direction = input('You\'re at the crassed.'
                  'where do you want to go.'
                  'Type "left" or "right":\n').lower()

if direction == "left":
 by = input('You\'re at the lake.'
            'There is an Island in the middle of the lake.'
            'Type "wait" to wait for a boat.'
            'Tpye "swim" to to swim acress.\n').lower()
 if by == "wait":
  door = input("They are arrived at the Island unharmed."
               "There is house with 3 doors 'red' 'yellow' and 'blue'."
               "Which colour do you choose?\n").lower()
  if door == "red":
   print("The room is full of fire, Game over!")
  elif door == "yellow":
   print("You got the treasure. You win!")
  elif door == "blue":
   print("You enter a room of beast. Game over")
  else:
   print("You chose a door that does\'nt exit. Game over")
 else:
  print("You got attacked by angry trout. Game over!")
else:
 print("You fell in to a hole.Game over!")

