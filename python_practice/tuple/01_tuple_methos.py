# TUPLE
# Ordered collection
# Immutable -> values cannot be changed after creation
# Allows duplicate values


tup = (2, 3, 1, 2, 4)

# print(tup)
# print(type(tup))

# Accessing
# print(tup[1])       # access element
# print(tup[1:4])     # slicing


# ------------------
# TUPLE METHODS
# ------------------

# 1. index() -> return index of first matching value
# print(tup.index(4))


# 2. count() -> count total occurrences
# print(tup.count(2))


# ------------------
# BUILT-IN FUNCTIONS
# ------------------

# len() -> total elements
# print(len(tup))


# max() -> largest value
# print(max(tup))


# min() -> smallest value
# print(min(tup))


# sum() -> total sum
# print(sum(tup))


# sorted() -> return sorted list (not tuple)
# print(sorted(tup))


# tuple() -> convert iterable into tuple
# print(tuple([1, 2, 3]))

# any() -> True if at least one element is truthy
# print(any(tup))

# all() -> True if all elements are truthy
# print(all(tup))

# ------------------
# EXTRA OPERATIONS
# ------------------

# Concatenation -> join tuples
# print((1, 2) + (3, 4))


# Repetition -> repeat tuple
# print((1, 2) * 3)


# Membership -> check existence
# print(2 in tup)
# print(10 not in tup)