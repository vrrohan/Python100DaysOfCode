#To get python to open & work with any directory present at any location in system, you need to provide a filepath, which tells python to look in specific location on your system
#My current working directory - Day17-WorkingWithFiles --> desserts --> waffles --> any.txt
#You can use relative path, to open a file present in waffles folder from current working directory i.e. Day17-WorkingWithFiles
#Relative file path tells python to look for a given location relative to the directory where current running file is stored
#You can use \\ double backward slash or / single forward slash for filepaths
with open('desserts/waffles/any.txt') as fo :
    print(fo.read().rstrip())
"""
Hello Python
Hello HTML
Hello Java
Hello C++
"""

#This means - look for any.txt in folder desserts in folder waffles & python assumes desserts folder located in Day17-WorkingWithFiles folder
#You can also tell python excatly where the file is on your system, regardless of where the program thats being executed is stored, this is called - Absolute file path
filePath = 'E:\other.txt'
with open(filePath, 'r') as fo :
    print(fo.read().rstrip())
"""
Hello line 1
Hello line 2
Python
Hello line 3
"""
#using absolute path, you can read files from any location on your system

#Read entire text file line by line - more memory efficient as it reads line by line, not reads entire file at once
with open('desserts/waffles/any.txt') as fo :
    for line in fo :
        print(line.rstrip())
"""
Hello Python
Hello HTML
Hello Java
Hello C++
"""
