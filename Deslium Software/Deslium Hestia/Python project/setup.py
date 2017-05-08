import sys
from cx_Freeze import setup, Executable

setup(
    name = "doctors",
    version = "3.1",
    description = "For working with DB",
    executables = [Executable("doctors.py",base = "Win32GUI")])