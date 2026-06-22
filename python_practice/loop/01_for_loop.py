# FOR LOOP
# Used to iterate over iterable objects
# (string, list, tuple, set, dict)


# ------------------
# ITERATION
# ------------------

# Iterate over string

# for ch in "python":
#     print(ch)


# Iterate over list

# nums = [1, 2, 3]
# for num in nums:
#     print(num)


# Iterate over tuple

# tup = (10, 20, 30)

# for i in tup:
#     print(i)


# ------------------
# RANGE()
# ------------------

# range(stop)

# for i in range(5):
#     print(i)


# range(start, stop)

# for i in range(2, 6):
#     print(i)


# range(start, stop, step)

# for i in range(1, 10, 2):
#     print(i)


# Reverse iteration

# for i in range(10, 0, -1):
#     print(i)


# ------------------
# ENUMERATE()
# ------------------

# Return index + value

# fruits = ["apple", "banana"]

# for index, value in enumerate(fruits):
#     print(index, value)


# ------------------
# ZIP()
# ------------------

# Iterate multiple iterables together

# names = ["A", "B"]
# marks = [90, 80]

# for n, m in zip(names, marks):
#     print(n, m)


# ------------------
# FOR ELSE
# ------------------

# else executes if loop ends normally

# for i in range(5):
#     print(i)
# else:
#     print("Loop completed")


# ------------------
# NESTED LOOP
# ------------------

# for i in range(3):
#     for j in range(2):
#         print(i, j)


# ------------------
# PASS
# ------------------

# pass -> placeholder

# for i in range(5):
#     pass


# num=(1,4,9,16,25,36,49,64,81,100)
# serch=int(input("Enter element to search :"))
# idx=0
# for i in num:
#     if i==serch:
#         print("Found at ",idx)
#         idx+=1
#     idx+=1


n=5
fact=1

for i in range(1,n+1):
    fact*=i
    
print(fact)
