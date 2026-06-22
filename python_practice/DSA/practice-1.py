# 1. frequency counter

# word=input("Enter a word :")
# f={}
# for w in word:
#     f[w]=f.get(w,0)+1

# print(f)

# 2.Duplicated detactor

# lst=list(map(int,input("Enter elements of list seprated by spaces : ").split()))
# filtered_lst=list(set(lst))

# if filtered_lst==lst:
#     print("Duplicate Doesn't Exist")
# else:
#     print("Duplicate Exist")
#     print("Filtered List : ",filtered_lst)

# 3.Find & Print Only Unique Elements

# lst=[1,2,3,4,5,3,2]
# f={}
# for l in lst:
#     f[l]=f.get(l,0)+1

# U=[]
# for key,v in f.items():
#     if v==1:
#         U.append(key)
    
# print(U)

# 4.reverse word Ex. 12 34 567 Output : 567 34 12

# words=input("Enter the sentance :").split()
# i=1
# for w in words:
#     print(words[len(words)-i],end=" ")
#     i+=1

# for i in range(len(words)-1,-1,-1):
#     print(words[i],end=" ")

# 5. Longest Word Finder
sen="Pratham rangoonwala python_player".split()
large=sen[0]
for i in range(len(sen)):
    if len(large)<len(sen[i]):
        large=sen[i]
print(large)

# 6.Sum of element of list
l1=list(range(1,11))
l2=list(range(11,23))

max_len=max(len(l1),len(l2))
l1.extend([0]*(max_len-len(l1)))
l2.extend([0]*(max_len-len(l2)))

l3=[a+b for a,b in zip(l1,l2)]
print(l3)