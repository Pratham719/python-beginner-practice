listo=[]
liste=[]
     
num=list(map(int,input("Enter the Numbers sepreted by space : ").split()))

for n in num:
    if(n%2==0):
        liste.append(n)
        
    else:
        listo.append(n)
        
print("Even Numbers :",liste)
print("Odd Numbers :",listo)
