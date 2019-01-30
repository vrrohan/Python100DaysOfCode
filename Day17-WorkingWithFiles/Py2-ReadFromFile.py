#Two types of files - Binary vs Text Files
#Text files includes simple text characters, that doesnot include font, size, images, pdf etc
#Binary files includes PDF's , images, spreadsheets etc Word file is a binary file - .jpg, .png or database file like .sqlite, .mdb, .pdf, .docx, .xls
#All above binary files require special type of software to open it. But text file has no specific encoding, can be opened in Text editor.
#3 steps to read/write files - call open(filename), call read() or write(), then call close()
import os
fileName = os.getcwd() + '\\test.txt'
#file_object = open(filename, mode) - Opens file in specified mode 'r' for reading, 'w' for writing, 'a' for append
#If you don't specify mode as 'r', then By default python lets you only read the data from the file. You cannot write or modify.
#read() - reads the entire content of files & return in string form
fileObject = open(fileName)
contents = fileObject.read()
print(contents)
"""
Know exactly what you want
This is line 2
This is line 3. Hello Python
This is line 4

"""
#Always close the file after reading or writing
fileObject.close()

#By default read() returns empty string when it reaches end of file, Hence extra blank line at the end of output from read()
#To avoid that you can use - rstrip(), which remove all whitespace characters from right of string
fileObject = open(fileName)
contents = fileObject.read()
print(contents.rstrip())
fileObject.close()
"""
Know exactly what you want
This is line 2
This is line 3. Hello Python
This is line 4
"""

#To read few characters, specify size inside read() as - read(size)
#read(size) - If file you are reading is longer than available memory, then you won't be able to access entire file at once
fileObject = open(fileName, 'r')
print(fileObject.read(12))                                                      #Know exactly
fileObject.close()

#To read file line by line use - readlines(), which return list of lines present in a file
fileObject = open(fileName, 'r')
print(fileObject.readlines())
fileObject.close()
"""
['Know exactly what you want\n', 'This is line 2\n', 'This is line 3. Hello Python\n', 'This is line 4\n']
"""

#Here 2 spaces , 1 becus of extra \n from each line + print() own \n character
fileObject = open(fileName, 'r')
for line in fileObject.readlines() :
    print(line)
fileObject.close()
"""
Know exactly what you want

This is line 2

This is line 3. Hello Python

This is line 4

"""

#Hence, use rstrip() to strip new line characters
fileObject = open(fileName, 'r')
for line in fileObject.readlines() :
    print(line.rstrip())
fileObject.close()
"""
Know exactly what you want
This is line 2
This is line 3. Hello Python
This is line 4
"""

#readline() will read & return single line by line starting from 1st line in a file , calling readline() 2nd time will return 2nd line in a file
fileObject = open(fileName, 'r')
print(fileObject.readline())
print(fileObject.readline())
fileObject.close()
"""
Know exactly what you want

This is line 2

"""

fileObject = open(fileName, 'r')
print(fileObject.readline().rstrip())
print(fileObject.readline().rstrip())
fileObject.close()
"""
Know exactly what you want
This is line 2
"""

#Read file line by line & also by line number
fileObject = open(fileName, 'r')
for (lineNumber, line) in enumerate(fileObject.readlines()) :
    print('line', lineNumber, ':', line.rstrip())
fileObject.close()
"""
line 0 : Know exactly what you want
line 1 : This is line 2
line 2 : This is line 3. Hello Python
line 3 : This is line 4
"""
