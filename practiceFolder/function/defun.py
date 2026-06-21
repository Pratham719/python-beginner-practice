def add(a=9,b=1):
    print("Sum :",a+b)
    
#add()

def isprime(a=7):
    for i in range(2,a):
        if a%i==0:
            count=True
            break
        else:
            count=False
    if count:
            print("Prime")
    else:
            print("Not a Prime")
                       
#isprime()

def max(a=9,b=3):
    if a>b:
        print("a is maximum")
    elif b>a:
        print("b is maximum")
    else:
         print("Equal")
         
#max()

def cube(a):
    print(a**3)
    
#cube(7)

def power(a,p):
    print(f"{a}^{p} =", a**p)
   
#power(2,3)

def even(a=10):
    if a%2==0:
        print("Even")
        c=True
    else:
        print("not an Even")
        c=False
    return c

#even()

def armstrong(a=377):
    rev=0
    sum=0
    temp=a
    while temp>0:
        dig=temp%10
        sum+=dig**3
        temp//=10
    if sum==a:
        print("Armstrong")
    else:
        print("Not an Armstrong")
        
#armstrong()
     
def intrest(pa,r,pr):
    i=pa*r*pr
    intr=i/100
    print("Simple Intrest :",intr)
    return intr

#p=float(input("Enter the principal amount :"))
#ra=float(input("Enter the rate of intrest :"))
#t=float(input("Enter the time period :"))

#intrest(p,ra,t)           

def areac(redias):
    print("Area of a circal :",3.14*redias*redias)
    return 3.14*redias*redias

# r=float(input("Enter the redias :"))
# areac(r)

def areas(side):
    print("Area of squre :",side*side)
    return side*side

# s=float(input("Enter the side of a squre :"))
# areas(s)

def arear(bre,len):
    print("Area of Reactangle :",bre*len)
    return bre*len

# l=float(input("Enter the length of Rectangele :"))
# b=float(input("Enter the breadth of Rectangle :"))
# arear(b,l)
    
def swap(a,b):
    c=a
    a=b
    b=c
    print("a :",a)
    print("b :",b)
    return a and b
#a=int(input("Enter a: "))
#b=int(input("Enter b: "))
#swap(a,b)

def fact(n): #recurion
    if n==1 or n==0:
        return 1
    return fact(n-1)*n
    
n=int(input("Enter N :"))
print(fact(n))