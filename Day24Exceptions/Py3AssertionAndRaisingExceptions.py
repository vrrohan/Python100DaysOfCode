import sys
#You can also raise an exception forcefully according to some conditions. That raised exception can be of any type - CustomException or In-built exceptions
#If you want to throw an error when certain conditions met, you can use - raise
num = int(input('enter number : '))
if num<5 :
    raise Exception('number less than 5')
else :
    print('number is ' + str(num))

#We can also assert that certain conditions are met. If conditions are true then it is ok, if it is false, program throw an AssertionError exception.
try :
    assert('linux' in sys.platform), "This platform is linux"
except AssertionError as ae :
    print('AssertionError : This platform is windows')

#remember, raise allows you to throw an exception at any time
#if there is function suppose A() which uses B() which inturn uses C(), and if exception occurs in function C().
#id exception is not handled in C(). exception goes back to B(), if there also exception isn't handled, then exception moves back to A(), even if there exception isn't handled, it will stops the execution of code & halts the program.
#also a try clause can have any number of except clause, but only one will be executed in case if exception arises
try :
    a = int(input('enter number : '))
    print(a)
    print(a/4)
    print(a+'hello')
except ValueError as ve :
    print('ValueError occurs')
except (TypeError, ZeroDivisionError) as tzde :
    print('TypeError or ZeroDivisionError occurs')

#ImportError - Raised when the import statement has troubles trying to load a module. Also raised when the “from list” in from ... import has a name that cannot be found.
#ModuleNotFoundError - A subclass of ImportError which is raised by import when a module could not be located. It is also raised when None is found in sys.modules.
#ModuleNotFoundError - when we try to import a module which is not present
"""
import hello
print('hello imported')
>>> import hello
>>> ModuleNotFoundError: No module named 'hello'
"""

#IndexError - when you try to access index which is out of range of list length
"""
lis = [1, 2, 3]
print(lis[99])
>>> print(lis[99])
>>> IndexError: list index out of range
"""
#KeyError - when a key is not found in dictionary

#NameError - Raised when a local or global variable name is not found

#StopIteration - Raised by built-in function next() and an iterator’s __next__() method to signal that there are no further items produced by the iterator.
