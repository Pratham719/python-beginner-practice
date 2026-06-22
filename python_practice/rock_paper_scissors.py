import random
computer=random.choice(["rock","paper","scissors"])
user=input("Enetr rock,paper or scissors :").lower()
if(
    (user=="rock" and computer=="paper") or 
    (user=="paper" and computer=="scissors") or 
    ( user=="scissors" and computer=="rock")
):
    print("You won ")
elif(user==computer):
    print("Draw")
else:
    print("You loose.computer choose",computer)