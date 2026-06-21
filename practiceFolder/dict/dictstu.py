dict1={}
n=int(input("Enter the number of students :"))

for i in range(n):
    k=input(f"Enter the name {i+1}:")
    v=int(input("Enter marks :"))
    dict1[k]=v
    
print("Dictonary :",dict1)
a=input("Enter the key to check :")
if a in dict1:
    
    print("Already Exist")
else:
    
    print("Doesnot Exist")