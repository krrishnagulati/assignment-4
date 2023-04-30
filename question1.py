#QUESTION 1
'''A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade.'''

marks=int(input("enter marks:\n"))
if(marks<0 or marks>100):
    print("error")
elif(marks>=80):
    grade="A"
elif(marks>=60):
    grade="B"
elif(marks>=50):
    grade="C"
elif(marks>=45):
    grade="D"
elif(marks>=25):
    grade="E"
else:
    grade="F"

if(grade=="A" or grade=="B" or grade=="C" or grade=="D" or grade=="E" ):
    print("congratulations you have passed the examination with grade:"+ grade)
else:
    print("you have failed the examination")
