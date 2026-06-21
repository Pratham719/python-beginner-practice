dict1 = {
    "1":10,
    "2":20, 
    "3":30   
}
key=input("Enter the key :")

if key in dict1:
    print("The same key is already present in dictonary")
    
else:
    val=int(input("Enter the value :"))
    dict1[key]=val
    
print(dict1)