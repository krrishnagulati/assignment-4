# QUESTION 2
'''A year is a leap year if it is divisible by 4, except that years divisible by 100 are not
leap years unless they are also divisible by 400. Write a program that asks the user
for a year and prints out whether it is a leap year or not.'''
year =(int(input("enter the year:\n")))
if year<0:
    print("error")
elif(year%100==0 and year%400==0):
    print("it may be a leap year")
elif(year%4==0):
    print("it is a leap year")
elif(year%100==0):
    print("it is not a leap year")
else:
    print("it is not a leap year")