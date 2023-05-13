#Choose any number and check that number is also guess by computer or not
#Also Showing to find how many times you attempt
import random
a= random.randint(1,100)
attemp=0
while True:
    num=int(input("Enter any number between 1 to 100: "))
    if num>1 and num<100:
        attemp+=1
    if num==a:
        print("Congratulation You Won and get Jackport...")
        break
    elif num<a:
        print("Number is smaller than Guess, Try Again...")
    elif num>a:
        print("Number is Greater then Guess, Try Again...")
    else:
        print("Value out of source mismatch! Try Again...")
print("Total Number of attemp for finding result are: ",attemp)