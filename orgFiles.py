#!/bin/python3

import shutil 
import send2trash
from pathlib import Path
import os

# os.mkdir("orgLab")
p = Path.cwd() / "orgLab"

#shutil.copy(source, destination) to copy file
shutil.copy((p / "src.txt"), (p / "dst.txt"))

# shutil.copytree(source, destination) to copy folder
# maybe need to judge whether dstFolder exists
# if (p / "dstFolder")
shutil.copytree((p / "srcFolder"), (p / "dstFolder"))

#move and rename files and folder
#shutil.move(src, dst)

# Permanently Deleting Files and Folders
# os.unlink(path)
# os.rmdir(path)
# shutil.rmtree(path)

# Safe Deletes with the send2trash Module
# Using send2trash is much safer than Python’s regular delete functions, 
# because it will send folders and files to your computer’s trash or 
# recycle bin instead of permanently deleting them.
# send2trash.send2trash(fileName)


# Walking a Directory Tree
# os.walk helps to iterate the path
# the os.walk() function will return three values on each iteration through the loop:
#   A string of the current folder’s name
#   A list of strings of the folders in the current folder
#   A list of strings of the files in the current folder
for folderName, subfolders, filenames in os.walk(p):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)

    print('')
    
    
