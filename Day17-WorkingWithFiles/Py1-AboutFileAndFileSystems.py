#A file has two key properties: a filename and a path. The path specifies the location of a file on the computer.
#For example, a file on Windows OS present in D drive, in folder Demo , filename is - test.py , the path will be - D:\Demo\test.py
#The part of the filename after the last period is called the file’s extension and tells you a file’s type.
#Example - .txt is a text file, .py is a python file, .docx is a Word document
#Folders can contain files and other folders.
#Example - file present at path - D:\Demo\Prim\test.py, Suppose Prim folder has 1 file test.py & 1 folder \bin
#The D:\ part of the path is the root folder, which contains all other folders.
#On Windows, the root folder is named C:\ and is also called the C: drive. On OS X and Linux, the root folder is /.

#Also note that while folder names and filenames are not case sensitive on Windows and OS X, they are case sensitive on Linux.
#The os module in python provides functions for interacting with the operating system. os, comes under Python’s standard utility modules.
#This module provides a portable way of using operating system dependent functionality. The os and os.path modules include many functions to interact with the file system.
import os
#name - gives the name of the operating system dependent module imported.
print(os.name)                                                                  #nt

#cwd() - returns current working directory
print(os.getcwd())                                                              #C:\github\python\MyModules

#chdir(path) - changes path from current working directory to the path we specify
os.chdir('D:\\github')
print(os.getcwd())                                                              #C:\github

#Python will display an error if you try to change to a directory that does not exist.
"""
There is no hello folder in C drive
os.chdir('C:\\hello')
FileNotFoundError: [WinError 2] The system cannot find the file specified: 'C:\\hello'
"""
#Backslash on Windows and Forward Slash on OS X and Linux
#On Windows, paths are written using backslashes (\) as the separator between folder names. OS X and Linux, however, use the forward slash (/) as their path separator.
#If you want your programs to work on all operating systems, you will have to write your Python scripts to handle both cases.
#Fortunately, this is simple to do with the os.path.join() function. If you pass it the string values of individual file and folder names in your path, os.path.join() will return a string with a file path using the correct path separators.

print(os.path.join('usr', 'bin', 'spam'))                                       #usr\bin\spam

#Backslashes are doubled because each backslash needs to be escaped by another backslash character. If I had called this function on OS X or Linux, the string would have been 'usr/bin/spam'.
#The os.path.join() function is helpful if you need to create strings for filenames. These strings will be passed to several of the file-related functions
#For example, the following example joins names from a list of filenames to the end of a folder’s name
fileNames = ['hello.py', 'test.docx', 'car.jpg']
for f in fileNames :
    print(os.path.join('D:\\filetest\\test', f))
"""
D:\filetest\test\hello.py
D:\filetest\test\test.docx
D:\filetest\test\car.jpg
"""

#Absolute vs Relative Paths
#There are two ways to specify a file path - An absolute path, which always begins with the root folder, A relative path, which is relative to the program’s current working directory
#There are also the dot (.) and dot-dot (..) folders. These are not real folders but special names that can be used in a path.
#A single period (“dot”) for a folder name is shorthand for “this directory.” Two periods (“dot-dot”) means “the parent folder.”
print(os.getcwd())                                                              #D:\github
os.chdir('D:\\gitrohan\\py100')
print(os.getcwd())                                                              #D:\gitrohan\py100
#.. - means parent folder, Hence when you want to go back to parent folder, simply use ..
os.chdir('..')
print(os.getcwd())                                                              #D:\gitrohan

#Absolute path is full path name of folder or a file in form of string
os.chdir('D:\\gitrohan\\py100\\Day17-WorkingWithFiles')
print(os.getcwd())                                                              #D:\gitrohan\py100\Day17-WorkingWithFiles

#Create new folder or directory using makedirs(path)
#This will create desserts folder, then create waffles folder in Day17-WorkingWithFiles folder
#os.makedirs('D:\\gitrohan\\py100\\Day17-WorkingWithFiles\\desserts\\waffles')
"""
If you try to run this makedirs() on same path again, it will give FileExistsError
FileExistsError: [WinError 183] Cannot create a file when that file already exists: 'D:\\gitrohan\\py100\\Day17-WorkingWithFiles\\desserts\\waffles'
"""

#The os.path module contains many helpful functions related to filenames and file paths.
#For instance, you’ve already used os.path.join() to build paths in a way that will work on any operating system.
#Since os.path is a module inside the os module, you can import it by simply running import os

#Handling Absolute and Relative Paths
#The os.path module provides functions for returning the absolute path of a relative path and for checking whether a given path is an absolute path.
#Calling os.path.abspath(path) will return a string of the absolute path of the argument. This is an easy way to convert a relative path into an absolute one.
#Calling os.path.isabs(path) will return True if the argument is an absolute path and False if it is a relative path.
#Calling os.path.relpath(path, start) will return a string of a relative path from the start path to path. If start is not provided, the current working directory is used as the start path.

print(os.path.abspath('.'))                                                     #D:\gitrohan\py100\Day17-WorkingWithFiles
print(os.path.abspath('.\\desserts'))                                           #D:\gitrohan\py100\Day17-WorkingWithFiles\desserts
print(os.getcwd())                                                              #D:\gitrohan\py100\Day17-WorkingWithFiles

