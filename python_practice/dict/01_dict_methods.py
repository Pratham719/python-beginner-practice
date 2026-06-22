# DICTIONARY
# Mutable -> values can be changed
# Stores data as key:value pairs
# Keys must be unique
# Keys must be immutable


info = {
    "name": "pratham",
    "subjects": ["python", "java", "c"],
    "topic": ("py", "th", "on"),
    "age": 18,
    "is_adult": True,
    "marks": 98
}


# ------------------
# ACCESSING VALUES
# ------------------

# print(info["name"])          # access value using key

# info["name"] = "vaish"       # update value

# print(type(info))


# ------------------
# NESTED DICTIONARY
# ------------------

# nested = {
#     "name": "rahul",
#     "subjects": {
#         "ss": 90,
#         "chem": 98
#     }
# }

# print(nested)
# print(nested["subjects"])
# print(nested["subjects"]["chem"])


# ------------------
# BUILT-IN FUNCTIONS
# ------------------

# len() -> count total keys
# print(len(info))


# type() -> return datatype
# print(type(info))


# list() -> convert iterable to list
# print(list(info.keys()))


# sorted() -> sort keys
# print(sorted(info))


# str() -> convert dict to string
# print(str(info))


# ------------------
# DICTIONARY METHODS
# ------------------

# 1. keys() -> return all keys
# print(info.keys())


# 2. values() -> return all values
# print(info.values())


# 3. items() -> return key-value pairs
# print(info.items())

# pairs = list(info.items())
# print(pairs[0])


# 4. get() -> return value safely (avoid KeyError)
# print(info.get("surname"))


# 5. update() -> add/update key-value pair
# info.update({"city": "surat", "name": "prit"})
# print(info)


# 6. clear() -> remove all items
# info.clear()


# 7. pop() -> remove value using key
# print(info.pop("age"))


# 8. popitem() -> remove last inserted pair
# print(info.popitem())


# 9. copy() -> create shallow copy
# copy_dict = info.copy()
# print(copy_dict)


# 10. setdefault() -> return value or create key
# print(info.setdefault("city", "surat"))