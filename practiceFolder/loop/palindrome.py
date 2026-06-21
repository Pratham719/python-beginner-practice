n=int(input("Enter N: "))
rev=0
temp=n
while temp>0:
    dig=temp%10
    rev=rev*10+dig
    temp=temp//10
    
if n==rev:
    print(f"{n} is palindrome")
    
else:
    print(f"{n} is not palindrome")