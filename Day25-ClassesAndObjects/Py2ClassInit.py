#How to initialize a class
#The instantiation of the class happened at the line - per = Person().
#You may have noticed that the property stored_name does not exist in the object until we assign a value to it.
#This can give very serious headaches if someone calls the method get_name before actually having a name stored (you can give it a try to see what happens!)
#Therefore it is very useful to run a default method when the class is first called. This method is called __init__ [which is similar to constructor in Java, self is equivalent to this operator in java]
class Person :
    """Creating a person class"""
    def __init__(self, name, age) :
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def displayPersonInfo(self) :
        """method that display person's information"""
        print('person name is', self.name, ',person age is', self.age)

    def getPersonAccess(self) :
        """method that displays whether person can access documents or not"""
        if self.age > 40 :
            print(self.name, 'can access documents.')
        else :
            print('person cannot access documents')

per = Person('elon', 48)
per2 = Person('bill', 35)
per.displayPersonInfo()
per2.displayPersonInfo()
per.getPersonAccess()
per2.getPersonAccess()

#triple quotes at starting of class and all methods acts like a docstring, which describes what this class is doing or method does.
#A function that’s part of a class is a method. Everything you learned about functions applies to methods as well; the only practical difference for now is the way we’ll call methods.
#The __init__() method at is a special method Python runs automatically whenever we create a new instance based on the Person class. This method has two leading underscores and two trailing underscores, a convention that helps prevent Python’s default method names from conflicting with your method names.

#We define the __init__() method to have three parameters: self, name and age. The self parameter is required in the method definition, and it must come first before the other parameters.
#It must be included in the definition because when Python calls this __init__() method later (to create an instance of Person), the method call will automatically pass the self argument.
#Every method call associated with a Person class automatically passes self, which is a reference to the instance itself; it gives the individual instance access to the attributes and methods in the class.

#When we make an instance of Person, Python will call the __init__() method from the Person class. We passed Person() a name and an age as arguments; self is passed automatically, so we don’t need to pass it.

#Any variable prefixed with self is available to every method in the class, and we’ll also be able to access these variables through any instance created from the class. self.name = name takes the value stored in the parameter name and stores it in the variable name, which is then attached to the instance being created.
#The same process happens with self.age = age. Variables that are accessible through instances like this are called attributes.
#The Person class has two other methods defined: displayPersonInfo() and getPersonAccess().
#Because these methods don’t need additional information like a name or age, we just define them to have one parameter, self. The instances we create later will have access to these methods. In other words, they’ll be able to sit and roll over.

per = Person('Mark', 27)
#When Python reads this line, it calls the __init__() method in Dog with the arguments 'Mark' and 27.
#The __init__() method creates an instance representing this particular person and sets the name and age attributes using the values we provided.
#The __init__() method has no explicit return statement, but Python automatically returns an instance representing this person. We store that instance in the variable per.

#To access the attributes of an instance, you use dot notation. we access the value of per attribute name by writing:
print(per.name)                             #Mark
per.name = 'NewName'
print(per.name)                             #NewName
