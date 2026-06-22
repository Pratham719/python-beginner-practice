# SETS
# Mutable collection -> elements can be added/removed
# Elements must be immutable (int, str, tuple)
# List and dict cannot be stored directly
# Unordered -> no fixed order
# Unique -> duplicate values are removed


# Example
# set1 = {1, 2, 6, 7, "hello", 7}
# print(set1)          # duplicate removed
# print(type(set1))
# print(len(set1))     # counts unique values


# Empty set
# empty_set = set()


# ------------------
# METHODS (modify set)
# ------------------

# 1. add() -> insert one element
# s = set()
# s.add(1)
# s.add(7)
# s.add((1, 3, 4))
# print(s)


# 2. remove() -> delete element (error if not found)
# s.remove(7)


# 3. clear() -> remove all elements
# s.clear()


# 4. pop() -> remove random element
# print(s.pop())


# ------------------
# OPERATIONS (return new set)
# ------------------

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# union() -> combine all unique values
print(set1.union(set2))

# intersection() -> common values only
print(set1.intersection(set2))

# difference() -> values present in first set only
print(set1.difference(set2))

# symmetric_difference() -> values not common in both sets
print(set1.symmetric_difference(set2))