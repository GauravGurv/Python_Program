while True:
    ch=int(input("Enter your choice: (Press 1 to continue and 0 to close):-"))
    if ch==1:
        email=input("Enter your E-Mail Address: ")
        k,j,d = 0,0,0
        # print(email)
        if len(email)>=6:           #checking condintion length should be more than 6 char
            if email[0].isalpha():      #checking Email should be alphabate
                if ("@" in email) and (email.count("@")==1):        #checking @ should be in th email
                    if (email[-4]=='.') ^ (email[-3]=='.'):             #using -ve index number to check last 3 element should be "."
                        for i in email:                                 #breaking the char and check via if condition
                            if i==i.isspace():                         #checking char should be space or not
                                k=1
                            elif i==i.isupper():                    #check char is alphabate or not text converting to be upper case
                                j = 1
                            elif i==i.isdigit():                    #checking condition is digit or not
                                continue                            #if condition is true then loop return to inital state by using continue
                            elif i=="_" or i=="." or i=="@":
                                continue
                            else:
                                d=1
                        if k==1 or j==1 or d==1:
                            print("'Wrong Email'--> Email should not be space between text")
                        else:
                            pirnt("Correct Email")
                    else:
                        print("'Wrong Email' Last 3rd index should be .")
                else:
                    print("'Wrong Email' there have one @ Should be in email")
            else:
                print("'Wrong Email' 1st Char should be Alphabate")
        else:
            print("Wrong Email--> Email should me min 6 char")
    elif ch==0:
        break
    else:
        print("Invalid Operation. Try Again......")