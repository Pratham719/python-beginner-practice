# def hel():
#     print("Hello")

# output=hel()
# print(output) # if fun. having none return than the output will be none

#average of 3 num
# def av(a,b,c):
#     sum=a+b+c
#     ave=sum/3
#     print(ave)
#     return ave
# av(7,8,9)#7,8,9 are the arguments

# def lent(list):
#     print( len(list))

# list1=[1,3,2,4]
# #lent(list1)

# def single_line(list):
#     for i in list:
#         print(i,end=" ")
    
# list1=["bha","eq","py","th","on"]
# # single_line(list1)

# def fact(a):
#     fact=1
#     for i in range(1,a+1):
#         fact*=i
#     print(fact)
        
# #fact(5)

# def usd(a):
#     b=a*89
#     print(a,"USD =",b,"INR")
#     return a
# #usd(100)

# def odev(n):
#     if n%2==0:
#         print("Even")
#     else:
#         print("Odd")
        
# #odev(30)

# def show(n):
#     if n==0: #base case
#         return
#     print(n)
#     show(n-1)
    
#show(9)

def fact(n):
    if (n==1 or n==0):
        return 1
    return fact(n-1)*n

#print(fact(5))
def sum(n):
    if (n==0):
        return 0
    return sum(n-1) + n
cal=sum(5)
#print(cal)

def print_ele(list,i=0):
    if i==len(list):
        return
    print(list[i])
    print_ele(list,i+1)
    
list1=[3,54,5,6,5,3,2,7,9]
print_ele(list1)   