n=int(input("Enter the Number to find his factors : "))
print(f"Factors of {n} :- ")
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")
    