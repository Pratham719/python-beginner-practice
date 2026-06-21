text=input("Enter string :")
count=0
p=True
for _ in text:
    count+=1

for i in range(count//2):
    if text[i]!=text[count-i-1]:
        p=False
        break

if (p):
    print("Palindrome")
else:
    print("Not a Palindrome")