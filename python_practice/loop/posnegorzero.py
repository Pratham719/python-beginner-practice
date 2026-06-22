n=int(input("Enter the total numbers :"))
a=[]
for i in range(1,n+1):
    b=int(input(f"Enter the value {i} :"))
    a.append(b)
    
posco=0
negco=0
zero=0    
for i in a:
    if i>0:
        posco+=1
    elif i<0:
        negco+=1
    elif i==0:
        zero+=1
print("Positive count :",posco)
print("Negative count :",negco)
print("Zero count :",zero)