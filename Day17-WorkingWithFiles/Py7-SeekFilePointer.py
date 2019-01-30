#File Seeks :- Moving the Read/Write Pointer
#Remember that when you write using the a+ mode, your file pointer is always going to be at the end of the file.
#If you use the fileobject.write() method, you’re not going to get anything in return. That’s because that method is looking after the pointer to find additional text.
#What you need to do then, is move the pointer back to the beginning of the file.
#The easiest way to do this is to use the fileobject.seek(offset, from_what) method. In this method, you put the pointer at a specific spot.
#The offset is the number of characters from the from_what parameter. The  from_what parameter has three possible values:
#0 – indicates the beginning of the file
#1 – indicates the current pointer position
#2 – indicates the end of the file
#When you’re working with text files (those that have been opened without a b in the mode), you can only use the default 0, or a seek(0, 2), which will take you to the end of the file.
#fileObject.seek(7, 0) on our file, you will place the pointer at the 8th character of the file (remember that Python starts counts at 0). 0 means from begin 8th character
import os
fileName = os.getcwd() + '\\withwrite.txt'
with open(fileName, 'r') as fo :
    fo.seek(7, 0)
    print(fo.read().rstrip())
"""
ython
Apple
Orange
"""

#If you want to check the current position of the pointer, you can use the  fileobject.tell() method, which returns a decimal value for where the pointer is at in the current file.
#If we want to find how long our current work_data file is, we can use tell()
with open(fileName, 'a') as fo :
    print(fo.tell())                                                            #29

with open(fileName, 'r') as fo :
    print(fo.tell())                                                            #0

with open(fileName, 'w') as fo :
    print(fo.tell())                                                            #0

#fo.tell() when mode is 'a' will tell the size of the file, becus pointer will be at the end of the file to append the data
