import os
import platform
import pathlib
from pip._internal.network.session import PipSession
import pkg_resources
import setuptools
import sys

os.system("clear" if platform.system() == "Linux" else "cls")
print("Before Starting, Auto-installing Python dependencies")
if platform.system() == "Linux":
    os.system(f"python3 -m pip install --upgrade -r requirements.txt")
else:
    os.system(f"python -m pip install --upgrade -r requirements.txt")
os.system("clear" if platform.system() == "Linux" else "cls")

if platform.system() == "Linux":
    os.system(f"python3 -m Nerinyan")
else:
    os.system(f"python -m Nerinyan")