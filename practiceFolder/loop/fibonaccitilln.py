#fibonacci till n (last num<=n)
n=int(input("Enter N :"))
a=0
b=1

while a<=n:
    print(a,end=" ")
    temp=a
    a=b
    b=temp+b