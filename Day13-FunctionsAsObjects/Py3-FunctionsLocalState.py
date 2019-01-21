#Functions can contain inner functions & can also return them
#Not only functions return other functions, these inner function can also capture & carry some of the parents function state with them
def getSpeak(text, vol) :
    def whis() :
        return text.lower()

    def yell() :
        return text.upper()

    if (vol>50) :
        return yell
    else :
        return whis

        print(getSpeak('Hello Elon', 70)())                                             #HELLO ELON
print(getSpeak('Hello Elon', 70))                                               #<function getSpeak.<locals>.yell at 0x000002176C18EAE8>

#In above, whis() and yell(), text.lower() or text.upper() they capture & remember the value of text argument of getSpeak()
#Functions that do this are called Lexical closures or simply "closures"
#A closure remembers the value from its enclosing lexical scope, even program flow is no longer in that scope
def make(n) :
    def add(x) :
        return x+n
    return add

plus3 = make(3)
print(plus3(9))                                             #12
plus5 = make(10)
print(plus5(10))                                            #20

#make() serves as a factory to create and configure add()
#pass by reference or pass by value in function
#In python, every variable name is a reference, when we pass variable to a function, a new reference to object is created
def myFunc(lis) :
    lis[0] = -1

myList = [10, 20, 30]
print(myList)                                               #[10, 20, 30]

myFunc(myList)
print(myList)                                               #[-1, 20, 30]

#Since, arguments are passed by reference, change made by function will be reflected into original list, lis will reference to original function object
#To make separate copy of your list or if you don't want original list to get affected by person, use [:] slicing while function call
def myFunc2(lis) :
    lis[0] = -1

myList = [10, 20, 30]
print(myList)                                               #[10, 20, 30]

myFunc(myList[:])
print(myList)                                               #[10, 20, 30]
