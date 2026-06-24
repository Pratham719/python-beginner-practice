lst=[]
for i in range(1,11):
    score =int(input(f"Enter runs scored in inning {i} :"))
    lst.append(score)
sum =sum(lst)
average =sum /len(lst)
print("Runs : ",lst)
print("Sum of Runs in last 10 innings :",sum)
print("Average of Runs in last 10 innings :",average)