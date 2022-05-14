#
#!A cross platform translate tool made by python
#
# Licensed under the GNU GENERAL PUBLIC LICENSE
#
# Copyright (C) 2022-present, SongZihui-sudo.
#
# @author      SongZihui-suao
# @file        install.py
#
import platform
import os

def main():
    print("installing")
    try:
        # linux
        if platform.system() == "Linux":
            print("system: linux\n")
            os.system("sudo pyinstaller -F transer.py")
            os.system("cp transer.png ./dist/")
            os.system("cp config.json ./dist/")
        # windows
        elif platform.system() == "Windows":
            print("system: windows\n")
            os.system("pyinstaller -F transer.py")
            os.system("copy \".transer.png\" \".\dist\\\"")
            os.system("copy \"config.json\" \".\dist\\\"")
        # mac
        elif platform.system() == "macos":
            print("system: macos\n")
            # i don'n have mac env
        else:
            print("other system\n")
    except:
        print("install error!")
    return 0
main()