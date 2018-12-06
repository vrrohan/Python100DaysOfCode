#To make replacement in string , use replace(olderSubstring, newSubstring)
#replace() returns a new string object each time
name = "xxxSPAMxxSPAMxxxxxSPAMx"
name = name.replace("SPAM", "MAPS")
print("name after replace() : " + name)                     #name after replace() : xxxMAPSxxMAPSxxxxxMAPSx

#replace also takes 3rd argument as how many substring to replace from start
name = "xxxxSPAMxxSPAMxSPAMxxxxxSPAMxxx"
#replace only the first 2 substrings
name = name.replace("SPAM", "MAPS", 2)
print("name after first 2 replacements : " + name)          #name after first 2 replacements : xxxxMAPSxxMAPSxSPAMxxxxxSPAMxxx

#Since string objects are immutable in python, both concatenation & replace() or any other methods return new string object each time you modify them
#If still you want to make many changes to a very large string, better to convert that string into a list using list()
name = "Hello Python"
nameList = list(name)
print("list is : " + str(nameList))

#once string is converted into list, you can make multiple changes to it without creating new copy each time
nameList[3] = 'X'
nameList[5] = 'X'
print("list is : " + str(nameList))                 #list is : ['H', 'e', 'l', 'X', 'o', 'X', 'P', 'y', 't', 'h', 'o', 'n']

#after all changes made to list, convert list back to string object using join()
name = ''.join(nameList)
print("list to string is : " + name)                #list to string is : HelXoXPython
print('SPAM'.join(['a','e','i','o','u']))           #aSPAMeSPAMiSPAMoSPAMu

#capitalize() - It returns a copy of the string with only its first character capitalized.
#title() makes 1st character of each word in Uppercase, while capitalize() makes only 1st character of 1st word in Uppercase
print("hello my name is rohan".capitalize())        #Hello my name is rohan

#max() is an inbuilt function that returns the highest alphabetical character in a string.
#max() is an inbuilt function that returns the highest alphabetical character in a string.
name = "Python"
print("max string is : " + max(name))               #max string is : y
print("min string is : " + min(name))               #min string is : P

#count() - returns the number of occurrences of a substring in the given string.
name = "Java is OOP, c++ is OOP, Python is OOP, html is not"
numberOfOOP = name.count("OOP")
print("number of OOP substring is : " + str(numberOfOOP))           #number of OOP substring is : 3
#count() also takes 2nd and 3rd argument, which indicates start & end index to search substring only with that limit
#count(subsrting, startIndex, endIndex) - will search substring between startIndex and endIndex only
numberOfOOP = name.count("OOP", 9, 40)
#number of OOP substring b/w 9th index & 40th index is : 2
print("number of OOP substring b/w 9th index & 40th index is : " + str(numberOfOOP))
