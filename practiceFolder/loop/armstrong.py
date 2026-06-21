n=int(input("Enter N :"))
temp=n
sum=0
while(temp>0):
    dig=temp%10
    sum+=dig**3
    temp//=10
if sum==n:
    print("Armstrong")
else:
    print("not Armstrong")
    