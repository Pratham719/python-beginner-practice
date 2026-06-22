odd=[]
even=[]
     
num=list(map(int,input("Enter the Numbers sepreted by space : ").split()))

for n in num:
    if n%2==0:
        even.append(n)
        
    else:
        odd.append(n)
        
print("Even Numbers :",even)
print("Odd Numbers :",odd)
