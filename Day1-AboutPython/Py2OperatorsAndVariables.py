#Few python operators are - +, -, *, /, **(Exponent), //(integer division), %(modulus)

#Additon(+), Subtraction(-), Multiplication(*), Division(/)
print(4+5)      #prints 9
print(8-3)      #prints 5
print(5+5-20)   #prints -10
print(9*9)      #prints 81

#python division / operator returns float value(decimal), even if both operands are of integer type
print(8/2)      #prints 4.0
print(8/2.0)    #prints 4.0
print(5/3)      #prints 1.666666666666667

#to get integer value from division use // integer division operator
print(8//2)     #prints 4
print(5//3)     #prints 1

#but if anyone one operand is of decimal (float) type, result will always be in decimal(float)
#both prints 4.0
print(8//2.0)
print(8.0//2)

#operators precedence from high to low (left to right)
#Exponent or power(**) --> Modulus(%) --> Integer division(//) --> Division(/) --> Multiplication(*) --> Subtraction(-) --> Additon(+)
#values inside () paranthesis always gets first preference

#** is Exponent operator i.e. x**y is y to power of x
print(3**3)     #prints 27
print(9**3)     #prints 729

#% is modulus operator
print(8%3)              #prints 2
print(23%7)             #prints 8
print(2+2**2%3)         #prints 3

#3 main python data types are - Integers, Floating point numbers, Strings
#Example of integers are : -2, -1, 0, 5, 9
#Example of floating numbers are : -0.5, -22.57, 0.0, 2.37
#Example of string are : 'a', "hello", 'welcome to python', "11th sept 2001"
#Anything within single or double quotes is a string
#'' is an empty string
quotes = ''
print("quote is : " + quotes)
quotes = "beautiful better than ugly..."
print("now quote is : " + quotes)

#to define variable in python, just name it with equals(=) sign & assign some value to it
#no need to define their data types
numA = 10
numB = 20
print("sum is : " , (numA+numB))    #prints 30

numC = numA/numB
print("division is : " , numC)      #prints 0.5

#Some rules regarding variable names in python are -
#1. Better practice to use only one world
#2. Can use letters, numbers & underscore(_)
#3. cannot start variable name with a number(or digit)
#4. Avoid using python reserved words as variable names
#5. Good practice to name variables in lowercase
#Some valid variable names are - bal, current_bal, _spam, account22
#Some invalid variable names are - current-bal(hyphens not allowed), current balance(spaces not allowed), 42people(cannot start with a number), total_sum$($ special character not allowed)
#Python variable names are case sensitive, so - spam, SPAM, sPaM, Spam, SPAm all are different
spam = "this is a spam mail"
SPAM = "this is BOLD spam mails"
print(spam + "\n" + SPAM)

#\n is a new line character - anything after \n will be displayed in a new line
print("hello is the line 1\nThis line will be next line\nThis line will be 3rd line")

#\t to add tab(4 or more spaces before) to your text, below line prints
#OOP languages are :
#	1. C++
#	2. Java
#	3. Python
#	4. C Sharp
#\n\t means - move to a new line & start next line with a tab
print("OOP languages are : \n\t1. C++\n\t2. Java\n\t3. Python\n\t4. C Sharp")
