# n = (int(input("Enter N : ")))
# for i in range(1,n +1):
#     print(i )

# a =list(input("Enter the list values : "))

# b =a.copy()
# print("B =",b)

# a=list(input("Enter the values of list : "))
# a.reverse()
# print("revarse list : ",a)

# a=list(map(int,input("Enter the values of list 1 : ").split()))
# b=list(map(int,input("Enter the values of list 2 : ").split()))

# c=[]
# for i in range(len(a)):
#     c.append(a[i]+b[i])
# print(c)

a = list(map(int,input("Enter value sapreted by space : ").split()))
b=[]
for i in a:
    b.append(i * i)
print("a =",a)
print("b =",b)

#a =list(map(int,input("Enter numbers : ").split()))
# b=a[1::2]

# print(b)

# for i in range(1,len(a),2):
#    print(a[i],end=" ")

# list=(1,2,4,6,5,3,9)
# max=max(list)
# min=min(list)
# print(max)
# print(min)



# def is_prime(n):
#     if n<2:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
    
# a =list(map(int,input("Enter values seperated by space :").split()))

# pl=[]

# for i in a:
#     if is_prime(i):
#         pl.append(i)
# print("Prime Number : ",pl)   