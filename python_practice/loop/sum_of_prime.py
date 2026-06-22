n=int(input("Enter N :"))
sum=0
for i in range(2,n+1):
    p=True
    for j in range(2,i):
        if i%j==0:
            p=False
    if p:
        sum+=i
        
print("Sum: ",sum)
