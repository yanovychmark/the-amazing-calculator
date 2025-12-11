#made by markus sorry but i will not tell you what all this stuff does
print("the amazing calculator v1.0 insert number of how many numbers use (1, 2, 3, 4) and then input what will the numbers be and select action - + / *")
A = int(input("how many numbers? ---->"))
if A == 1:
    b = int(input('number ---->'))
    print(b)
if A == 2:
    b = int(input('number ---->'))
    c = int(input('number ---->'))
    omega = input("action ------>")
    if omega == "-":
        print(b - c)
    if omega == "+":
        print(b + c)
    if omega == "/":
        if b == 0:
            print("04 check debug")
        elif c == 0:
            print("04 check debug")
        else:
            print(b / c)
    if omega == "*":
        print(b * c)
    else:
        print("if you got nothing check debug 01")
if A == 3:
    b = int(input('number ---->'))
    c = int(input('number ---->'))
    d = int(input('number ---->'))
    omega = input("action ------>")
    if omega == "-":
        print(b - c - d)
    if omega == "+":
        print(b + c + d)
    if omega == "/":
        if b == 0:
            print("04 check debug")
        elif c == 0:
            print("04 check debug")
        elif d == 0:
            print("04 check debug")
        else:
            print(b / c / d)
    if omega == "*":
        print(b * c * d)
    else:
        print("if you got nothing check debug 01")
if A == 4:
    b = int(input('number ---->'))
    c = int(input('number ---->'))
    d = int(input('number ---->'))
    e = int(input('number ---->'))
    omega = input("action ------>")
    if omega == "-":
        print(b - c - d - e)
    if omega == "+":
        print(b + c + d + e)
    if omega == "/":
        if b == 0:
            print("04 check debug")
        elif c == 0:
            print("04 check debug")
        elif d == 0:
            print("04 check debug")
        elif e == 0:
            print("04 check debug")
        else:
            print(b / c / d / e)
    if omega == "*":
        print(b * c * d * e)
    else:
        print("if you got nothing check debug 01")
else:
    print("if you got nothing check debug 02")
alpha = input("debug mode Y/N?")
if alpha == "Y":
    print("ValueError: invalid literal for int() with base 10: means that text was used for numbers only")
    print("01 no answear means that the action is wrong or is not a real one")
    print("02 no answear means that the number of numbers is to large or not correct")
    print("04 do not do that stupid mistake (0/number)")
    print("if you want to to calculate again restart the program")
