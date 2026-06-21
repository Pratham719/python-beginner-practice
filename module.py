# random module
import random
#1) print(random.random())                  #0 >= random <= 1

#2) print(random.randint(1,6))              #dice

coin=["Head","Tail"]
#3) print(random.choice(coin))              #coin

#4) print(random.choice("python"))          #pick a char

#5) print(random.randrange(1,10,2))

dice=[1,2,3,4,5,6]
#6)  random.shuffle(dice)                   #will shuffle the list
# print(dice)

print(random.sample(dice,2)) #pick 2 output from dice ex.2,4