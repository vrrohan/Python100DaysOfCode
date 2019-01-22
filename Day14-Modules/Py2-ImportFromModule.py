#import imports the whole module to your current python code
#Sometimes you may choose to import only certain parts of your module using - from
#from {module-name} import {function or variable or anything}
from mymodule import num

print('sum of list is : ', sum(num))                                            #sum of list is :  140

#When using from imports, donot use moduleName while referring to elements of module, you can call that thing directly
#dir() - list all function names present in a module in sorted order
num = 99
color = 'Orange'
listOfTeams = ['France', 'Spain', 'England', 'Argentina']
def func1() :
    print('this is func1')

def func2() :
    print('this is func2')

#using dir() simply will list all names present in our current module(namespace)
print(dir())
"""
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'color', 'func1', 'func2', 'listOfTeams', 'num']
"""

#You can see, list of variables present in current module - num, color, listOfTeams
#Also function names - func1, func2
#All other names that begin with __ underscore are default python attributes associated with current module
#like __name__ returns name of your module

#There are two types of module - user defined modules & standard built-in Modules
#There one more way to import anything from a module at once, using - from {module-name} import *
from math import *
print(pi)                                                                       #3.141592653589793
print(e)                                                                        #2.718281828459045
print(sum([10, 20, 30, 40, 50]))                                                #150

#Using import * imports all names except those begining with underscore
#importing everything using * is generally considered as a bad practice

import mymodule2 as my2
"""
this is print statement 1
this is print statement 2
"""
#Since you can import statements also from your module
#There are 2 simple plain print statements in mymodule2 module, hence on import mymodule2 statement, it simply prints both statement
#You can see all functions & variables in mymodule2 using dir()
my2Names = dir(my2)
print(my2Names)                                                                 #['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'getCurrentTime', 'getSystemInfo', 'listOFNames', 'sys', 'time']

#You can see list of all names of functions & variable names present in mymodule2 module
print('current time is : ' + my2.getCurrentTime())                              #current time is : 17:47:46
print('current os version is : ' + my2.getSystemInfo())                         #current os version is : Windows 10