print(os.path.isabs('.'))                                                       #False
print(os.path.isabs(os.getcwd()))                                               #True

#os.path.relpath()
print(os.path.relpath('D:\\gitrohan\\py100\\Day17-WorkingWithFiles', 'D:\\gitrohan'))                           #py100\Day17-WorkingWithFiles
print(os.path.relpath('D:\\gitrohan\\py100\\Day17-WorkingWithFiles', 'D:'))                                     #.
print(os.path.relpath('D:\\gitrohan\\py100\\Day17-WorkingWithFiles', 'D:\\'))                                   #gitrohan\py100\Day17-WorkingWithFiles
print(os.path.relpath('D:\\gitrohan\\py100\\Day17-WorkingWithFiles', 'D:\\gitrohan\\py100\\Day17-WorkingWithFiles'))                                  #.
print(os.path.relpath('D:\\gitrohan\\py100\\Day17-WorkingWithFiles', 'D:\\gitrohan\\py100\\Day17-WorkingWithFiles\\desserts'))                        #..
print(os.path.relpath('D:\\gitrohan\\py100\\Day17-WorkingWithFiles', 'D:\\gitrohan\\py100\\Day17-WorkingWithFiles\\desserts\\waffles'))               #..\..

print(os.path.relpath('C:\\Windows', 'C:\\spam\\eggs'))                         #..\\..\\Windows
print(os.getcwd())                                                              #D:\gitrohan\py100\Day17-WorkingWithFiles

#Calling os.path.dirname(path) will return a string of everything that comes before the last slash in the path argument.
#Calling os.path.basename(path) will return a string of everything that comes after the last slash in the path argument.
#C:\Windows\System32\calc.exe, Dir name = C:\Windows\System32 , Base name = calc.exe
path = 'C:\\Windows\\System32\\calc.exe'
print(os.path.basename(path))                                                   #calc.exe
print(os.path.dirname(path))                                                    #C:\Windows\System32

#If you need a path’s dir name and base name together, you can just call os.path.split() to get a tuple value with these two strings, like so:
calcFilePath = 'C:\\Windows\\System32\\calc.exe'
print(os.path.split(calcFilePath))                                              #('C:\\Windows\\System32', 'calc.exe')

#Notice that you could create the same tuple by calling os.path.dirname() and os.path.basename() and placing their return values in a tuple.
print((os.path.dirname(calcFilePath), os.path.basename(calcFilePath)))          #('C:\\Windows\\System32', 'calc.exe')

#But os.path.split() is a nice shortcut if you need both values. Also, note that os.path.split() does not take a file path and return a list of strings of each folder.
#For that, use the split() string method and split on the string in os.sep. Recall from earlier that the os.sep variable is set to the correct folder-separating slash for the computer running the program.
calcFilePath = 'C:\\Windows\\System32\\calc.exe'
print(calcFilePath.split(os.path.sep))                                          #['C:', 'Windows', 'System32', 'calc.exe']

#Finding File Sizes and Folder Contents
#os.path module provides functions for finding the size of a file in bytes and the files and folders inside a given folder.
#Calling os.path.getsize(path) will return the size in bytes of the file in the path argument.
#Calling os.listdir(path) will return a list of filename strings for each file in the path argument.
print(os.path.getsize('D:\\gitrohan\\py100\\Day17-WorkingWithFiles\\test.txt'))                                 #1783
print(os.listdir('D:\\gitrohan\\py100\\Day17-WorkingWithFiles'))                                                #['desserts', 'Py1-AboutFileAndFileSystems.py', 'rohn-icon.bmp', 'test.txt']

#If I want to find the total size of all the files in this directory, I can use os.path.getsize() and os.listdir() together.
totalSize = 0
for filename in os.listdir('D:\\gitrohan\\py100\\Day17-WorkingWithFiles') :
    totalSize = totalSize + os.path.getsize(os.path.join('D:\\gitrohan\\py100\\Day17-WorkingWithFiles', filename))

print(totalSize)                                    #782939
#loop over each filename in the D:\\gitrohan\\py100\\Day17-WorkingWithFiles folder, the totalSize variable is incremented by the size of each file.
#os.path.join() to join the folder name with the current filename. The integer that os.path.getsize() returns is added to the value of totalSize.

#Checking Path Validity
#Many Python functions will crash with an error if you supply them with a
#path that does not exist. The os.path module provides functions to check
#whether a given path exists and whether it is a file or folder.
#Calling os.path.exists(path) will return True if the file or folder referred to in the argument exists and will return False if it does not exist.
#Calling os.path.isfile(path) will return True if the path argument existsand is a file and will return False otherwise.
#Calling os.path.isdir(path) will return True if the path argument existsand is a folder and will return False otherwise.
print(os.path.exists('C:\\Windows'))                                            #True
print(os.path.exists('C:\\some_made_up_folder'))                                #False
print(os.path.isdir('C:\\Windows\\System32'))                                   #True
print(os.path.isfile('C:\\Windows\\System32'))                                  #False
print(os.path.isdir('C:\\Windows\\System32\\calc.exe'))                         #False
print(os.path.isfile('C:\\Windows\\System32\\calc.exe'))                        #True
