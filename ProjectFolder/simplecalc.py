#20 min
while True:
    print("_______Welcome______")
    print("1.Addition")
    print("2.Substraction")
    print("3.Multiplication")
    print("4.division")
    print("4.Exit")
    ch=int(input("Enter your choice(1-5):"))
    a=int(input("Enter A: "))
    b=int(input("Enter B: "))

    if ch==1:
        c=a+b
        print(f"{a} + {b} =",c)
    elif ch==2:
        c=a-b
        print(f"{a} - {b} =",c)
    elif ch==3:
        c=a*b
        print(f"{a} * {b} =",c)
    elif ch==4:
        if b<1:
            print("invalid value of B ")
        else:
             c=a/b
             print(f"{a} / {b} =",c)
    elif ch==5:
        break
    else:
        print("Invalid input ")