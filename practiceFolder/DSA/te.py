# a=int(input("Enter the Number to Revese :"))
# temp=a
# rev=0
# while temp>0:
#     dig=temp%10
#     rev=rev*10+dig
#     temp//=10
# print(rev)

# count=0
# while temp>0:
#     temp//=10
#     count+=1
# print(count)

# sum=0
# while temp>0:
#     dig=temp%10
#     sum+=dig
#     temp//=10
# print(sum)

def is_prime(n):
    is_p=True
    if(n<2):
        is_p=False
    for i in range(2,n-1):
        if n%i==0:
            is_p=False
            return is_p
    return is_p

# output=is_prime(a)    
# print(output) 

def fab(n):
    if n==1:
        return 1
    if n==0:
        return 0
    return fab(n-1) + fab(n-2) 

# n=int(input("Enter the  N :"))

# for i in range(n):
#     print(fab(i),end=" ")

# sen=input("Enter the Sentance :").lower()
# vowels={'a','e','i','o','u'}
# count=sum(1 for ch in sen if ch in vowels)
# print(count)

# Input: "apple"

# Output:
# a:1
# p:2
# l:1
# e:1

# a=input("Enter any :")
# freq={}
# # for ch in a:
#     if ch in freq:
#         freq[ch]+=1
#     else:
#         freq[ch]=1
# print(freq)

# for ch in a:
#     freq[ch]=freq.get(ch,0)+1

# print((freq))

# lst=[1,2,3,4,5,6,6,7,7,8,8]

# i=0
# while i<len(lst):
#     j=i+1
#     while j<len(lst):
#         if lst[i]==lst[j]:
#             lst.pop(j)
#         else:
#             j+=1
#     i+=1

# print(lst)


# lst=list(set(lst))
# print(lst)

# result=[]
# for l in lst:
#     if l not in result:
#         result.append(l)
# print(result)

import random as rm
# n=rm.randint(1,20)

# while True:
#     u=int(input("Gusee the Number from 1 to 20 :"))

#     if u==n:
#         print("Correct")
#         break
#     elif u-n>=5:
#         print("You are guseed Too high")
#     elif n-u>=5:
#         print("You are guseed Too low")
#     elif u>n:
#         print("You are guseed high")
#     else:
#         print("You are guseed low")

# sen=input("Enter a sentance :")

# words=sen.split()

# total_ch=0
# longest=""

# for ch in sen:
#     if ch!=" ":
#         total_ch+=1

# for word in words:
#     if len(longest)<len(word):
#         longest=word

# print("longest : ",longest)
# print("Total Words :",words)
# print("Total ch : ",total_ch)

# lst=[1,2,3,4,5,7,8,10]
# s=lst[0]
# for l in range(len(lst)):
#     if lst[l]!=s:
#         print(s,end=" ")
#         s+=1
#     s+=1

# f=input("Enter First word : ")
# s=input("Enter Second word : ")

# if sorted(f)==sorted(s):
#     print("Anagram")
# else:
#     print("Not anagram")                
        
# f=input("Enter First word : ")
# s=input("Enter Second word : ")

# if len(f)!=len(s):
#     print("Not Anagram")

# else:
#     fq={}

#     for ch in f:
#         fq[ch]=fq.get(ch,0)+1
    
#     for ch in s:
#         if ch not in fq:
#             print("Not Anagram")
#             break

#         fq[ch]-=1
    
#     else:
#         if all(value==0 for value in fq.values()):
#             print("Anagram")
#         else:
#             print("Not Anagram")

# Sum of matric
m1=[1,2,3,4,5,6,12,2,3,56,67]
m2=[7,8,9,10,11,12,13]
m3=[]
if len(m1)>len(m2):
    diff=len(m1)-len(m2)

    for _ in range(diff):
        m2.append(0) 
    
if len(m2)>len(m1):
    diff=len(m2)-len(m1)

    for _ in range(diff):
        m1.append(0) 
    

for i in range(len(m1)):
    m3.append(m1[i]+m2[i])

print(m3)