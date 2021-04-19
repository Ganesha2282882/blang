# access varlist as single function arg: varlist[":{}:".format(line[0][1:-1])]
# if input is variable: if line[0][0] == ":" and line[0][-1] == ":": 

import sys
import os

codef = open(sys.argv[1], "r+t")
code = codef.read()
codef.close()

lines = code.split("\n")

def nothing():
    pass

def readprog(prog):
    for line in prog:
        line.replace("\r", r"")
        line = line.split(" ")
        if line[0] == "say":
            del line[0]
            if line[0][0] == ":" and line[0][-1] == ":":
                for x in varlist[":{}:".format(line[0][1:-1])][0:]:
                    print(x, end="")
                 
                print()
                
            else:
                for x in line[0:]:
                    print(x, end=" ")

                print()

        elif line[0] == "add":
            del line[0]
            if line[0][0] == ":" and line[0][-1] == ":":
                 try:
                    print(float(varlist[":{}:".format(line[0][1:-1])]) + float(varlist[":{}:".format(line[1][1:-1])]))
                 
                 except:
                    print("ERROR: Unknown hard error")
                 
            else:
                try:
                    print(float(line[0]) + float(line[1]))

                except:
                    print("ERROR: Unknown hard error")

        elif line[0] == "mpy":
            del line[0]
            if line[0][0] == ":" and line[0][-1] == ":":
                try:
                    print(float(varlist[":{}:".format(line[0][1:-1])]) * float(varlist[":{}:".format(line[1][1:-1])]))
                
                except:
                    print("ERROR: Unknown hard error")
                    
            else:
                try:
                    print(float(line[0]) * float(line[1]))

                except:
                    print("ERROR: Unknown hard error")

        elif line[0] == "div":
            del line[0]
            if line[0][0] == ":" and line[0][-1] == ":":
                try:
                    print(float(varlist[":{}:".format(line[0][1:-1])]) / float(varlist[":{}:".format(line[1][1:-1])]))
                
                except:
                    print("ERROR: Unknown hard error")
            else:
                try:
                    print(float(line[0]) / float(line[1]))

                except:
                    print("ERROR: Unknown hard error")

        elif line[0] == "stt":
            del line[0]
            if line[0][0] == ":" and line[0][-1] == ":":
                try:
                    print(float(varlist[":{}:".format(line[0][1:-1])]) - float(varlist[":{}:".format(line[1][1:-1])]))
             
                except:
                    print("ERROR: Unknown hard error")
                    
            else:
                    try:
                        print(float(line[0]) - float(line[1]))

                    except:
                        print("ERROR: Unknown hard error")

        elif line[0] == "ram":
            del line[0]
            if line[0][0] == ":" and line[0][-1] == ":":
                try:
                    open(varlist[":{}:".format(line[0][1:-1])], "rb").close()
                    
                except:
                    print("ERROR: Unknown hard error")
            
            else:
                try:
                    open(line[0], "rb").close()

                except:
                    print("ERROR: Unknown hard error")

        elif line[0] == "inp":
            del line[0]
            if line[0][0] == ":" and line[0][-1] == ":": 
                varlist[":inputtext:"] = input(varlist[format(":{}:".format(line[0][1:-1] + " ")))
                
            else:
                varlist[":inputtext:"] = input(line[0])

        elif line[0] == "if":
            del line[0]
            try:
                if line[1] == "is":
                    if varlist[":{}:".format(line[0][1:-1])] == varlist[":{}:".format(line[2][1:-1])]:
                        readprog([" ".join(line[3:])])

                    else:
                        print("no")

                elif line[1] == "not":
                    if varlist[":{}:".format(line[0][1:-1])] != varlist[":{}:".format(line[2][1:-1])]:
                        readprog([" ".join(line[3:])])

                    else:
                        print("no")

            except:
                print("ERROR: Unknown hard error")

        elif line[0] == "lop":
            del line[0]
            while True:
                readprog([" ".join(line[0:])])

        elif line[0] == "\n":
            del line[0]
            nothing()

        elif line[0] == "":
            del line[0]
            nothing()

        elif line[0] == " ":
            del line[0]
            nothing()
        
        elif line[0] == "scl":
            del line[0]
            if line[0][0] == ":" and line[0][-1] == ":":
                systemcmd = varlist[":{}:".format(line[0][1:-1])]
                os.system(systemcmd)
                
            else:
                systemcmd = " ".join(line[0:])
                os.system(systemcmd)
        
        elif line[0] == "var":
            del line[0]
            varlist[":{}:".format(line[0])] = "{}".format(" ".join(line[1:]))

        else:
            print("ERROR:", line[0], "is not a valid function.")

varlist = {}
readprog(lines)
