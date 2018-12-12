#Just like integers, floating-point & string, there is another type in python - Boolean
#But unlike ints, floats & string objects, Boolean has only 2 values possible i.e. True or False (true/false is not Boolean, it is capital T)
spam = True
print(spam)                             #True
print(type(spam))                       #<class 'bool'>

#It is a syntax error when you try to assign True or False some values i.e. you cannot use True or False as variable names
#this true is not bool type
true = 'This is True'
print(true)

#This line will give error
#True = 'Boolean value'
#SyntaxError: can't assign to keyword

#Comparision operators are : ==, !=, <, >, <=, >=
#They evaluate to bool value either True or False
print(42==42)                   #True
print(2!=3)                     #True
print(5>8)                      #False
print(9!=9)                     #False

#integer and floating-point will always be unequal to a string value
print('hello'=='hello')         #True
print('hello'=='Hello')         #False
print(True==True)               #True
print(True!=False)              #True
print(42==42.0)                 #True
print(42=='42')                 #False

#>, <, <=, >= works only with integers, float values and string values
print(42<100)                   #True
myAge = 29
print(myAge>100)                #False

#You can use ( > , < , <= , <= , == , !=  ) to compare two strings. Python compares string lexicographically i.e using ASCII value of the characters.
#Suppose you have str1  as "Mary"  and str2  as "Mac" . The first two characters from str1  and str2 ( M  and M ) are compared.
#As they are equal, the second two characters are compared. Because they are also equal, the third two characters ( r  and c ) are compared.
#And because 'r'  has greater ASCII value than 'c' , str1  is greater than str2.
print('a'<'b')                  #True
print('Mary'>'Mac')             #True
#becus 'h' has ascii value of 104 and H has ascii value of 72, hence 104<72 is False
print('hello'<'Hello')          #False
#'hello' length is smaller than 'helloo' hence, True.
print('hello'<'helloo')         #True
print('teeth'<'tee')            #False

# == , checks if values on both sides are equal or not
# = , assigns value on right side to left side
#Boolean operator : and, or & not
#Binary boolean operator : and & or, that always takes 2 values
#(A and B): returns True if both are True, else always False
print("True and True : " + str(True and True))                  #True and True : True
print("True and False : " + str(True and False))                  #True and False : False

#(A or B): returns False if both are False, else returns True
print("True or False : " + str(True or False))                  #True or False : True
print("False or False : " + str(False or False))                #False or False : False

#not operator : operates only on one value , it evaluates to opposite boolean value
print("not True : " + str(not True))                            #not True : False
#you can nest not operator
print("not not not not True : " + str(not not not not True))    #not not not not True : True

#Mixing boolean and comparision operators
print("(4<5) and (5<6) is " + str((4<5) and (5<6)))             #(4<5) and (5<6) is True
print("(1==2) or (2==2) is " + str((1==2) or (2==2)))           #(1==2) or (2==2) is True

#Evaluation process of these expressions begin from left to right
#first 4<5 is evaluated to True ==> True and (5<6) ==> then 5<6 is evaluated ==> True and True ==> True
#output- (2+2==4) and not 2+2==5 and 2*2==2+2 is True
print("(2+2==4) and not 2+2==5 and 2*2==2+2 is " + str((2+2==4) and not 2+2==5 and 2*2==2+2))

#Python evaluation for boolean operators - not is evaluated first, then and & then or is evaluated
#Above expression - 2+2==4 is True ==> True and not 2+2==5 and 2*2==2+2 ==> then 2+2==5 ==> True and not False and 2*2==2+2 ==> 2*2==2+2 is True hence
#True and not False and True ==> not is evaluated first, hence, not False = True ==> True and True and True ==> True and True ==> True
