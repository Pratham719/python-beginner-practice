dict1=[]
for i in range(5):
    a =list(map(str,input(f"Enter the student Name {i+1}:").split()))
    b =list(map(float,input("Enter the student Marks :").split()))
    dict1.append(a)
    dict1.append(b) 
print("Entered student name and marks :",dict1)
lar=dict1[1]

for i in range(1,10,2):
    if dict1[i]>lar:
        lar=dict1[i]
print("Largest :",lar)