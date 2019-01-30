#You can write to a file similar way print() writes string to screen
#You write to a file, we need append 'a' or 'w' mode
#w - write mode will overwrite everything in a file, it starts writing from a scratch
#a- append mode will start writing from end of file. Contents of file are not overwritten
#If filename, passed to open() doesnot exist, then both 'w' & 'a' will create a new blank file & will write contents to it
import os
fileName = os.getcwd() + '\\wtest.txt'

#By default with write(), we need to use \n character at end of string to write from a new line
#write() doesnot automatically adds a newline character to end of string like print(), you have to add it manually
fileObject = open(fileName, 'w')
fileObject.write('This is HTML.')
fileObject.write('HTML is tag language\n')
fileObject.write('Python is scripting language')
fileObject.close()
"""
This is HTML.HTML is tag language
Python is scripting language
"""

#To write multiple lines to a file, use - readlines()
newLines1 = ['\nManchester United\n', 'Barcelona\n', 'Real Madrid\n']
fileObject = open(fileName, 'a')
fileObject.writelines(newLines1)
fileObject.close()
"""
This is HTML.HTML is tag language
Python is scripting language
Manchester United
Barcelona
Real Madrid
"""

#writable() - returns True if file opened for writing i.e. if mode is 'w', 'a', 'r+' or 'a+'
fileObject = open(fileName, 'r+')
print(fileObject.writable())                                                    #True
fileObject.close()

#Python can only write strings to a text file, If you want to store any digits or numbers or type other than string, you need to convert that into string using str()
"""
fileObject.write(99)
TypeError: write() argument must be str, not int
"""
fileObject = open(fileName, 'a')
fileObject.write(str(3.14756859))
fileObject.close()
"""
This is HTML.HTML is tag language
Python is scripting language
Manchester United
Barcelona
Real Madrid
3.14756859
"""
