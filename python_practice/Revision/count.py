list1=list(map(int,input("Enter n sepreted by space :").split()))
countn=0
countz=0
countp=0
for i in list1:
    if i<0:
        countn+=1
    elif i==0:
        countz+=1
    elif i>0:
        countp+=1

print("pos",countp)
print("neg",countn)
print("zero",countz)