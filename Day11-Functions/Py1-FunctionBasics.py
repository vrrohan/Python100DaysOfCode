#Functions used to perform some task or some calculations based on some input & may return some value
#Some common code which needs to be called mutiple times in any code, put all that code in a function & then you only need to call that function by its name
#Another important property of a function is that they perform only one specific task. It is generally a good practice to perform only one specific task from your function.
#We have already learnt few functions like print(), len(), input() etc
#Functions in python start with def keyword followed by function-name, paranthesis & then colon(:)
#This is a function definition
def sayHello(name) :
    print('Hello ' + name)

#This function takes 1 argument & prints hello
#Thats function call
sayHello('Guido')                                   #Hello Guido
sayHello('Steve')                                   #Hello Steve

#Functions are used just to avoid code duplication
#Things inside paranthesis when function definition is called Parameter
#Values we pass when calling a function are called Arguments
#name is a Parameter, while 'Guido' is an Argument

#Functions also return some values like len(), input() etc
def getNameLength(name) :
    return len(name)

#Since function is returning some value, we need print() or some variable to store & display that returned value
print('length of Guido is : ', getNameLength('Guido'))                          #length of Guido is :  5
elonLen = getNameLength('Elon')
print('length of Elon is : ', elonLen)                                          #length of Elon is :  4

#You can return any value from function
#None Data type - None means absence of some value , type is NoneType data type
#print() is a function which returns None
s = print('Hello Python')                                                       #Hello Python
print(type(s))                                                                  #<class 'NoneType'>
print(s==None)                                                                  #True

#By Default Python adds - return None, to end of any function definition that has no return statement
#Even if you mention only - return , then also None is returned

#How to call function that returns some value
#Either you can store the value returned from that function & display that value using print
def getSquare(num) :
    return num*num

sqFive = getSquare(5)
sqNine = getSquare(9)
print(sqFive)                                           #25
print(sqNine)                                           #81

#or, you can directly display the value of that function using print()
#If you, call any function using print() then print() will display the returned value from that function
def greetMessage(name) :
    print('Welcome : ', name.title())

#Here greetMessage() is not returning any value, so you can directly call it without any print()
greetMessage('guido van rossum')                        #Welcome :  Guido Van Rossum

#Since, greetMessage() has no return value, hence Default value is None, so this print() first displays message, then display its return type
"""
Welcome :  Elon Musk
None
"""
print(greetMessage('elon musk'))
