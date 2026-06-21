a=[91,13,25,27,9,11,17,15,19]
b=[22,24,34,46,56,58,50,12,14,24]
suma=0
sumb=0
for i in a:
    suma+=i
    
for i in b:
    sumb+=i
    
a.sort(reverse=True)
print(a)
print("Sum of even :",suma)
b.sort(reverse=True)
print(b)
print("Sum of odd :",sumb)