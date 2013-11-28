import sys
from cx_Freeze import setup, Executable

setup(
    name = "Renamer",
    version = "0.1",
    description = "Program for the bulk renaming of files in an ordered manner",
    executables = [Executable("Renamer.py", base = "Console")])