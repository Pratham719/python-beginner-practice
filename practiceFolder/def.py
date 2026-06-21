def isp(n):
    if (n<2):
        return False
    for i in range(2,int(n**0.5)+1):
        if n%2==0:
            return False
    return True

a = list(map(int,input("Enter the N sepreted by space : ").split()))
pl =[]
for i in a :
    if isp(i):
        pl.append(i)
    
print("Prime Numbers :",pl)