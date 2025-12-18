#made by markus sorry but i will not tell you what all this stuff does
l = True
while l == True:
    print("the amazing calculator v1.7 insert number of how many numbers use (1, 2, 3, 4, 5) and then input what will the numbers be and select action - + / * "
          " for 4 -+ will be 1+1-1+1 and /* will be 1*1/1*1 */, +- will reverse placement")
    A = int(input("how many numbers? ---->"))
    if A == 1:
        b = int(input('number ---->'))
        print(b)
    elif A == 2:
        b = int(input('number ---->'))
        c = int(input('number ---->'))
        omega = input("action ------>")
        if omega == "-":
            print(b - c)
        elif omega == "+":
            print(b + c)
        elif omega == "/":
            if b == 0:
                print("04 check debug")
            elif c == 0:
                print("04 check debug")
            else:
                print(b / c)
        elif omega == "*":
            print(b * c)
        else:
            print("check debug 01")
    elif A == 3:
        b = int(input('number ---->'))
        c = int(input('number ---->'))
        d = int(input('number ---->'))
        omega = input("action ------>")
        if omega == "-":
            print(b - c - d)
        elif omega == "+":
            print(b + c + d)
        elif omega == "/":
            if b == 0:
                print("04 check debug")
            elif c == 0:
                print("04 check debug")
            elif d == 0:
                print("04 check debug")
            else:
                print(b / c / d)
        elif omega == "*":
            print(b * c * d)
        else:
            print("if you got nothing check debug 01")
    elif A == 4:
        b = int(input('number ---->'))
        c = int(input('number ---->'))
        d = int(input('number ---->'))
        e = int(input('number ---->'))
        omega = input("action ------>")
        if omega == "-":
            print(b - c - d - e)
        elif omega == "+":
            print(b + c + d + e)
        elif omega == "/":
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
        elif omega == "*":
            print(b * c * d * e)
        elif omega == "-+":
            print(b + c - d + e)
        elif omega == "+-":
            print(b - c + d - e)
        elif omega == "/*":
            if b == 0:
                print("04 check debug")
            elif c == 0:
                print("04 check debug")
            elif d == 0:
                print("04 check debug")
            elif e == 0:
                print("04 check debug")
            else:
                print(b * c / d * e)
        elif omega == "*/":
            if b == 0:
                print("04 check debug")
            elif c == 0:
                print("04 check debug")
            elif d == 0:
                print("04 check debug")
            elif e == 0:
                print("04 check debug")
            else:
                print(b / c * d / e)
        else:
            print("check debug 01")
    elif A == 5:
        b = int(input('number ---->'))
        c = int(input('number ---->'))
        d = int(input('number ---->'))
        e = int(input('number ---->'))
        f = int(input('number ---->'))
        omega = input("action ------>")
        if omega == "-":
            print(b - c - d - e - f)
        elif omega == "+":
            print(b + c + d + e + f)
        elif omega == "/":
            if b == 0:
                print("04 check debug")
            elif c == 0:
                print("04 check debug")
            elif d == 0:
                print("04 check debug")
            elif e == 0:
                print("04 check debug")
            elif f == 0:
                print("04 check debug")
            else:
                print(b / c / d / e / f)
        elif omega == "*":
            print(b * c * d * e * f)
        else:
            print("check debug 01")
    else:
        print("check debug 02")
    alpha = input("debug mode Y/N? ----->")
    if alpha == "Y":
        print("ValueError: invalid literal for int() with base 10: means that text was used for numbers only")
        print("01 no answear means that the action is wrong or is not a real one")
        print("02 no answear means that the number of numbers is to large or not correct")
        print("04 do not do that mistake (0/number)")
        print("05 debug function is not correct")
        print("if you want to to calculate again restart the program")
        delta = input("insert debug prompt---->")
        if delta == "quit":
            print("thanks for using")
            l = False
        elif delta == 'null': #insert cool debug features here
            print("test")
        elif delta == 'exit debug':
            print("ok")
        elif delta == 'puzzle':
            lol = input("why did the chicken cross the road?----->")
            if lol == "legsrelatetackyfrygain":
                print("correct")
            else:
                print("wrong")
        else:
            print("05 check debug")
    else:
        rep = input("calculate again?Y/N ---->")
        if rep == "Y":
            print("ok")
        else:
            l = False


