#This is a single line comment in python
#For multi-line comments use # sign on each line
#To print anything on console in python, use - print()
print("hello python")
print(2+3)

#Python expressions consists of values(like 2, "hello", 3.14) & operators(like +, -, *, /) & they always evaluate down to single values
print(5+9)
print("hello" + " python")
print(4*5)
#first 5+9 is evaluated, that is 14. 14/7 = 2.0
print((5+9)/7)
#prints 16.0, First 7+1=8, then 3-1=2 , then 8/2=4.0 , then 5-1=4 , then 4*4.0=16.0
print((5-1)*((7+1)/(3-1)))

#A single value with no operators is also an expression
print(99)
print(45.67)

#Python does not requires semi-colons to terminate statements like other programming languages
#Semi colons can be used to delimit statements if you wish to put multiple statements on single line
#Python standard - do not use semi-colons at end of statements

#Python 2 , you can use print " " without paranthesis also - like >>>print "hello world" or >>>print("hello world"). Both are correct
#From python 3 onwards, print() is a function. Hence always use >>>print("Hello World") with paranthesis

#Always save your python code as .py extension
#To run python code in atom, use - ctrl+shift+B , but first install "script" package
#To install "Script", goto - Packages --> Settings View --> Install packages/Themes --> Install --> search "script" --> click Install

#To run python code from command prompt, type - python filename.py

#calling print() with nothing inside it will put a blank line on the screen
print("this is line 1")
print()
print()
print("this is line 2, after 2 blank print()")
