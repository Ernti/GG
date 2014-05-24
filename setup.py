import sys
import datetime
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os", "OpenGL", "OpenGL.platform"],"includes": ["re"], "excludes": ["tkinter"], "include_files": ["gg\data", "host"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = "Win32GUI"
#if sys.platform == "win64":
#    base = "Win64GUI"

now = datetime.datetime.now()

setup(name="GG",
        version="0.1." + now.strftime('%d%m%Y'),
        description="GGgame!",
        options={"build_exe": build_exe_options},
        executables=[Executable("GGgame.py", base=base)])
