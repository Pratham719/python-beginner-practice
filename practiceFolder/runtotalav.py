tup=[]
for i in range(1,11):
    score =int(input(f"Enter runs scored in inning {i} :"))
    tup.append(score)
sum =sum(tup)
average =sum /len(tup)
print("Runs : ",tup)
print("Sum of Runs in last 10 innings :",sum)
print("Average of Runs in last 10 innings :",average)