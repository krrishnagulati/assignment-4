#QUESTION 3
'''Write a multiplication game program for kids. The program should give the player
ten randomly generated multiplication questions to do. After each, the program
should tell them whether they got it right or wrong and what the correct answer is.
Question 1: 3 x 4 = 12
Right!
Question 2: 8 x 6 = 44
Wrong. The answer is 48.
...
...
Question 10: 7 x 7 = 49
Right.'''
import random

print("WELCOME TO THE MULTIPLICATION GAME!!")
print("you will be given 10 multiplication questions\n")

count=0
score=0
while count<10:
    count =count+1
    num1 = random.randint(1,11)
    num2 = random.randint(1,11)
    guess= int(input("what is " + str(num1) + " x "+ str(num2) +" = "))
    ans = int(num1*num2)
    correct = guess == ans
    if (guess== ans):
        print ("right!!")
        score +=1
    else:
        print("wrong, the correct answer is " + str(ans) + ",")
        

    print("\nyou got {} questions correct out of ten questions".format(score))