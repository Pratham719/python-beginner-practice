# List is mutable
info ={
    "name" : "pratham",
    "subjects":["python" ,"java","c"],
    "topic":("py","th","on"),
    "age" : 18,
    "is_adult":True,
    "Marks":98
    }
# info ["name"] ='vaish'
# print(type(info))
# print(info["name"])

# nested={
#     "name":"rahul",
#     "subjects":{
#         "ss":90,
#         "chem":98
#         }    
# }
#  print(nested)
# print(nested["subjects"])
# print(nested["subjects"]["chem"])

# print(len(info)) #output : n(total key)    # exepet nested keys

#1) print(info.keys())
# print(list(info.keys()))

#2) print(info.values())

#3) print(info.items())          # returns dict as a tuple
# pairs = list(info.items()) 
#4) print(pairs[0])                #returns key and values from index 0

#5) print(info.get('surname'))   #whenever we work with multiple dicts and if 1 error come(due to wrong dict/key name) 
                                 #than the code after the error will not be run ,so we use .get() fun

#6)info.update({"city":"surat","name":"prit"})
# print(info)

#7) info.clear()                #after this output:{}