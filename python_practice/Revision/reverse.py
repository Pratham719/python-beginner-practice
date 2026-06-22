n=int(input("Enter n:"))
rev=0
t=n
while(t>0):
    d=t%10
    rev=rev*10+d
    t=t//10

print("Reversed value :",rev)