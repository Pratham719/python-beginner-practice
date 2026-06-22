def sumn(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return n+sumn(n-1)
#print(sumn(10))

def rev(s):
    if len(s)==0:
        return s
    return rev(s[1:]) + s[0]
#print(rev("llob irh"))