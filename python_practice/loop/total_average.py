marks = []
for i in range(1,6):
    a=float(input(f"Enter the marks of Subject {i} : "))
    marks.append(a)
t = sum(marks)
av = t / len(marks)

print("Total of given Numbers : ",t)
print("Average of given Numbers : ",av)
