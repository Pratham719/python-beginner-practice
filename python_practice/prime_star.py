# sum of prime
def prime(n):
    total=0
    if n<2:
        return total
    for i in range(2,n+1):
        p=True
        for j in range(2,i):
            if i%j==0:
                p=False
                break
        if p:
            total+=i
    print(total)
    return total
#prime(5)   

#from list of n, move zero to the end of the list

l=[1,0,2,0,4,6]
for i in l:
    if i==0:
       l.remove(i)
       l.append(i)
#print(l)

def star(n):
    k=0
    for i in range(1,n+1):
        for s in range(1,(n-i)+1):
            print(end=" ")
        while k!=(2*i-1):
            print("*",end="")
            k+=1
        k=0
        print()
        
star(7)