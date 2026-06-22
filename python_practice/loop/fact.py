n=int(input("Enter N : "))
i=1
fact=1
for i in range(1,n+1):
    fact*=i
    
print("factorial of n nums are",fact)