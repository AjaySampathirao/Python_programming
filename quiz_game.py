#!/bin/python3

print("**************************")
print("Welcome to my quiz game..!\n")

Question_bank=[ 
{"text":"1.The ability of one class to acquire methods and attributes of another class is called?", "answer":"A"},
{"text": "2.Which of the following is the type of inheritance?", "answer": "D"}, 
{"text": "3.What type of inheritance have multiple subclasses to a single subclass?", "answer": "C"},
{"text": "4.what is the depth of multilevel inheritance in python?", "answer": "C"}, 
{"text": "5.What does mro stands for?", "answer": "B"}
] 

Options=[ 
["A. Inheritance", "B. Abstraction", "C. Polymorphism", "D. ObjectS"], 
["A. Single", "B. Double", "C. Multiple", "D. Both A and C"], 
["A. Multiple Inheritance", "B. Multilevel Inheritance", "C. Hierarchical Inheritance", "D. None of these"], 
["A. Two level", "B. Three level", "C. Any level", "D. None of these"], 
["A. Method recursive object", "B. Method resolution order", "C. Main resolution order", "D. Method resolution object"]
]

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

