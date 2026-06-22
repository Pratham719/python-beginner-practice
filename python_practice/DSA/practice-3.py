m=[[11,12,13],[14,15,16]]

# 1.Matrix Row Sum

# for _,row in enumerate(m,start=1):
#     total=0
#     for i in row:
#         total+=i
#     print(f"Sum of row {_} = {total}")

# 2.1 Matrix Column Sum
# col1=sum([row[0] for row in m])
# col2=sum([row[1] for row in m])
# col3=sum([row[2] for row in m])

# print("Sum of column 1 :",col1)
# print("Sum of column 2 :",col2)
# print("Sum of column 3 :",col3)

# 2.2 DSA way

# for col in range(len(m[0])):
#     total=0
#     for row in m:
#         total+=row[col]
#     print(f"Sum of row {col+1} = {total}")

# 3.Matrix Traversal

# new_m=[]

# for i in range(len(m[0])):
#     t=[]
#     for j in range(len(m)):   
#         t.append(m[j][i])
#     new_m.append(t)
    
# print(m)
# print(new_m)

# 4.1 Diagonal Sum
lst=[[11,12,13],[14,15,16],[17,18,19]]
total=0

# for i in range(len(lst[0])):
#     for j in range(len(lst)):
#         if i==j:
#             sum+=lst[i][j]
# print("Diagonal Sum :",total)

# 4.2 DSA way
# for i in range(len(lst)):
#     total+=lst[i][i]

# print(total)

# 5.1 Secondary Diagonal Sum
# sum_e=0
# for i in range(len(lst[0])):
#     expected=len(lst)-1
    
#     for j in range(len(lst)):
#         total=i+j
#         if total==expected:
#             sum_e+=lst[i][j]
        
# print("sum",sum_e)   

# 5.2 DSA way
for i in range(len(lst)):
    c=len(lst)-1-i
    total+=lst[i][c]
print("Sum :",total)

# 6 Find Largest Element in Matrix - DSA way
largest=lst[0][0]
for i in range(len(lst)):
    for j in range(len(lst[0])):
        if largest<lst[i][j]:
            largest=lst[i][j]
print(largest)