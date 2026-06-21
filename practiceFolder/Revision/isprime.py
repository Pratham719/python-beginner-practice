n=int(input("Enter N :"))
p=False
if n<=1:
    print("Not a prime")

for i in range(2,int(n**0.5)+1):
    if n%i!=0:
        p=True
        break
if p:
    print("Is prime")
else:
    print("Not prime")