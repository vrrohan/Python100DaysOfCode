#when creating custom exception classes, your class must derive from Exception or BaseException class directly or in-directly
#In this case, AgeExceedException class is deriving from Exception class directly
#but , other two classes MarksLimitOutofRange and NameLengthTooShort exception class derive from Exception class in-directly, as they use - Error class, which in turn uses Exxception class directly.
class Error(BaseException) :
    pass

class AgeExceedException(Exception) :
    pass

class MarksLimitOutofRange(Error) :
    pass

class NameLengthTooShort(Error) :
    pass

name = str(input('enter name : '))
age = int(input('enter age : '))
marks = int(input('enter marks : '))
try :
    if age > 60 or age < 18 :
        raise AgeExceedException('Age limit execeed...')
    elif len(name) < 3 :
        raise NameLengthTooShort('Name is too short')
    elif marks > 100 or marks < 0 :
        raise MarksLimitOutofRange('marks cannot be less than 0 or greater than 100')
    else :
        print('name is', name, 'age is', age, 'marks is', marks)
except (AgeExceedException, NameLengthTooShort, MarksLimitOutofRange) as e :
    print(e)

#If you donot derive or inherit your class from Exception class , then it will throw an exception:- TypeError: catching classes that do not inherit from BaseException is not allowed
#You have to use - any one of the two classes - BaseException or Exception
#You can also use specific exception class in your custom exception class like - ValueError or TypeError or FileNotFoundError, but you need to handle only that particular exception
