from os.path import expanduser
import requests
from sys import argv
import zipfile
import os
home = expanduser("~")
os.chdir(home)
argw = argv[1:]
def nothing():
    pass

if argw[0] == "i":
    try:
        os.mkdir(".bvm")

    except FileExistsError:
        nothing()

    print("Downloading blang version {}...".format(argw[1]))
    open("blang.zip", "wb").write(requests.get("https://github.com/blang-pl/blang/archive/refs/tags/{}.zip".format(argw[1])).content)
    print("Installing blang version {}...".format(argw[1]))
    zipfile.ZipFile("blang.zip", "r").extractall(".bvm")
    os.remove("blang.zip")
    print("Installed. v/")

elif argw[0] == "s":
    cargs = " ".join(argv[3:])
    os.system("python .bvm/blang-{}/app.py {}".format(argw[1], cargs))