while True:
    print("enter your age")
    age=input()
    if age.isdecimal():
        break
    else:
        print("Plz enter numerical string")
print("your age is ",age)
while True:
    print("enter your password")
    pass1=input()
    if pass1.isalnum():
        break
    else:
        print("Plz enter valid password")
print("your password is ",pass1)

