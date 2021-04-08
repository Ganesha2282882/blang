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
        for x in line[0:]:
            print(x, end=" ")
            [ijohj y u yuku  uogiu i y uyguiyn9yg7 

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

    elif line[0] == "is":
        del line[0]
        try:
            if line[1] == "is":
                if str(line[0]) == str(line[2]):
                    print("yes")

                else:
                    print("no")

            elif line[1] == "not":
                if str(line[0]) != str(line[2]):
                    print("yes")

                else:
                    print("no")

        except:
            print("ERROR: Unknown hard error")

    elif line[0] == "lop":
        del line[0]
        while True:
            print("loop")

    elif line[0] == "\n":
        del line[0]
        nothing()

    elif line[0] == "\r\n":
        del line[0]
        nothing()

    elif line[0] == "":
        del line[0]
        nothing()

    else:
        print("ERROR:", line[0], "is not a valid function.")
