n=int(input("Enter the N(to check if its perfect) :"))
a=[]
sum=0
for i in range(1,n):
    if n%i==0:
        a.append(i)
        sum+=i
        
if sum==n:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")