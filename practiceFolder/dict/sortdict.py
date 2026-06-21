n=int(input("Enter the Number of keys : "))
dict1={}

for i in range(n):
    key=input("Enter key :")
    values=int(input("Enter value : "))
    dict1[key]=values
    
c = dict(sorted(dict1.items(),key=lambda x:x[1]))
print("Sorted  Dictonary by values : ",c)

