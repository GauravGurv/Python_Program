import random
val=int(input("1 Play | Yes \n2 No | Exit\n"))
attemp=0
h=0
c=0
if val==1 or val=="yes":
    while True:
        val1 = int(input('''
            0=Rock
            1=Paper
            2=Scissor
            Enter Your Choice: '''))
        l = ["Rock", "Paper", "Scissor"]
        val2=random.choice(l)
        if attemp==5:
            break
        if l[val1]=="Rock" and val2=="Paper":
            print("You Choose: ",l[val1])
            print("You Choose: ",val2)
            print("Computer Wins...")
            attemp+=1
            c+=1
        elif l[val1]=="Paper" and val2=="Rock":
            print("You Choose: ", l[val1])
            print("You Choose: ", val2)
            print("Human Wins...")
            attemp+=1
            h+=1
        elif l[val1]=="Rock" and val2=="Scissor":
            print("You Choose: ", l[val1])
            print("You Choose: ", val2)
            print("Human Wins...")
            attemp+=1
            h+=1
        elif l[val1]=="Scissor" and val2=="Rock":
            print("You Choose: ", l[val1])
            print("You Choose: ", val2)
            print("Computer Wins...")
            attemp+=1
            c+=1
        elif l[val1]=="Paper" and val2=="Scissor":
            print("You Choose: ", l[val1])
            print("You Choose: ", val2)
            print("Computer Wins...")
            attemp+=1
            c+=1
        elif l[val1]=="Scissor" and val2=="Paper":
            print("You Choose: ", l[val1])
            print("You Choose: ", val2)
            print("Human Wins...")
            attemp+=1
            h+=1
        else:
            print("You Choose: ", l[val1])
            print("You Choose: ", val2)
            print("Draw! Try Again...")
            attemp+=1
    if c>h:
        print("Computer points {} \nHuman points {} \n-->Computer Win".format(c,h))
    elif c<h:
        print("Computer points {} \nHuman points {} \n-->Human Win".format(c,h))
    else:
        print("Match Draw")
elif val==2 or val=="No":
    print()
else:
    print("Invalid Input/Operation")




