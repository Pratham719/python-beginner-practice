a=int(input("Enter a="))
b=int(input("Enter b="))
c=int(input("Enter c="))
d=int(input("Enter d="))

if (a>=b and a>=c and a>=d):
    print("a is gretest")
elif(b>=c and b>=d ):
    print("b is gretest")
elif(c>=d):
    print("c is gretest")
else:
    print("d is gretest")