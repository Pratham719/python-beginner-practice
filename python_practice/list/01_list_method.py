# LIST
# Mutable -> elements can be changed
# Ordered -> index position exists
# Allows duplicate values
# Stores multiple datatypes


students = ["Pratham", "Rahul", "Aman", "Neha"]

print(students)


# ------------------
# ACCESSING
# ------------------

# Indexing

print(students[0])          # first element
print(students[-1])         # last element


# Slicing

print(students[1:3])        # index 1 to 2
print(students[:2])         # beginning to index 1
print(students[2:])         # index 2 till end
print(students[::-1])       # reverse list


# ------------------
# MODIFYING LIST
# ------------------

marks = [80, 85, 90]

print("Before:", marks)

marks[1] = 95

print("After:", marks)


# ------------------
# LIST METHODS
# ------------------

nums = [10, 20, 30]

# 1. append()
# Add one value at end

print("\nappend()")
print("Before:", nums)

nums.append(40)

print("After:", nums)


# 2. extend()
# Add multiple values

print("\nextend()")

nums.extend([50, 60])

print(nums)


# 3. insert()
# Insert at specific index

print("\ninsert()")

nums.insert(1, 99)

print(nums)


# 4. remove()
# Remove first matching value

print("\nremove()")

nums.remove(20)

print(nums)


# 5. pop()
# Remove using index

print("\npop()")

removed = nums.pop(2)

print("Removed:", removed)
print(nums)


# 6. clear()
# Remove everything

temp = [1, 2, 3]

print("\nclear()")

temp.clear()

print(temp)


# ------------------
# SEARCHING
# ------------------

items = ["apple", "banana", "mango"]

# 7. index()
# Find position

print("\nindex()")
print(items.index("banana"))


# 8. count()
# Count occurrences

data = [1, 2, 1, 1, 5]
print("\ncount()")
print(data.count(1))


# ------------------
# SORTING
# ------------------

marks = [90, 70, 50, 100]

# 9. sort()

print("\nsort()")
marks.sort()
print(marks)

# Descending

marks.sort(reverse=True)
print(marks)


# 10. reverse()

print("\nreverse()")
marks.reverse()
print(marks)


# ------------------
# COPYING
# ------------------

list1 = [1, 2, 3]

# 11. copy()

list2 = list1.copy()
list2.append(4)

print("\ncopy()")
print(list1)
print(list2)


# ------------------
# BUILT-IN FUNCTIONS
# ------------------

nums = [4, 8, 1, 9]

print("\nBuilt-in Functions")

print("Length:", len(nums))

print("Max:", max(nums))

print("Min:", min(nums))

print("Sum:", sum(nums))

print("Sorted:", sorted(nums))


# ------------------
# LIST COMPREHENSION
# ------------------

# Create squares

square = [i*i for i in range(1, 6)]

print("\nList Comprehension")
print(square)


# Filter even

even = [i for i in range(10) if i % 2 == 0]
print(even)


# ------------------
# MEMBERSHIP
# ------------------

fruits = ["apple", "banana"]

print("\nMembership")

print("apple" in fruits)

print("orange" not in fruits)