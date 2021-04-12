import os
from sys import argv

os.system("git clone https://github.com/Ganesha2282882/blang.git blangpkg-env")
os.chdir("blangpkg-env")
os.system("git checkout modpit")
os.system("make getblang")

for pkg in argv[1:]:
  os.system("patch < {}.diff".format(pkg))

os.system("make")
