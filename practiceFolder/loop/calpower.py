base=int(input("Enter base : "))
power=int(input("Enter power : "))
ans=1
for i in range(power):
    ans*=base
    
print(f"{base}^{power} = {ans}")
