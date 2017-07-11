import os.path
import shutil

from pathlib import Path
from time import localtime, strftime

src = Path("../spoon-output")
dst = Path("../Results/" + strftime('%Y-%m-%d_%H_%M_%S/', localtime()))

def copytree(src, dst, symlinks=False, ignore=None):
    print("Copying...")
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)
    print("Complete.")

if src.exists():
    print("File found.")
    copytree(src, dst)
