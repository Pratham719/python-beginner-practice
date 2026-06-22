# 1.Rotate list right
# lst=[11,12,13,14,15,16,17]
# rotate_by=2

# le=len(lst)-rotate_by

# new=[]
# for i in range(le,len(lst)):
#     new.append(lst[i])
# for i in range(0,le):
#     new.append(lst[i])
# print(new)

# 2.find missing number

# lst=[1,3,4,5,6,8,10,12]
# mis=[]
# expected=lst[0]

# for i in range(len(lst)):
#     while expected<lst[i]:
#         mis.append(expected)
#         expected+=1
#     expected+=1
# print(mis)

# 3.1 Move zero to the end of the list
# lst=[1,2,0,9,0,4,0,1,6,8,0,8,0,9]

# new=[]
# z=0
# for n in lst:
#     if n==0:
#         z+=1
#     else:
#         new.append(n)

# for _ in range(z):
#     new.append(0)
# print(new)

# 3.2 DSA way
# lst=[1,2,0,9,0,4,0,1,6,8,0,8,0,9]
# pos=0

# for i in range(len(lst)):
#     if lst[i]!=0:
#         lst[pos],lst[i]=lst[i],lst[pos]
#         pos+=1
# print(lst)

# 4.Second Largest WITHOUT sort()
# lst=[19,2,5,3,4,6,7,9,17]
# largest=float('-inf')
# sec=float('-inf')
    
# for i in lst:
#     if i>largest:
#         sec=largest
#         largest=i
#     elif i>sec and i!=largest:
#         sec=i
# print("Second Largest :",sec)

# 5.1 Pair Sum Problem

# lst=[1,4,2,6,4,7,9,8]
# target=11

# for l in range(len(lst)):
#     for i in range(l+1,len(lst)):
#         if lst[l]+lst[i]==target:
#             print(f"{lst[l]} + {lst[i]} = {target}")

# 5.2 DSA way
lst = [1,4,2,6,4,7,9,8]
target = 11

seen=set()

for num in lst:
    needed=target-num

    if needed in seen:
        print(f"{needed} + {num} + {target}")
    seen.add(num)

