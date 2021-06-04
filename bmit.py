import sys
import os
import requests as reqs

argw = sys.argv
del argw[0]
try:
  os.mkdir("blang_modules")
  
except FileExistsError:
  pass

os.chdir("blang_modules")
modfileobj = open("{}.blang".format(argw[0]), "w")
modfileobj.write(reqs.get("https://raw.githubusercontent.com/blang-pl/blang-mod-repo/main/mods/{}.blang".format(argw[0]).content)
modfileobj.close()
os.chdir("..")
