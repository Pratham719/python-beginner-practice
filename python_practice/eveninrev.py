# for i in range(19,0,-2):
  #  print(f"{i}",end=" ")

#Find min and max from array
arr=[]
n=int(input("Enter the Number of array Elements :"))
for i in range(n):
    val=int(input(f"Enter the Element {i+1} :"))
    arr.append(val)
print(arr)
min=max=arr[0]
for i in range(n):
    if arr[0]>arr[i]:
        min=arr[i]
    if arr[0]<arr[i]:
        max=arr[i]
print("Min :",min)
print("Max :",max)