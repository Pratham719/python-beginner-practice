# multiple l1's first with l2's last value..
# l1=list(map(int,input("Enter list 1 sepreted by space :").split()))
# l2=list(map(int,input("Enter list 1 sepreted by space :").split()))

# l3=[]
# n=len(l1)
# for i in range(n):
#     l3.append(l1[i]*l2[n-i-1])

# print(l3)
 
#Table of given n
# table=[]
# for i in range(1,11):
#     table.append(n*i)
# print(table)
#l1=[]

#sum,ave of first 10 odd
# for i in range(20):
#     if i%2!=0:
#         l1.append(i)
# sum1=sum(l1)
# av=sum1/len(l1)
# print(l1)
# print(sum1)
# print(av) 

#store run,their sum and average
# score=[]
# for i in range(10):
#     n=int(input(f"Enter runs scored in inning {i+1} :"))
#     score.append(n)
# print(score)
# s=sum(score)
# ave=s/len(score)
# print(s)
# print(int(ave))


#l=list(map(int,input("Enter number sepreted by space :").split()))
# lo=[]
# le=[]
# n=len(l)
# for i in l:
#     if i%2==0:
#         le.append(i)
#     else:
#         lo.append(i)

# print("Odd List :",lo)
# print("Even List :",le)

#sort values of list
#print(sorted(l))

#Delete element at pos
# n=list(map(int,input("Enter the elements of list :").split()))
# pos=int(input(f"Enter the position to delete element (0-{len(n)-1}):"))
# n.pop(pos)
# print(n)

#ascending,descending
n=list(map(int,input("Enter the elements of list :").split()))
n.sort()
print("Ascending order :",n)
n.sort(reverse=True)
print("Desecnding order :",n)