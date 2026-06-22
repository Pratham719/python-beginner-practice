# s1=input("Enter the 1st word : ")
# s2=input("Enter the 2nd word : ")

# if len(s1)!=len(s2):
#     print("Not Anagram")
# else:
#     f={}
#     for ch in s1:
#         f[ch]=f.get(ch,0)+1

#     for ch in s2:
#         if ch not in f:
#             print("Not Anagrammm")
#             break
#         f[ch]-=1
#     else:
#         if all(value==0 for value in f.values()):
#             print("Anagram")
#         else:
#             print("Not Anagramm")

# 2 Password checker

# p = input("Choose a password : ")

# while True:
#     Up = False
#     low = False
#     dig = False
#     spec = False

#     if len(p) < 7:
#         print("Password length should be more than 6")

#     for ch in p:

#         if ch.isupper():
#             Up = True

#         if ch.islower():
#             low = True

#         if ch.isdigit():
#             dig = True

#         if not ch.isalnum():
#             spec = True

#     if not Up:
#         print("Missing Uppercase Letter")

#     if not low:
#         print("Missing Lowercase Letter")

#     if not dig:
#         print("Missing Digit")

#     if not spec:
#         print("Missing Special Character")

#     if len(p) >= 7 and Up and low and dig and spec:
#         print("Password Accepted")
#         break

#     else:
#         p = input("Enter password again : ")

# Store Expence
# import pandas as pd
# data=pd.DataFrame({"Items":["chocolate","puri","water","Food"],"Price":[30,40,20,200]})

# selected_items={}
# total=0
# print(data)
# N=int(input("Enter the No of different items : "))
# for i in range(N):
#     selected_item=input(f"Enter the index of the item {i+1} :")
#     n=int(input("Enter the Number of Units :"))
#     item_name=data.loc[selected_item,"Items"]
#     item_price=data.loc[selected_item,"Price"]

#     selected_items[item_name]=selected_items.get(item_name,0)+n
#     total+=item_price*n
    
# print("Selected Items:", selected_items)
# print("Total Expense:", total)

num=[1,2,3,4]
ans=[]
ans.append(num)
ans.append(num)

print(ans)