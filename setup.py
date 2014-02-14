import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"],"includes": ["OpenGL.platform.win32", "OpenGL.arrays.ctypesarrays", "OpenGL.arrays.numpymodule", "OpenGL.arrays.lists", "OpenGL.arrays.numbers"], "excludes": ["tkinter"], "include_files": ["gg\data"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = "Win32GUI"
#if sys.platform == "win64":
#    base = "Win64GUI"

setup(name="GG",
        version="0.1",
        description="GGgame!",
        options={"build_exe": build_exe_options},
        executables=[Executable("GGgame.py", base=base)])
