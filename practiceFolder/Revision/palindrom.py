n=int(input("Enter N :"))
t=n
rev=0
while(t>0):
    d=t%10
    rev=rev*10+d
    t=t//10

if rev==n:
    print("Is palindrome")
else:
    print("not palindrom")