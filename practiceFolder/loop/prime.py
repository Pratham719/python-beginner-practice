n=int(input("Enter N :"))
if n<=1:
    print(f"{n} is not a prime number")
    found=False
    
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        found=True
        break
    else:
        found=False
        
        
if(found):
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")
