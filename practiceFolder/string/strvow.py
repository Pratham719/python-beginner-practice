line =input("Enter the line of text :")
for vow in "aeiou":
    print(f"{vow}:{line.count(vow)}")