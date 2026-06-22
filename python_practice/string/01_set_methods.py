# STRING
# Immutable -> characters cannot be changed
# Ordered -> index position exists
# Supports indexing and slicing


str1 = "hello"
str2 = "world"

# ------------------
# BASIC OPERATIONS
# ------------------

# Concatenation -> join strings
# final_str = str1 + " " + str2
# print(final_str)


# Length -> total characters
# print(len(final_str))


word = "college"


# ------------------
# INDEXING
# ------------------

# Positive indexing
# c o l l e g e
# 0 1 2 3 4 5 6

# print(word[2])      # access character


# Negative indexing
# c  o  l  l  e  g  e
#-7 -6 -5 -4 -3 -2 -1

# print(word[-2])


# ------------------
# SLICING
# ------------------

# syntax -> string[start:end:step]
# end index is excluded

print(word[1:5])      # olle

print(word[:5])       # from beginning to 5

print(word[1:])       # from 1 to till end

print(word[1:6:2])    # skip 1 character


# Negative slicing

print(word[-3:-1])    # eg

# print(word[-7:-4])  # col


# Reverse string

# print(word[::-1])


# ------------------
# STRING METHODS
# ------------------

text = "hello world"


# upper() -> convert to uppercase
# print(text.upper())


# lower() -> convert to lowercase
# print(text.lower())


# capitalize() -> first letter uppercase
# print(text.capitalize())


# title() -> capitalize every word
# print(text.title())


# strip() -> remove spaces
# print(" hello ".strip())


# replace() -> replace text
# print(text.replace("world", "python"))


# find() -> return index
# print(text.find("o"))


# count() -> count occurrences
# print(text.count("l"))


# startswith() -> check starting
# print(text.startswith("he"))


# endswith() -> check ending
# print(text.endswith("ld"))


# split() -> convert to list
# print(text.split())


# join() -> join iterable
# print("-".join(["a", "b", "c"]))


# ------------------
# BUILT-IN FUNCTIONS
# ------------------

# len()
# print(len(text))


# max()
# print(max(text))


# min()
# print(min(text))


# sorted()
# print(sorted(text))