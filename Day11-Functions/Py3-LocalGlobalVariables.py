#Parameters and variables that are assigned in a called function are said to exist in that function’s local scope.
#Variables that are assigned outside all functions are said to exist in the global scope.
#A variable that exists in a local scope is called a local variable, while a variable that exists in the global scope is called a global variable. A variable must be one or the other; it cannot be both local and global.
name = 'python'
def getInfo(age) :
    city = 'manchester'
    print('age is', age)
    print('name is', name)
    print('city is', city)

getInfo(25)
"""
age is 25
name is python
city is manchester
"""

#Here, name is global variable, while city & age is local variable
#You cannot use age & city outside that function, while you can use name both inside & outside of that function
"""
print(city)
NameError: name 'city' is not defined
"""

#Think of a scope as a container for variables. When a scope is destroyed, all the values stored in the scope’s variables are forgotten.
#There is only one global scope, and it is created when your program begins. When your program terminates, the global scope is destroyed, and all its variables are forgotten.

#A local scope is created whenever a function is called. Any variables assigned in this function exist within the local scope.
#When the function returns, the local scope is destroyed, and these variables are forgotten.
#A local scope is created inside a function or inside for-loop or inside while-loop or inside if-condition

#A local scope is created whenever a function is called. Any variables assigned in this function exist within the local scope.
#When the function returns, the local scope is destroyed, and these variables are forgotten.

#Local Scopes Cannot Use Variables in Other Local Scopes
#A new local scope is created whenever a function is called, including when a function is called from another function.
def spam() :
    eggs = 99
    bacon()
    print(eggs)

def bacon() :
    ham = 101
    eggs = 0
    print('bacon ham=', ham, 'bacon eggs=', eggs)

#Here local variable of bacon() eggs=0 doesn't affect local variable of spam() eggs=99
#Local variable of one function is completely separated from local variable of another function
spam()
"""
bacon ham= 101 bacon eggs= 0
99
"""

#What happen if Both local & global variables have same name
name = 'elon musk'
def getInfo() :
    name = name.title()
    print(name)

"""
getInfo()
UnboundLocalError: local variable 'name' referenced before assignment
"""
#Becus when you try to access global var name inside getInfo(), python tries to create a new local variable - name, so when you try to access name.title(), it no longer access global name
#Despite, it tries to create a new local variable name & before that it is trying to access name.title(), which is not created yet, Hence UnboundLocalError error occurs

#To access a global variable inside any function , use global keyword inside function definition
#If you have a line such as global name at the top of a function, it tells Python, “In this function, name refers to the global variable, so don’t create a local variable with this name.”
def getInfo() :
    global name
    name = name.title()
    print(name)

getInfo()                                               #Elon Musk

#If both global & local variable have same name - then preference goes to local variable
name = 'elon musk2'
def getInfo(name) :
    print('name is', name)

getInfo('guido rossum')                                 #name is guido rossum

#
