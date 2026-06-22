n=int(input("Enter N:"))
sum=0
t=n
while(t>0):
    d=t%10
    sum=sum+(d**3)
    t//=10
if sum==n:
    print("Armstrong")
else:
    print("Not an armstrong")