marks = list(map(float, input("Enter marks for 5 subjects (space-separated): ").split()))

total = sum(marks)
average = total / len(marks)

print("\n--- Student Marks Summary ---")
print(f"Marks: {marks}")
print(f"Total Marks: {total}")
print(f"Average Marks: {average:.2f}")