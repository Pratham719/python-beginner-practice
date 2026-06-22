set1=set(map(int,input("Enter values sepreted by space :").split()))
print("2nd set :-")
set2=set(map(int,input("Enter values sepreted by space :").split()))
    
com=set1.intersection(set2)
print("comman values :",com)