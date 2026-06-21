a= input("Enter List : ").split()

b=a.copy()
b.reverse()

if( b== a):
    print("List is palindrome")
else:
    print("Not palindrome")
