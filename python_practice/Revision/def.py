def prime(n=3):
        p=True
        if n<2:
            p=False
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                p=False
                break
        if p:
             print("Prime")
        else:
            print("Not a Prime")
       
#prime()

def maxi(a=2,b=4):
    if a>b:
        print("a is greater")
    elif a==b:
        print("both are equal")
    else:
        print("b is greater")
#maxi()

def power(n=5,i=3):
    p=1
    for v in range(i):
        p=p*n
    print(p)
#power()

def cube(n):
    c=n**3
    print(c)
#cube(n=5)

def even(i):
    if i%2==0:
        return True
    return False
#print(even(8))

def armstrong(n):
    t=n
    sum=0
    while t>0:
        d=t%10
        sum+=d**3
        t=t//10
    if sum==n:
        print("armstrong")
    else:
        print("Not an armstrong")
#armstrong(371)

def inte(pa,r,t):
    interest=pa*r*t/100
    print(interest)
    return interest
# p=int(input("Enter principal amount :"))
# rate=float(input("Enter rate of amount :"))
# tp=int(input("Enter time period :"))

# inte(p,rate,tp)

def fact(n):
    if n==1 or n==0:
        return 1
    return fact(n-1)*n
print(fact(5))