import os
import subprocess

inter = "blang"
try:
    with open(".brepl_tmp", "wt") as tmpf:
        tmpf.write("say Found interpreter without input.")

    subprocess.call(["{}".format(inter), ".brepl_tmp"])

except:
    inter = input("interpreter => ")

while True:
    with open(".brepl_tmp", "wt") as tmpf:
        tmpf.write(input("=> "))

    os.system("{} .brepl_tmp".format(inter))