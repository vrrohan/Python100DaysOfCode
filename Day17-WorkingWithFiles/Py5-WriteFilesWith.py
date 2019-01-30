#using with keyword while writing to a file, so that no need to close the file again & again
import os
fileName = os.getcwd() + '\\withwrite.txt'

with open(fileName, 'w') as fo :
    fo.write('Hello Java\n')
    fo.write('Hello Python\n')
"""
Hello Java
Hello Python
"""

#Attempt to read from or write to a closed file will throw ValueError Exception
"""
fo = open(fileName, 'r')
fo.close()
fo.read()
ValueError: I/O operation on closed file.
"""

listFruits = ['Apple\n', 'Orange\n', 'Guava\n', 'Mango\n', 'Peach\n']
with open(fileName, 'a') as fo :
    for f in listFruits :
        fo.write(f)
"""
Hello Java
Hello Python
Apple
Orange
Guava
Mango
Peach
"""
