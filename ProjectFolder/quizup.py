print("Welcome to the Python Quiz!")
questions = [
    (
        "What is the output of the following code?\nprint(type([]))",
        "A. <class 'list'>\nB. <class 'tuple'>\nC. <class 'set'>\nD. <class 'dict'>",
        "A"
    ),
    (
        "Which keyword is used to define a function in Python?",
        "A. function\nB. def\nC. fun\nD. define",
        "B"
    ),
    (
        "What is the correct file extension for Python files?",
        "A. .pyth\nB. .pt\nC. .p\nD. .py",
        "D"
    ),
    (
        "Which loop is used when the number of iterations is known?",
        "A. while\nB. do-while\nC. for\nD. repeat",
        "C"
    ),
    (
        "What is the output of this code?\nprint(2 ** 3)",
        "A. 6\nB. 8\nC. 9\nD. 23",
        "B"
    )
]
s=0
for i,q in enumerate(questions,start=1):
    print(f"\nQuestion {i} :-")
    print(q[0])
    print(q[1])
    ans=input("Enter option(A/B/C/D) :").upper()

    while ans not in['A','B','C','D']:
        ans=input("Invalide input,Enter option(A/B/C/D) :").upper()

    if ans==q[2]:
        print("Correct option")
        s+=1
    else:
        print(f"Wrong choice,correct option is {q[2]}")
    
per=s*100/5
print("Result :-")
print(f"{s}/{len(questions)}")
print(f"Precentage :{per}")


if s == 5:
    print("Brilliant! Perfect score!")
elif s >= 3:
    print("Excellent! Keep it up!")
else:
    print("Nice try! Practice more!")