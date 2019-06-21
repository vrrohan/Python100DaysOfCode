#python uses special objects called exceptions to manage errors that occur during program run-time
#If you handle the exception, program will continue running. if you don't program will be halted & traceback is shown
#In python exceptions are handled via try-except block
#ZeroDivisionError - print(5/0) this will give ZeroDivisionError exception. You cannot divide a number by 0 in python
try :
    num = int(input('Enter a number : '))
    print(10/num)
    print('exception handling line 1')
    print('exception handling line 2')
except ZeroDivisionError as zero :
    print('You cannot divide a number by 0')

#here zero is a variable that holds ZeroDivisionError - exception object , which arises due to line 7
#line which create exception will jump to except block & lines below that will never be albe to execute if exception occurs
#here line 8 & line 9 will never execute if exception arises.
#any code that depends on try-block executing successfully goes into else block. Hence, else block will execute if no exception occurs in try block
"""
try :
    #your code where exception can occur
except Exception :
    #your exception handling code
else :
    #code you want to run of no exception occur in try block
"""
try :
    num = int(input('Enter a number : '))
    print(10/num)
except ZeroDivisionError as zero :
    print('You cannot divide a number by 0')
else :
    print('exception handling line 1')
    print('exception handling line 2')

#one more block is there - finally block. Sometimes you want certain code to execute whether exception occurs or not. Put that code inside finally block
#like closing all resources whether exception occurs or not
try :
    num = int(input('Enter a number : '))
    print(10/num)
except ZeroDivisionError as zero :
    print('You cannot divide a number by 0')
else :
    print('exception handling line 1')
    print('exception handling line 2')
finally :
    print('finally block... closing all opened resources')

#Hence difference between else & finally block is - else block executes if no exception generates in try block i.e. try block runs successfully
#but finally will be executed, whether execption occured or not 
