#!/bin/python3

from quiz_database import Question_bank
from quiz_database import Options

print("*********************")
print("Welcome to quiz game..!")

score=0
def check_answer(user_guess, currect_answer):
 if user_guess==currect_answer:
  return True
 else:
  return False

for question_num in range(len(Question_bank)): # 0 1 2 3 4
 print("-----------------------------")
 print(Question_bank[question_num]["text"])

 for i in Options[question_num]:
  print(i)

 guess=input("Enter your answer (A/B/C/D): ").upper()
 is_currect=check_answer(guess,Question_bank[question_num]["answer"])

 if is_currect:
  print("Currect Answer")
  score += 1
 else:
  print("Incurrect Answer")
  print(f"The currect answer is {Question_bank[question_num]['answer']}\n")
 print(f"your current score is {score}/{question_num+1}")
print(f"you must given {score} of currect answers")
print(f"Your score is {(score/len(Question_bank))*100}%")

