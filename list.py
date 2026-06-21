# List is mutable
# marks =[66.7,34.6,45.6,34.8]
# print(marks)
# print(type(marks))
# print(marks[2])

# stu = ["karan",85,"surat"]
# print(type(stu))
# print(stu)
# stu[2]= 67
# print(stu)

marks =[10,100,90,60,50]               #slicing in List
# print(marks[-6 :-2])                 # print [10,100,900]
#print(marks[1 :5])                    # print [100,90,60,50]
marks1=marks.list[:]
# 1) marks.append(77)                   #Adds value at end of a list
# print(marks)

# 2) marks.sort()                       #print values in assending order
# print(marks)

# 3) marks.sort(reverse = True)         #print value in dissending order
# print(marks)

# 4) marks.reverse()                    # reverse original list
# print(marks)

# 5) marks.insert(2,13)                 #insert values at the end
# print(marks)

#  list =[1,2,3,2] 
# 6) list.remove(2)                    #remove the first occurance
# print(list)

# 7) list.pop(2)                       #list.pop(index)
# print(list)

#8) list.extend(marks)  #val of list,whan val of marks