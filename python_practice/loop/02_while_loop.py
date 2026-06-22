# while
# i=100  # i is iterator
# while i>=1: 
#     print(i)
#     i-=1
    
# Repeating execution of loop is called iteration
i=1  
while i<=10: 
    print(i)
    i+=1 


# n=int(input("Enter the value of a table :"))
# i=1
# while i<=10:
#     ans=n*i
#     print(f"{n} x {i} = {ans}")
#     i+=1

# Traversing list elements one by one

# list1=[]
# i=1
# while i<=10:
#     list1.append(i*i)
#     i+=1
# print(list1)    


# num=[1,4,9,16,25,36,49,64,81,100]
# x=int(input("Enter the num to seach :"))

# i=0
# while i<len(num):
#     if (num[i]==x):
#         print("Found at index",i)
#     i+=1    

# 1.break
i=1
while i<=5:
    print(i)
    if(i==3):
        break
    i+=1           
    
# 2.continue
i=1
while i<=5:
    
    if(i==3):
        i+=1
        continue
    print(i)
    i+=1           