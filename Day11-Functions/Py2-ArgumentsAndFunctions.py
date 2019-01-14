#During function call, arguments are passed, while during function definition parameters are declared
#def calSum(a, b) : return a+b   ==> Function definition
#calSum(4,5) ==> Function call, so (a,b) are function parameters while (4,5) are arguments
#A function can have multiple parameters, here parameters are name & age
def getInfo(name, age) :
    print('This is person info')
    print('name is : ' + name.title())
    print('age is : ' + str(age))

#arguments are - 'guido van rossum' and 35
getInfo('guido van rossum', 35)

#Two types of arguments are there - Positional & Keyword based arguments
#Positional arguments- which need to be in same order as the order of parameters in function definition
#Keyword arguments- where each argument consist of a variable name & a value , order of arguments doesn't matter here
def getPersonInfo(name, age) :
    print('name is : ' + name.title())
    if age>18 :
        print(name.title() + ' eligible to vote')
    else :
        print(name.title() + ' not eligible to vote')

#order matters in Positional arguments or it will produce uneven results & may also give error
getPersonInfo('guido van rossum', 35)
"""
name is : Guido Van Rossum
Guido Van Rossum eligible to vote
"""
#arguments order changed, hence this will give AttributeError
"""
getPersonInfo(56, 'guido van rossum')
AttributeError: 'int' object has no attribute 'title'
"""

#Keyword arguments - when passing arguments during function call, you pass name value pair
#You directly associate name & value within argument, No issue of proper ordering your arguments
#argument name must be same as names of parameters in function definition
getPersonInfo(name='guido van rossum', age=35)
"""
name is : Guido Van Rossum
Guido Van Rossum eligible to vote
"""
getPersonInfo(age=17, name='elon ironman musk')
"""
name is : Elon Ironman Musk
Elon Ironman Musk not eligible to vote
"""

#Above we explicitly tell python to put 'guido van rossum' into name & 35 into age
#When you use keyword arguments, be sure to use the exact names of the parameters in the function’s definition.

#Default Arguments - When writing a function, you can define a default value for each parameter.
#If an argument for a parameter is provided in the function call, Python uses the argument value. If not, it uses the parameter’s default value.
def getPersonInfo(name, age=17) :
    print('name is : ' + name.title())
    if age>18 :
        print(name.title() + ' eligible to vote')
    else :
        print(name.title() + ' not eligible to vote')

#Here, python uses age default parameter value as 17
getPersonInfo('elon ironman musk')
"""
name is : Elon Ironman Musk
Elon Ironman Musk not eligible to vote
"""

#Here python uses age value as 45, 17 gets overriden
getPersonInfo('guido van rossum', 45)
"""
name is : Guido Van Rossum
Guido Van Rossum eligible to vote
"""

#When you use default values, any parameter with a default value needs to be listed after all the parameters that don’t have default values.
#This allows Python to continue interpreting positional arguments correctly.
"""
def getPersonInfo(age=17, name, city) :
    print('name is : ' + name.title())
    if age>18 :
        print(name.title() + ' eligible to vote')
    else :
        print(name.title() + ' not eligible to vote')

SyntaxError: non-default argument follows default argument
"""

#print() - used to print anything on console that was passed inside print()
#print() has optional parameter end and sep
#By default, print() automatically adds newline character to end of string that was passed
print('hello guido')                                            #hello guido
print('this statement is in new line')                          #this statement is in new line

#However, we can set end parameter ourself also
#Here end is no longer new line character, another print() will print statement after one space
print('hello guido', end=' ')                                   #hello guido new statement
print('new statement')

#end - when passing multiple string values to print() separated by comma, print automatically separates them with single space
print('cats', 'dogs', 'birds')                                  #cats dogs birds
#You can set end value also, how to separate your string values
print('cats', 'dogs', 'birds', sep=', ')                        #cats, dogs, birds

#Both end & sep act as default arguments in print(), if you don't pass anything end act as - end='\n' & sep act as - sep=' '

#Python passing variable number of arguments
#Python allows a function to collect an arbitrary number of arguments from the calling statement.
#For example, consider a function that builds a pizza. It needs to accept a number of toppings, but you can’t know ahead of time how many toppings a person will want.
#The function in the following example has one parameter, *toppings, but this parameter collects as many arguments as the calling line provides
def makePizza(*toppings) :
    print(toppings)

#*toppings tells Python to make an empty tuple called toppings and pack whatever values it receives into this tuple.
#Note that Python packs the arguments into a tuple, even if the function receives only one value
makePizza('green peppers')                                                      #('green peppers',)
makePizza('extra cheese', 'green peppers', 'mushrooms', 'olives')               #('extra cheese', 'green peppers', 'mushrooms', 'olives')

def makePizza(*toppings) :
    print('Make pizza with following toppings :')
    for tops in toppings :
        print('-', tops)

makePizza('green peppers')
"""
Make pizza with following toppings :
- green peppers
"""

makePizza('extra cheese', 'green peppers', 'mushrooms', 'olives')
"""
Make pizza with following toppings :
- extra cheese
- green peppers
- mushrooms
- olives
"""

#Mixing positional, keyword & varags(arbitrary number of arguments), always place positional parameters first, then keyword or arbitary arguments
def makePizza(pizzaPrice, *toppings, country='India') :
    print('country is', country, 'price is', pizzaPrice, 'toppings is', toppings)

def makePizza(pizzaPrice, country='India', *toppings) :
    print('country is', country, 'price is', pizzaPrice, 'toppings is', toppings)
