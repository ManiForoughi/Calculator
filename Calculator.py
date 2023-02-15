
w = input("What is your symbol (x, +, -, /) ")
PossVar = ["x", "-", "/", "+"]


if w == "x":
    z = float(input("What is your 1st number? "))
    if z == float or int:
        you = float(input("What is your 2nd Number? "))
        print(z * you)
    else:
        print("Invalid Number... Restart")
elif w == "/":
    z = float(input("What is your 1st number? "))
    if z == float or int:
        you = float(input("What is your 2nd Number? "))
        print(z / you)
    else:
        print("Invalid Number... Restart")
elif w == "+":
    z = float(input("What is your 1st number? "))
    if z == float or int:
        you = float(input("What is your 2nd Number? "))
        print(z + you)
    else:
        print("Invalid Number... Restart")
elif w == "-":
    z = float(input("What is your 1st number? "))
    if z == float or int:
        you = float(input("What is your 2nd Number? "))
        print(z - you)
    else:
        print("Invalid Number... Restart")
else:
    print("Invalid Input")
    