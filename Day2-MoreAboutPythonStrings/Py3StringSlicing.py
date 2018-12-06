#You can obtain a sub-string from a string also known as string-slicing
#You can cut any portion of string & can obtain it using [:]
#s[m:n] - means cut string from index m till one position before index n i.e. m is included, n is excluded
name = "MontyPython"
print(name[2:5])        #prints- nty
print(name[0:9])        #prints- MontyPyth

#If you omit first index, slicing starts from begining of string
print(name[:5])         #prints- Monty
print(name[0:5])        #prints- Monty

#means s[:n] is equivalent to s[0:n]
#omiting 2nd index will result in slicing till last character of string
print(name[3:])         #prints- tyPython
print(name[3:11])       #prints- tyPython

#means s[m:] is equivalent to s[m:len(name)-1]
#omiting both first & 2nd index will slicing entire string from begining to end
print(name[:])          #prints- MontyPython

#name[:n] + name[n:] = name
newname = name[:3] + name[3:]
print(newname)          #prints- MontyPython

#giving 1st or 2nd index range outside of limit of length of string will not give any error
print(name[3:99])       #prints- tyPython
print(name[-12:6])      #prints- MontyP

#If the first index in a slice is greater than or equal to the second index, Python returns an empty string.
print(name[4:4])
print(name[8:3])

#negative indices can also be used to slice a string
print(name[-5:-2])      #prints- yth , omits character at index -2
print(name[-8:])        #prints- tyPython

#Another variant in string slicing is specifying the - stride i.e. how many characters to jump after retrieving each character in the slice
name = "MontyPythonCodes"
#Adding a 3rd additional index , designates a stride i.e. number of jumps or skips it need to do while slicing a string
#s[m:n:o] - slice from m till n & jump every o times
print(name[0:9:2])      #prints- Mnyyh , actually is - MontyPytho, but skipping every 2nd character means - M , skip o, n, skip t, y, skip P, y, skip t, h, skip o
print(name[3::3])       #prints- tyoos

numbers = "12345"*5
print(numbers[::5])     #prints- 11111
print(numbers[4::5])    #prints- 55555

#You can also use a negative stride to collect items in the opposite order.
#For example, the slicing expression "hello"[::−1] returns the new string "olleh"
#the first two bounds default to 0 and the length of the sequence
#stride of −1 indicates that the slice should go from right to left instead of the usual left to right. The effect, therefore, is to reverse the sequence
name = "HelloSpam"
print(name[::-1])                   #mapSolleH

#the slice S[5:1:−1] fetches the items from 2 to 5, in reverse order
#will start from index 5, goes till index 2 & goes in reverse order
print(name[5:1:-1])                 #Soll

#you can also reverse a string using this negative string slicing
name = "spam"
reverseName = name[::-1]
print("name is : " + name)                              #name is : spam
print("reverse of name is : " + reverseName)            #reverse of name is : maps

#slice string using slice(a,b) - a index included, b index excluded
name = "HelloPython"
print(name[slice(2,6)])                                 #prints- lloP
print(name[slice(None, None, -1)])                      #prints- nohtyPolleH

#Strings are immutable in python, it means they didn't change string itself. They return new string object
#To make a new string value from existing string, using string slicing & concatenation
s = "Spammy"
s = s[:3] + "xx" + s[5:]
#s[:3] makes Spa, s[5:] makes y
print(s)                    #Spaxxy
