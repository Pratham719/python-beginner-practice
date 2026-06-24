#r - read ; w - truncate the file ; a - append ; a+ -append +reading and writing
#r+ - reading and writing (overwrite) ; w+ - reading and writing(trncate) 
# f=open("input.py")

# # data=f.read()       #read the entire file data
# # print(data)

# line=f.readline()     #read the 1st line and print the next line empty (beacause having \n)
# print(line)           #compiler will read the line and will print after print()

# data1=f.read()        #read the remaining data exept what is already readed or printed
# print(data1)

# f.close()             #it is important to close the file to print file data 2nd time,privacy etc

# f=open("demo.txt","a") 
# a=f.write("\nstill learning")
# b=f.read()
# print(b)
# f.close()

# f=open("demo.txt","w+") 
# f.write("\nstill uehdiucw cd lning")
# print(f.read())
# f.close()

# with open("demo.txt","r") as f: #alias(diff name of same person)
#     data=f.read()
#     print(data)

# import os
# os.remove("demo.txt")

#Q-1) 
# with open("practice.txt","w") as f:
#     d=f.write("Hi everyone\n")
#     d=f.write("We are using file I/O using python\n")
#     d=f.write("I like python")

#Q-2)
def replace_word():
    with open("practice.txt","r") as f:
        c=f.read()
        new=c.replace("python","java")
        print(new)

#Q-3)
#  with open("practice.txt","r") as f:
#     c=f.read()
#     if "are" in c:
#         print("yes,it does")
#     else:
#         print("nop")

#OR

# w="are"
# with open("practice.txt","r") as f:
#     c=f.read()
#     if c(w)!=-1:
#         print("yes,it does")
#     else:
#         print("nop")

def check_for_line(w):
    
    with open("practice.txt","r") as f:
        for i in range(len("practice")):
            c=f.readline()
            if c.find(w)!=-1:
                print(f"found at line {i+1}")
    return -1
ch=check_for_line("pyton")
#print(ch)


with open("num.txt","w") as f:
    f.write("1,2,3,4,5,6,7,8,9,77,55,66,44,78,54,78,98")
    
with open("num.txt","r") as f:
    r=f.read()
    # n=""
    # for i in range(len(r)):
    #     if(f[i]==","):
    #        print(int(n))
    #        n=""
    #     else:
    #         n+=r[i]
with open("num.txt","r") as f:
    re=f.read()
    count=0
    n=re.split(",")
    for val in n:
        if(int(val)%2==0):
            count+=1
print(count)









