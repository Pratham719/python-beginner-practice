#conversion
a,b=1,2.4
sum=a+b #The process : 1.00 + 2.4 = 3.4
print(sum)


#Error :

# a,b=1,"2.4" here we are try to convert float to string that cannot be possible
# sum=a+b #The process : 1.00 + 2.4 = 3.4
# print(sum)#

#int(value)
#float(value)
#str(value) / "2" #this 2 is a str now

a=int("2")
b=4.5

sum=a+b #the process : 2.0 + 4.5 = 6.5
print(type(a))
print(sum)