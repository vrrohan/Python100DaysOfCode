#All data in a Python program is represented by objects or relations between objects.
#Things like strings, lists, modules, and functions are all objects. There’s nothing particularly special about functions in Python.
#In Python Functions are first class objects, means you can store them into data structures like list, dictionary etc, pass as an argument to another function & many more
#Some properties of first-class functions are -
#1. Function is an instance of object type
#2. Can store function in a variable i.e. can assign a function to a variable
#3. Pass function as a parameter to another function
#4. We can return a function from another function
#5. We can store them into Data structures like list, dictionary, sets etc.

def foo(name) :
    return name.upper() + '!'

print(foo('rohan'))                                        #ROHAN!

#Because the yell function is an object in Python you can assign it to another variable, just like any other object
bar = foo

#Above line doesn’t call the function. It takes the function object referenced by yell and creates a second name pointing to it, bark.
#Now two names 'yell' & 'bark' points to same function object
#You can now execute the same underlying function object by calling bark
print(bar('guido'))                                        #GUIDO!

#Function objects and their names are two separate concerns. Here’s more proof: You can delete the function’s original name (yell).
del foo

#Because another name (bark) still points to the underlying function you can still call the function through it
#However calling yell will give NameError
print(bar('elon musk'))                                    #ELON MUSK!

"""
print(foo('elon musk'))
NameError: name 'yell' is not defined
"""

#Functions are objects of type - function
#Python attaches a string identifier to every function at creation time for debugging purposes. You can access this internal identifier with the __name__ attribute
print(bar.__name__)                                        #foo

#While the function’s __name__ is still “yell” that won’t affect how you can access it from your code. This identifier is merely a debugging aid.
#A variable pointing to a function and the function itself are two separate concerns.

#Python 3.3 there’s __qualname__ which serves a similar purpose and provides a qualified name string to disambiguate function and class names.
print(bar.__qualname__)                                    #foo

#Functions can be passed as an argument to another function. Because functions are objects, we can pass them as argument.
#Functions that accept other functions are arguments are called Higher Order functions.
def shout(text) :
    return text.upper()

def whisp(text) :
    return text.lower()

#Higher order function
def greet(func) :
    val = func('Hello Guido van Rossum')
    print(val)

greet(whisp)                                            #hello guido van rossum
greet(shout)                                            #HELLO GUIDO VAN ROSSUM

#Functions can return other functions also
def sumOfNumbers(x) :
    def add(y) :
        return x+y
    return add

#since, sumOfNumbers returns function & you can assign function to a variable
sum = sumOfNumbers(7)
print(sum)                                              #<function sumOfNumbers.<locals>.add at 0x000002071CEFEC80>
print(sum(10))                                          #17
print(sumOfNumbers(5)(3))                               #8
print(sumOfNumbers(100)(21))                            #121

#Another classical example of Higher order function is built-in map()
#map() takes 2 arguments, a function & any iterable like list, set or dictionary & calls function on each element of iterable
print(list(map(shout, ['mark', 'paul', 'wayne'])))                              #['MARK', 'PAUL', 'WAYNE']
