#!/bin/python3
from pathlib import Path
import os

## Basic concatenate
myPath = str(Path('spam', 'bacon', 'egg'))
# winPath = str(WindowsPath('spam', 'bacon', 'egg'))
print("Basic concatenate:")
print(myPath)
print("\n------------------------------------------------------")

## Concatenate a list of path
myFiles = ['a.txt', 'b.txt', 'c.txt']
print("Concatenate a list of path")
for filename in myFiles:
    print(Path(r'~/someFolder', filename))
print("\n------------------------------------------------------")

## Use '/' to join path
# The only thing you need to keep in mind when using the / operator for
# joining paths is that one of the first two values must be a Path object.
slashPath = Path('slash') / 'a' / 'b' 
# not quite safe, can use sys.platform to judge the os and decide
# which slash to use
print('slashPath:', slashPath)
print("\n------------------------------------------------------")

## current working directory
print("Current and changed working directory")
currentPath = Path.cwd()
print('currentPath:', currentPath)
## change directory\
os.chdir(currentPath / ".." / "RegEx_Stuff")
changedPath = Path.cwd()
print("changedPath", changedPath)
os.chdir(currentPath / ".." / "RWFiles")
print("\n------------------------------------------------------")

## Home Directory
homeDir = Path.home()
print("homeDir:", homeDir)

## Make Directory
# os.makedirs("...") # this is to recursively make subdirectories
# Path(r'...').mkdir() # this just create one folder

## Components
compDir = Path.cwd() / "1.txt"
print("Path:", compDir)
print("Anchor:", compDir.anchor)
print("Parent:", compDir.parent)
print("Name:", compDir.name)
print("Stem:", compDir.stem)
print("Suffix:", compDir.suffix)
print("Drive:", compDir.drive)

# compDir = Path.cwd()
print("\n------------------------------------------------------")

## Parents
for i in range(len(str(compDir).split("/"))-1):
    print("Parent", i, compDir.parents[i])

print("\n------------------------------------------------------")

## Dir and Base Name
print("Dir and Base Name")
print("Dirname:",os.path.basename(currentPath))
print("Basename:",os.path.dirname(currentPath))
print("Split result:",os.path.split(currentPath))
print("Sep result:", str(currentPath).split(os.sep))
print("\n------------------------------------------------------")

# glob 
print("Glob")
p = Path('/home/ec2-user/environment/playground/pythonPlay/RWFiles')
for file in p.glob("*.txt"):
    print(file)
    
print("\n------------------------------------------------------")

#RW files
print("Read and Write Files")
print("simple way to interact")
p = Path("1.txt")
p.write_text("Hello, World!") #return number of characters being written
print(p.read_text())

print("\n------------------------------------------------------")


#open() 'w' 'r'
#read() 
#write()