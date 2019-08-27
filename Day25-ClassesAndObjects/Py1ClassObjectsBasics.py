#We defined a class named Person, which doesn't do anything. Hence, it says pass
class Vehicle :
    pass

#All the methods in python take a first input variable called self, referring to the class itself. When you define a new method, you should always include the self, but when calling the method you should never include it.
#You can also write methods that don't take any input, but still will have the self in them
class Person :
    def __init__(self) :
        self.storedName = ''
        print('__init__() initiated...')

    def getName(self, name) :
        return str(name).upper()

    def welcomePerson(self) :
        print('Welcome to Person class')

    def storeName(self, name) :
        self.storedName = name

    def getStoredName(self) :
        print('Stored name is :', self.storedName)

per = Person()
print(per)
print(per.getName('elon musk'))
per.welcomePerson()

#Now store person name
per.storeName('Guido Rossum')
per.getStoredName()

#Since, storedName in self.storedName is created only when storeName() gets called first. If you try to invoke getStoredName() first, you will get error , since storedName class variable isn't created yet
"""
per2 = Person()
per2.getStoredName()
AttributeError: 'Person' object has no attribute 'storedName'
"""

#the method storeName takes one argument - name and stores it into the class variable storedName. Variables in the context of classes are called attributes in the context of a class.
#The method getStoredName just returns the stored property. we can also access the property - storedName directly, without the need to call the getName method.
#You can call storeName() method and create the storedName variable by passing argument and can access this variable directly using per object also
per = Person()
per.storeName('Bill Gates')
print(per.storedName)

#or, you can first create and initialize storedName variable directly without calling storeName() and then call getStoredName()
per = Person()
per.storedName = 'Python Django'
per.getStoredName()
