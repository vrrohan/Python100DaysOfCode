#A file containing set of functions, which you want to include in your application.
#Module is nothing but a file containing python code. To break larger coder in smaller manageable & organized code
#Modules help in organizing our code, makes code easy to maintain & place similar code at one place according to their functionality.
#Module names must end with .py extension

#We created a module named mymodule.py which contains 2 methods
import mymodule

#To access functions from mymodule, use - moduleName.functionName()
print(mymodule.greet('elon musk'))                                              #ELON MUSK!!!
print(mymodule.whisp('Guido Van Rossum'))                                       #guido van rossum...

#A module can contain variables also like a list, string, dictionary or any other variable.
#mymodule file contains variable num, which is of type list
print(mymodule.num[2])                                                          #9
print(mymodule.num[0])                                                          #1

newList = mymodule.num
for n in newList :
    print(n, end=', ')                                                          #1, 4, 9, 16, 25, 36, 49,

#Sometimes your module name is longer, in that case calling functionName with module name becomes too long for developer
#Typing larger code becomes boring so, you can create alias name for your module while importing
import mymodule as my
print(my.greet('elon musk'))

#There are several built-in standard modules also like - random, math, sys, datetime, time etc
import random as r
print(r.randint(0, 9))                                                          #5

import math as m
print('value of pi is :', m.pi)                                                 #value of pi is : 3.141592653589793
print('value of e is :', m.e)                                                   #value of e is : 2.718281828459045
