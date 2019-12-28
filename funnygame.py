import random
from random import randint
name = input("your name: ")
point = 0
question = 1
limit_questions = int(input("your limit question: "))
while question <= limit_questions:
    number1 = randint(0,100)
    number2 = randint(0,100)
    ctnc= ['*','+','-']
    way = random.choice(ctnc)
    if way == '*':
        answer=number1*number2
        print(f"{number1} {way} {number2} = ")
        your_answer = int(input("your answer: "))
        if your_answer == answer:
            point = point +10
            question = question +1
        elif point > 0:
            point-= 10
            question = question +1
        else:
            question = question +1
            point = 0
            pass
    elif way == '+':
        answer=number1+number2
        print(f"{number1} {way} {number2} = ")
        your_answer = int(input("your answer: "))
        if your_answer == answer:
            point = point +10
            question = question +1
        elif point > 0:
            point-= 10
            question = question +1
        else:
            question = question +1
            point = 0 
            pass
    else:
        answer=number1-number2
        print(f"{number1} {way} {number2} = ")
        your_answer = int(input("your answer: "))
        if your_answer == answer:
            point = point +10
            question = question +1
        elif point > 0:
            point-= 10
            question = question +1
        else:
            question = question +1
            point = 0
            pass
print(name+"'s point is: ")
print(point)

            
