import random

d = 0
p = 0

while True:
    r=input("press r to roll, q to quit :")

    if r == 'r':
        d == random.randint(1,6)
        print("you got :",d)
        if d == 6:
            print("congratulations, you can play now.")
            break
        else:
            print("roll again, till  you get 6.")

while true:
    r = input("press r to roll,q to quit :")

    if r == 'r':
        d = random.randint(1,6)
        print("you got :",d)

        p = p+d
        if p > 100:
           p = p-d
           print ("wait till you get", 100-p)

        print("your new position is :",p)

        if p == 100:
           print("you won!")
           exist()
        if p == 8:
            p = 37
            print("wow, a ladder. go to ",p)
        if p == 13:
            p = 34
            print("wow, a ladder. go to ",p)
        if p == 40:
            p = 68 
            print("wow , a ladder. go to ",p)
        if p == 52:
            p = 81
            print("wow , a ladder. go to ",p)
        if p == 76: 
            p = 97
            print("wow , a ladder. go to ",p) 
        if p == 11:
            p = 2
            print("no, a snake. go to",p)
        if p == 25:
            p = 4
            print("no,a snake. go to",p)
        if p == 38:
        	p = 9
        	print("no, snake. go to",p)
        if p == 65:
        	p = 46
        	print("no,a snake. go to",p)
        	
    elif r == 'q':
        print(" bye")
        exist()
