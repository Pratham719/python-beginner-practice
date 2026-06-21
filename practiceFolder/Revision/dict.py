# a={
#     "sub":{"maths","fupc"},
#     "marks":{90,100}
# }
# b={ 
#     "roll no":10
# }
# a.update(b)
# print(a)

# sub={
#     "phy":55,
#     "maths":90,
#     "chem":56
# }
# #sub.clear()
# c=dict(sorted(sub.items(),key=lambda x:x[1]))
# print(c)

dict1={}
n=int(input("Enter number of keys :"))

for i in range(n):
    key=input("Enter key :")
    val=float(input("Enter val :"))
    if val.is_integer():
        val=int(val)
    dict1[key]=val
print(dict1)
# che=input("Enter key to check if key is already present in dictionary :")
# if che in dict1:
#     print("Found")
# else:
#     print("Not found")

# d=input("Enter key to delete :")
# dict1.pop(d)
# print(dict1)

# t=max(dict1,key=dict1.get)
# print("max :",t)

