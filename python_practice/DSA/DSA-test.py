import random as rd



comp=rd.randint(1,3)

print("\n---------- BEST OF LUCK -----------\n")

user=input("Choose between stone/paper/scissor : ")

if comp==1:
    c="stone"
elif comp==2:
    c="paper"
else:
    c="scissor"

if user=="stone":
    if c=="paper":
        print("You lose")
    elif c=="scissor":
        print("You won")
    else:
        print("tie")

elif user=="paper":
    if c=="stone":
        print("You won")
    elif c=="scissor":    
        print("You lose")
    else:
        print("tie")

else:
    if c=="stone":
        print("You won")
    elif c=="paper":    
        print("You lose")
    else:
        print("tie")

print(f"computer choosed {c}")