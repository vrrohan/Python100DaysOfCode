#string formatting allows us to perform multiple type-specific substitutions on a string in a single step.
#string formatting also returns a new string object each time
#You can format a string by passing specific arguments values by position, by keyword or by relative position using format()
#'my' goes to position 0, 'red' goes to position 1
print("this is {0} {1} car".format('my', 'red'))            #this is my red car

stmt = "this is {} {} car".format('my', 'red')
print(stmt)                 #this is my red car

#formatting by position. mention position inside {} & format it by passing values at that position
stmt = "This is {0} big {1} {2}"
print(stmt.format(1, 'red', 'car'))             #This is 1 big red car

#formatting by keyword, mention keyword inside {} & pass values inside format()
stmt = "There are {number} big {color} {animal}"
print(stmt.format(number=3, color='blue', animal='whales'))             #There are 3 big blue whales

#formatting both by position & keyword
stmt = "There are {0} big {color} {1}"
print(stmt.format(2, 'horses', color='black'))                          #There are 2 big black horses

#you cannot use positional parameters after keyword argument, below both statement will cause SyntaxError: positional argument follows keyword argument
#print(stmt.format(2, color='black', 'horses'))
#print(stmt.format(color='black', 2, 'horses'))
#always use all positional arguments first, then use keyword argument

#using list in string formatting
stmt = "{0} team has total {1} members : {namesList}"
#Manchester United team has total 5 members : ['rooney', 'ronaldo', 'pogba', 'evra', 'rio']
print(stmt.format('Manchester United', 5, namesList=['rooney', 'ronaldo', 'pogba', 'evra', 'rio']))

#formatting by relative position
stmt = "there are {} big {} {}"
print(stmt.format(5, 'red', 'trucks'))                          #there are 5 big red trucks

#Number Formatting
#d - for integer, f - for floating point numbers
print("the number is : {:d}".format(123))                       #the number is : 123
#to pad 123 with leading whitespaces use (number)d
print("the number is : {:5d}".format(123))                      #the number is :   123
#to pad 123 with leading 0's till 5 places use, :0(number of padding)d
print("the number is : {:05d}".format(123))                     #the number is : 00123
#Formatting float numbers
print("the number is : {:f}".format(123.456789))                #the number is : 123.456789
#padding for 12 places with leading 3 0's - 9 digits + 1 for . + 3 0's = 13f
print("the number is : {:013f}".format(123.456789))
#formatting floats upto n digits after decimal using .n - n places after decimal
#10.3f means - f for float value, 10 means pad 123.456789 from left till 10 places, .3 means - display till 3 digits after decimal
print("the number is : {:10.3f}".format(123.456789))            #the number is :    123.457
#pad 123.456 with 0's & 2 digits after decimal
print("the number is : {:08.2f}".format(123.456))               #the number is : 00123.46

#Number formatting for signed numbers, use +f for positive float numbers or -f for negative float numbers or +d for positive integers or -d for negative integers
print("Positive number 22500 is : {:+d}".format(22500))         #Positive number 22500 is : +22500
print("Negative for 22500 is : {:-d}".format(-22500))           #Negative for 22500 is : -22500
print("Negative float -3.1476 is : {:-.2f}".format(-3.1476))    #Negative float -3.1476 is : -3.15
print("Positive float 55.658 is : {:+.2f}".format(55.658))      #Positive float 55.658 is : +55.66
#output- Positive float 22.546 & Negative float -3.145 is : +22.55, -3.15
print("Positive float 22.546 & Negative float -3.145 is : {:+.2f}, {:-.2f}".format(22.546, -3.145))

#using d with float types give ValueError: Unknown format code 'd' for object of type 'float'
#print("number : {:d}".format(3.14)) - this will give ValueError
#using f with integer types, will display integer in float type
print("number 25 used with f is : {:f}".format(25))             #number 25 used with f is : 25.000000

#formatting & displaying numbers using commas, inserts commas between every 3 digit groups. Use {:,d}
print("{:,d}".format(9999999))                      #9,999,999
print("{:,f}".format(1234.5678))                    #1,234.567800
print("{:,d} {:,d}".format(99999999, 8888888))      #99,999,999 8,888,888
print("{:,.2f}".format(1234.5678))                  #1,234.57

#To format decimal number in binary, octal & hexadecimal form use - {0:b} for binary, {0:o} for octal & {0:x} for hexadecimal
#0 is positional parameter here becus here we are formatting only one number = 12, which is at 0th position
number = 12
#output- binary(12)=1100, octal(12)=14, hexadecimal(12)=c
print("binary(12)={0:b}, octal(12)={0:o}, hexadecimal(12)={0:x}".format(number))

#By default, {:f} formats float values upto 6 places after decimal
print("value of pie is : {0:f}".format(3.14))       #value of pie is : 3.140000

#Number formatting with alignment
#By default using {:number d} example - {:5d} will align the number from right filling with whitespaces
#{:05d} will align the number from right filling with 0's
print("number right aligned to 5 : {:5d}".format(123))          #number right aligned to 5 :   123
print("number right aligned to 5 0's : {:05d}".format(123))     #number right aligned to 5 0's : 00123

#For left alignment, use <5d, will align the number to left filling remaining spaces with whitespace
#<05d will left align the number to left filling remaining spaces with 0's
print("number left aligned to 5 : {:<5d}".format(123))          #number left aligned to 5 : 123[whitespace][whitespace]
print("number left aligned to 5 : {:<05d}".format(123))         #number left aligned to 5 : 12300
print("number : {:<06d}".format(12))                            #number : 120000

#formatting strings with s
#will format string till 5 places from left
print("{:.5s}".format("caterpillar"))                   #cater
#for left alignment till 8 places
print("{:8.5s}".format("caterpillar"))                  #cater[ws][ws][ws]
print("{:<08.5s}".format("caterpillar"))                #cater000

#for right alignment, filled with 0's
print("{:>08.5s}".format("caterpillar"))                #000cater
print("{:*>8.5s}".format("caterpillar"))                #***cater

#for center alignment use ^
#.5s slice 5 characters from 'caterpillar' to 'cater'
#^11 means center align the word 'cater'
#*^11, fill it will *
print("{:*^11.5s}".format("caterpillar"))               #***cater***
