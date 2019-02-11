#To read a file, we use open(), we can either read the whole file at once, or we can read file line by line
import os
path = os.getcwd() + '\\script.py'
print(open(path).read())
"""
import sys
print(sys.path)
num = 2
print(num**2)

"""

#readline() will read file line by line saving space in memory, readline() when at end of file, empty string is returned, which we can detect to break out of loop
#file also works like an iterator, they have method __next__, which returns next line from a file each time it is called
#only difference between readline() & __next__() is, next() returns StopIteration exception at end of file
f = open(path)
print(f)                                                                        #<_io.TextIOWrapper name='D:\\gitrohan\\py100\\Day22-Iterators\\script.py' mode='r' encoding='cp1252'>
print(next(f))
"""
import sys

"""

print(next(f))
"""
print(sys.path)

"""
print(f.__next__())
"""
num = 2

"""
print(f.__next__())
"""
print(num**2)

"""
#Space is added at the end of each line, after calling next() or __next__()
print('----------')
for line in open(path) :
    print(line)
"""
import sys

print(sys.path)

num = 2

print(num**2)

"""
#we can read a file using while loop also, but it is slow
#Automatiic iteration using this above for loop, while manual iteration using next() or __next__()
#To simplyfy manual iteration, python 3 provides built-in next() which automatically calls __next__()
#When for loop begins, it first obtains an iterator from iterable object by passing it to iter()
#iter() internally calls __iter__()
