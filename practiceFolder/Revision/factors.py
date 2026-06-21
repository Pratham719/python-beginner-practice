n=int(input("Enter N :"))

list1=[]
for i in range(1,n+1):
    if n%i==0:
        
        list1.append(i)
print(f"Factors of {n} :",end=" ")
print(list1)
