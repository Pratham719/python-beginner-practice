import random
# lst="qwertyuiopasdfghjklzxcvbnm0123456789"
# pwd=""

# for i in range(5):
#        pwd+=random.choice(lst)

# print(pwd)
    
# OTP generator
# num="0123456789"
# otp=""
# for i in range(6):
#     otp+=random.choice(num)
 
# print(otp)

# otp=""
# for i in range(6):
#         otp+=str(random.randint(1,9))


# print("OTP :",otp)

def generate_otp(length=6):
    digits = "0123456789"
    otp = ""
    for i in range(length):
        otp += random.choice(digits)
    return otp

print("OTP:", generate_otp())
