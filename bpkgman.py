import os
from sys import argv

os.system("git clone https://github.com/Ganesha2282882/blang.git blangpkg-env")
os.chdir("blangpkg-env")
os.system("git checkout modpit")

for pkg in argv[1:]:
  os.system("patch < {}.diff".format(pkg))
