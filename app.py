import sys

codef = open(sys.argv[1], "r+t")
code = codef.read()
codef.close()

lines = code.split("\n")

def nothing():
    pass

for line in lines:
    line = line.split(" ")
    if line[0] == "say":
        del line[0]
        try:
            print(line[0], end=" ")

        except:
            nothing()

        try:
            print(line[1], end=" ")

        except:
            nothing()

        try:
            print(line[2], end=" ")

        except:
            nothing()

        print()

    elif line[0] == "add":
        del line[0]
        try:
            print(int(line[0]) + int(line[1]))

        except:
            print("ERROR: Unknown hard error")

    elif line[0] == "mpy":
        del line[0]
        try:
            print(int(line[0]) * int(line[1]))

        except:
            print("ERROR: Unknown hard error")

    elif line[0] == "div":
        del line[0]
        try:
            print(int(line[0]) / int(line[1]))

        except:
            print("ERROR: Unknown hard error")

    elif line[0] == "ta":
        del line[0]
        try:
            print(int(line[0]) - int(line[1]))

        except:
            print("ERROR: Unknown hard error")

    elif line[0] == "ram":
        del line[0]
        try:
            open(line[0], "rb").close()

        except:
            print("ERROR: Unknown hard error")

    elif line[0] == "inp":
        del line[0]
        while True:
            input("% ")

    elif line[0] == "if":
        del line[0]
        try:
            if line[1] == "is":
                if eval(line[0]) == eval(line[2]):
                    print("yes")

                else:
                    print("no")

            elif line[1] == "not":
                if eval(line[0]) != eval(line[2]):
                    print("yes")

                else:
                    print("no")

        except:
            print("ERROR: Unknown hard error")

    elif line[0] == "lop":
        del line[0]
        while True:
            print("loop")

    else:
        print("ERROR:", line[0], "is not a valid function.")
