#!/usr/bin/python3
import os

# Opening a file

fo = open("Resources/foo.txt","a")
print("Name of the file is", fo.name)
print(fo.name, "access mode is", fo.mode)
print("Status of ",fo.name,"is", fo.closed)

fo.write("\nwriting from the program is awesome!!")

fo.close()
print("Status of ", fo.name,"is", fo.closed)

fo1 = open("Resources/foo.txt","rb")
str1 = fo1.read(150)
print(str1)
count = fo1.tell()
print(count)
fo1.close()

os.rename("Resources/foo.txt","Resources/foo_Renamed.txt")
