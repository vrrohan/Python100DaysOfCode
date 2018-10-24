#You can use single'' or double quotes"" with strings
message = "This is double quoted string"
message2 = 'this is single quoted string'
print(message)
print(message2)

#you can use single quotes with double quotes "''" or double quotes with single quotes '""'
#Always single or double quote, whosoever used at begin of string always that must end the string
#\ is used as escape character, character immidiate next to \ is not processed by python interpreter
quote1 = "He said- \"lets go for a walk\". And he went away."
print(quote1)

#In above string , if "He said- "lets go for a walk". And he went away."
#this line will give error, as when python starts processing this string, it starts from here - "He
#another double quotes"" he encounter at position just before lets - "lets
#quote2 = "He said- "lets go for a walk". And he went away."
#print(quote2)      #In that case, python will give syntax error as - SynataxError: invalid syntax

#To find length of string use len(), pass string as argument inside len()
name = "John Wayne"
print("length of name '" + name + "' is " + str(len(name)))

#Change string to all uppercase or lowercase
#upper() - changes all characters to uppercase
#lower() - changes all characters to lowercase
print("uppercase of name '" + name + "' is : " + name.upper())          #JOHN WAYNE
print("lowercase of name '" + name + "' is : " + name.lower())          #john wayne

#title() to display each word of string in title case
#Where each word begins with a capital letter
print("titlecase of name '" + name + "' is : " + name.title())          #John Wayne

#Stripping whitespaces from a string
#lstrip() - To remove whitespace from left of string
#rstrip() - To remove whitespace from right of string
#strip() -  To remove whitespace from both the ends
#This string contains 3 whitespaces at start, 5 whitespaces at middle & 2 whitespaces at end of string
teamname = "   Manchester     United  ";
print(teamname.lstrip())            #prints - "Manchester     United  "
print(teamname.rstrip())            #prints - "   Manchester     United"
print(teamname.strip())             #prints - "Manchester United"

#More about Syntax error - generally occurs when python doesn't recognize a section of your program as valid python code
#Example - using single apostrophe ' with single quotes gives - SynataxError
#If String starts with "" double quotes , python recognizes end of string  where next " appears
#If string starts with single ', python recognizes end of string where next ' appears
#Example - messg = "One of Python's main strength" #Ok
#Example - messg = 'One of python's main strength' #notok , as this will give syntax error

#String concatenation using +, you can add or concatenate 2 or more strings using + operator
team1 = "Manchester"
team2 = "Arsenal"
team3 = "Chelsea"
allTeamNames = team1 + ", " + team2 + ", " + team3;
print("names of all teams : " + allTeamNames)           #prints - "Manchester, Arsenal, Chelsea"

#* - creates multiple copies of string, use with integer value only
name = "Rohan"
print(name*3)           #prints- "RohanRohanRohan"
print(name*5)           #prints- "RohanRohanRohanRohanRohan"
print(name*0)           #prints- ""

# string = string * 0 - makes an empty string
name = name * 0;
print("after name=(name*0), name is " + name)

#using -ive values with string object also make string empty
name = "python"
print("name*-3 = " + (name*-3))

#at this point name is still - "python". To make it empty, re-assign it
print("name still : " + name)                                #prints- name still : python
name=name*-5;
print("after re-assignment name is : " + name)               #prints- after re-assignment name is :

#Remember you can only use integers with string mutiplication * operator, not even floats
#Using floats with (float * string) gives - TypeError : can't multiply sequence by non-int of type 'float'

#str() converts integer or float values back to string object
#using type() we can determine their type after conversion
age = 17
pie = 3.147
print("before conversion age is : " + str(type(age)))           #prints- before conversion age is : <class 'int'>
print("before conversion pie is : " + str(type(pie)))           #prints- before conversion pie is : <class 'float'>
age = str(age)
pie = str(pie)
print("after conversion age is : " + str(type(age)))            #prints- after conversion age is : <class 'str'>
print("after conversion pie is : " + str(type(pie)))            #prints- after conversion pie is : <class 'str'>

#ord() - converts character to integer Value
#It returns Ascii or Unicode value of input character i.e. 97 for a, 98 for b, 99 for c
print(ord('a'))         #97
print(ord('b'))         #98
print(ord('c'))         #99
#print(ord('')) will give error ,  as it expects some character inside ''
print(ord(' '))         #32
print(ord('A'))         #65
print(ord('D'))         #68

#chr() - converts integer to character
print(chr(97))          #a
print(chr(45))          #-
print(chr(32))          #(space)
print(chr(67))          #C
print(chr(68))          #D
