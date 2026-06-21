ch = input("Enter a charcter : ").lower()

if len(ch)!=1 or not ch.isalpha():
    print("Please enter a single character")
else:
    if ch in ['a','e','i','o','u']:
        print("The character is \033[1m vowel \033[0m")
    else:
        print("The character is **consonant**")            