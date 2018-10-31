#Python strings are indeed sequence of characters. You can access each character in string using [] , just like arrays in other programming langauges like java, c++ etc.
#Python string indexing starts with 0 till (length of string) - 1
#Python string indexing starts from end also. last element has index of -1, 2nd last has index of -2 & so on
name = "Manchester United"
print(name[0])          #prints- M
print(name[4])          #prints- h
print(name[11])         #prints- U

#last element has index len(str)-1
print(name[len(name)-1])        #prints- d
print(name[-1])                 #prints- d
print(name[-2])                 #prints- e
print(name[-8])                 #prints- r

#every string object has some limit i.e. 0 till len(str), you cannot access string characters outside that limit
#name = "Hello", accessing name[7] will give - IndexError: string index out range
name = "Hello"
#print(name[7]) will give - IndexError: string index out of range
#print(name[-12]) also gives IndexError

#Always remember, negative number indexing starts from last & it starts will -1
#positive number indexing starts from begining & it starts with 0

#updating a single character in string is not possible
name = "Python"
print(name)
#This line will give - TypeError: 'str' object does not support item assignment
#name[0] = 'J'
#print(name)

#update an entire string is possible, name changed from "Python" to "Jython"
name = "Jython"
print("new name is : " + name)

#you can also delete a string using del keyword
name = "Rohan"
print("name is : " + name)
#this deleted string named "name"
del name
#now since, name is deleted, using name with print will give - NameError: name 'name' is not defined
#print("after del, name is : " + name)

#similarly deleting single character in string is not possible
name = "Python"
print("lang is : " + name)
#This line will give, TypeError: 'str' object doesn't support item deletion
#del name[2]
