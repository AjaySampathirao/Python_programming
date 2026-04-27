#!/bin/python3

import os
def add (a,b):
 return a+b
def subtract (a,b):
 return a-b
def multipy (a,b):
 return a*b
def divide (a,b):
 return a/b

operations_dict={
"+":add,
"-":subtract,
"*":multipy,
"/":divide
}

def calculator():
 number1=float(input("Enter the first number:"))
 for symbol in operations_dict:
  print(symbol)
 continue_flag=True
 while continue_flag:
  op_symbol=input("pick any operation:")
  number2=float(input("Enter next number:"))
  calculator_function=operations_dict[op_symbol]
  output=calculator_function(number1,number2)
  print(f"{number1} {op_symbol} {number2} = {output}")
  should_continue=input(f"Enter 'y' to continue calculate with {output} or 'n' to start new calculater or 'x' to exit:")
  if should_continue=='y':
   number1=output
  elif should_continue=='n':
   continue_flag = False
   os.system('clear')
   calculator()
  elif should_continue=='x':
   continue_flag = False
   print("Exiting..")
  else:
   continue_flag=Flase
   print("Bye")
calculator()
