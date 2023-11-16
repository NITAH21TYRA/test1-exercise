#QUESTION 2 (i)
def average_of_numbers(x,y):
    sum = x + y
    average= (sum)/2
    #print(f"The average of two numbers is {average}")
#Choosing 6 and 4 as numbers of my choice.
average_of_numbers(70,70)

#(ii)
#Let the three numbers be 70,55 and 85
a = 70
b = 55
c = 85
#if a<b and a<c:
    #print("{a} is the minimum number")
 #elif b<a and b<c:
    #print(f"{b} is the minimum number")
# else:
    #print(f"{c} is the minimum number")

#Write a program that asks a user to in put 3 numbers and finds the minimum number.

def minimum_number(a,b,c):
    a = int(input('Enter the first number'))
    b = int(input('Enter the second number'))
    c = int(input('Enter the third number'))
    if (a<b and a<c):
        print(f"{a} is the minimum number")
    elif (b<a and b<c):
        print(f"{b} is the minimum number")
    else:
        print(f"{c} is the minimum number")
minimum_number(60,70,80)


[90,88,84,71,49]
def gradeCourseUnit(mark):
    if(mark>=90 and mark<=100):
        print(f"You scored an A")
    elif(mark>=80 and mark<=89):
        print(f"You scored a B")
    elif(mark>=70 and mark<=79):
        print(f"You scored a C")
    else:
        print(f"You scored a D,below average.")
gradeCourseUnit(90)


#Logical or
def guessNumber(num):
    if(num==89 or num==100):
        print(f"You get it right")
    else:
        print(f"Try again,wrong attempt")

