list=list(map(int,input("Enter a list : ").split()))

pos =int(input("Enter position to Delete (starting from 1) :"))

if 1<=pos<=len(list):
    del list[pos-1]
    print("Updated List :",list)
else:
    print("Invalid position")    