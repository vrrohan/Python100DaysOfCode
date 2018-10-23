#+ is used to concatenate 2 or more Strings
print("Alice " + "Bob")
name = "Rohan"
state = "Delhi"
country = "India"
print("Username is : " + name + "\nCurrently living in : " + state + ", " + country)

#You cannot add string & a integer, it will give - TypeError : must be str, not int
#info = "Your age is " + 22;     #TypeError
#print(info)

#when using both inside print() either use , or convert int value to string values
print("Your age is : ", 22)

#To convert int value to string use - str()
age = 17
print("Your age is : " + str(age))

#To take input from user , use - input()
name = input("Please enter your name : ")
print("Nice to meet you : " + name)

#But input() returns value in form of string
age = input("Enter you age : ")
#age is of string type else, it will give TypeError on using with +
print("Your age is : " + age)

#To convert string to integer, use - int()
ageAfter5Years = int(age) + 5
#Since it is a integer now, we need to convert it back to string
print("Your age after 5 years will be : " + str(ageAfter5Years))

#With python, you can use + operator only to add two integers or floats or concatenate 2 Strings
#You cannot add (String+integer) in python, unlike in java.
#For string+integer, you have to use str() or int() methods
print(int("5"))

#If you pass string value to int() which cannot be converted back to integer, it will give ValueError : invalid interal for int
#i.e. "hello" cannot be converted back to some integer value
#print(int("hello")) will give TypeError

#Similarly float() - it will return float form of the values you passed
print(float(99))
print(float(-55))
print(float(0))

#passing value that cannot be converted back to float will give - ValueError, "python" cannot be converted into float
#print(float("python"))

#type() returns type of literal(or value) that is passed. type() returns bool i.e. either true or false (not string type)
print(type(5))                  #prints <int>
print(type(99.55))              #prints <float>
print(type('hello python'))     #prints <str>
print(type(True))               #prints <bool>

#so before converting illegal types for TypeError, always check values that are passed using - is
#since type() returns type of value that was passed, using type() + is = returns bool , which is again not of type str
#hence to concatenate both , convert bool value back to str type
print("Is 5 an integer : " + str((type(5) is int)))
print("Is 99.55 a float : " + str((type(99.55) is float)))
print("Is 'hello python' a string object : " + str((type("hello python") is str)))

#Hence 4 methods we see - str(), int(), float(), type()
#1. str() converts passed value back to string type
#2. int() converts passed value back to integer type. Gives TypeError for string values
#3. float() converts passed value back to float type. Gives TypeError for string values
#4. type() returns type of value that was passed
print(str(29))
print(str(-99) + " type is " + str(type(str(-99))))
print(int(3.14))
print(int(-0.99))
print(float(10))
print(str(-3.14) + " type is " + str(type(str(-3.14))))

#There is another type in python named as bool having only 2 values, either - True or false
#For integers- 0 is False, else everything is True
print(bool(-33))        #True
print(bool(1))          #True
print(bool(0))          #False

#For string - "" empty string is False, else everything is true
print(bool("hello"))    #True
print(bool(""))         #False

#For floats - 0.0 is False, else everything is True
print(bool(-3.14))      #True
print(bool(4.55))       #True
print(bool(0.0))        #False
print(bool())           #False

#To get length of string use - len(), pass string inside len() methods
#len() returns integer i.e. number of characters in string including space
name = input("Enter your name : ")
#Since , we cannot concatenate string + integer , we need to cast result of len() back to string using str()
print("name length is : " + str(len(name)))
#length of empty string is 0
print(len(''))

#Both integer & floats are numbers while Strings are text
#Hence, 42 & 42.00 both are same, while 42 & '42' are different
print("42==42.0 : " + str(42==42.0))                    #True
print("42=='42' : " + str(42=='42'))                    #False
print("42.0==0042.000 : " + str(42.0==0042.000))        #True

#title() - displays each word in title case i.e. mark wayne --> Mark Wayne, where each word begins with a capital letter
name = "mark wayne rooney"
#prints - Mark Wayne Rooney
print("Name is : " + name.title())
