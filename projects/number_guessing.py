#NumberGuessing Python project
#print("Hello world")
import random

comp_guess=random.randint(1,10)

limit=0
score=0

#0 , 1,2,.......!3
while(limit<3):
    try:
        user_guess=int(input("Guess the number (between 1 to 10):"))
        if(user_guess>10 or user_guess<0):
            print("Wrong input!!!")
    except:
        print("Please enter the correct input")
    

    if(comp_guess==user_guess):
        if(limit==0):
            score+=15
            break

        elif(limit==1):
            score+=10
            break
        elif(limit==2):
            score+=5
            break
        else:
            score=score
            break
    elif(comp_guess>user_guess):
        print("Your guess numbers is lower than my number!!")
    else:
        print("Your guess numbers is greater than my number!!")
    
    limit+=1

if(limit>2):
    print("You have tried many times!!")
    print("My number was {}".format(comp_guess))

else:
    print("Congo! Your score is {}".format(score))
    