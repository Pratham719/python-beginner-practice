# def multipy_rev(a,b):
#     c =[]
#     n=len(a)
#     for i in range(n):
#         c.append(a[i]*b[n-i-1])
#     return c

# a=list(map(int,input("Enter the values of list A:").split()))
# b=list(map(int,input("Enter the values of list B:").split()))
# outcome =multipy_rev(a,b)
# print(outcome)

# OR

list1=list(map(int,input("Enter the values of A seprated by space : ").split()))
list2=list(map(int,input("Enter the values of B seprated by space : ").split()))
list3 =[]
n=len(list1)
for i in range(n):
    list3.append(list1[i]*list2[n-i-1])
    
print("Result :",list3)