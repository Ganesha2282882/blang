import os
import sys

def nothing():
    pass

if sys.argv[1] == "say":
    try:
        print(sys.argv[2])

    except:
        nothing()

    try:
        print(sys.argv[3])

    except:
        nothing()

    try:
        print(sys.argv[4])

    except:
        nothing()

elif sys.argv[1] == "add":
    try:
        print(int(sys.argv[2]) + int(sys.argv[3]))

    except:
        print("ERROR: Unknown hard error")

elif sys.argv[1] == "mpy":
    try:
        print(int(sys.argv[2]) * int(sys.argv[3]))

    except:
        print("ERROR: Unknown hard error")

elif sys.argv[1] == "div":
    try:
        print(int(sys.argv[2]) / int(sys.argv[3]))

    except:
        print("ERROR: Unknown hard error")

elif sys.argv[1] == "ta":
    try:
        print(int(sys.argv[2]) - int(sys.argv[3]))

    except:
        print("ERROR: Unknown hard error")

elif sys.argv[1] == "ram":
    try:
        open(sys.argv[2], "rb").close()

    except:
        print("ERROR: Unknown hard error")

elif sys.argv[1] == "inp":
    while True:
        input("% ")

elif sys.argv[1] == "if":
    try:
        if sys.argv[3] == "is":
            if eval(sys.argv[2]) == eval(sys.argv[4]):
               print("yes")

            else:
                print("no")

        elif sys.argv[3] == "not":
            if eval(sys.argv[2]) != eval(sys.argv[4]):
                print("yes")

            else:
                print("no")

    except:
        print("ERROR: Unknown hard error")

elif sys.argv[1] == "lop":
    while True:
        print("loop")

else:
    print("ERROR:", sys.argv[1], "is not a valid function.")
