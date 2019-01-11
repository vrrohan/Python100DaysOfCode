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
        print(name.title() + ' not eli')
