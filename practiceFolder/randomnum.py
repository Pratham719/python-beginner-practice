import random
num=random.randint(1,10)
guess=int(input("Enter your guess from 1 to 10 (3 attempts):"))
attempts=2
while(attempts>0):
    if guess==num:
        print("\n✅ Correct")
        break
    else:
        print(f"Wrong. attempts left :{attempts}")
        guess=int(input("\nEnter your guess from 1 to 10 :"))
        attempts-=1
    if attempts==0:
        print("\nGame over . The Number was",num)
   
    