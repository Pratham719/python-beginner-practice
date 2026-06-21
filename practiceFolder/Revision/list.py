l1=list(map(int,input("Enter list 1 values sepreted by space :").split()))
# l2=list(map(int,input("Enter list 2 values sepreted by space :").split()))

# l3=[]
# l=min(len(l1),len(l2))

# for i in range(l):
#     l3.append(l1[i]+l2[i])
# print(l3)

# l2=l1.copy()
# l2.sort(reverse=False)
# print(l2)
l2=[]
#WAPT to print all prime n from list in other list(ie.input [2,3,4,5,6,7,8,9,11,17],output [2,3,5,7,11,17])
for i in l1:  
    if i>1:
        p=True
        for j in range(2,i):
            if i%j==0:
                p=False
                break
        if p:
            l2.append(i)
print(l2)