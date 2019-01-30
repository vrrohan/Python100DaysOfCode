#To read a file - file_object = open(filename, mode), open() returns a file object that represents file & its contents
#Different modes in which you can open a file is - 'r' - reading mode(default mode), 'w' - writing mode, 'a' - append mode, 'r+' - read/write mode (file pointer at begining of file), 'a+' - append & read mode (file pointer placed at end of file)
#When working with binary files, you choose 'b' i.e. 'wb', 'rb', 'r+b', 'a+b'
import os
fileName = os.getcwd() + '\\withread.txt'

fileObject = open(fileName, 'r')
print(fileObject.read().rstrip())
fileObject.close()
"""
This is line 1 : python
This is line 2 : c++
This is line 3 : Java
HTML is at line 4
"""

#After every read() or write(), you have to call close file each, before working with or opening file again
#When your code gets larger, closing the file sometimes become messy or developer forget to close the file, in which case resources gets leaked
#Using with keyword, Python ensures your file resource will get automatically closed, developer no longer need to worry about closing the file
with open(fileName, 'r') as fileObject :
    print(fileObject.read().rstrip())
"""
This is line 1 : python
This is line 2 : c++
This is line 3 : Java
HTML is at line 4
"""

#Append each line in a file with --
linesInFile = []
#First read all lines & store it in a list i.e. 0th element of list contains line1 of file, 1st element is line number 2 in file
with open(fileName, 'r') as fileObject :
    for line in fileObject.readlines() :
        linesInFile.append(line)
#Now read each element of list one by one, append it will -- & store in a file, open the in write mode so that it starts writing from scratch
with open(fileName, 'w') as fileObject :
    for lines in linesInFile :
        fileObject.write('--' + lines)
"""
--This is line 1 : python
--This is line 2 : c++
--This is line 3 : Java
--HTML is at line 4
"""

#we can complete above task with single with keyword also , using mode 'r+' i.e. both read & write
linesInFile = []
with open(fileName, 'r+') as fileObject :
    #After reading & storing each line in a list
    for line in fileObject.readlines() :
        linesInFile.append(line)
    #Now write each line to a file
    for line in linesInFile :
        fileObject.write('++' + line)
"""
++--This is line 1 : python
++--This is line 2 : c++
++--This is line 3 : Java
++--HTML is at line 4
"""
