#An expression with two strings joined using in or not in will evaluate to a Boolean True or False.
#These expressions test whether the first string (the exact string, case sensitive) can be found within the second string.
name = "Hello World!"
print('Hello' in name)              #True
print('hello' in name)              #False
print('Wor' in name)                #True
print('' in  name)                  #True
print('cats' not in name)           #True
print(' ' not in name)              #False

#find(substring) method returns the lowest index of the substring if it is found in given string. If its is not found then it returns -1.
name = "xxxSPAMxSPAMxxSPAMSPAMxxxxSPAMx"
loc = name.find("SPAM")
print("SPAM lowest index is from : " + str(loc))            #SPAM lowest index is from : 3
loc = name.find("JULY")
print("JULY lowest index is from : " + str(loc))            #JULY lowest index is from : -1

#find() comes in two flavours, find(substring, startIndex) - will search 'substring' from startIndex till end of string.
#find(substring, startIndex, endIndex) - will search 'substring' from startIndex till endIndex
name = "Roses are red, red is a color. This car is also red"
locRed = name.find('red', 20)
#output- lowest index of 'red' substring after 20th index is : 48
print("lowest index of 'red' substring after 20th index is : " + str(locRed))
#this will search subsrting 'red' between index 12 & 50 only
locRed = name.find('red', 12, 50)
#output- lowest index of 'red' substring between 12th index & 50th index is : 15
print("lowest index of 'red' substring between 12th index & 50th index is : " + str(locRed))

#rfind(substring) method returns the highest index of the substring if found in given string. If not found then it returns -1.
name = "xxxSPAMxSPAMxxSPAMSPAMxxxxSPAMx"
loc = name.rfind("SPAM")
print("SPAM highest index is from : " + str(loc))            #SPAM highest index is from : 26
loc = name.rfind("x")
print("x highest index is from : " + str(loc))               #x highest index is from : 30

#rfind(subsrting, startIndex)
#will search 'SPAM' from index 7 till end of string
loc = name.rfind('SPAM', 7)
#output- highest index of substring 'SPAM' after index 7 is : 26
print("highest index of substring 'SPAM' after index 7 is : " + str(loc))

#rfind(substring, startIndex, endIndex) - will search for substring between startIndex(included) & endIndex(excluded)
#will search subsrting 'SPAM' between 7 & 21 : xxSPAMSPAM
#xx SPAM(starts at 14) SPAM(starts at 18), but since endIndex is excluded, it will not detect SPAM at index 18. Hence, 14 is returned
loc = name.rfind('SPAM', 7, 21)
#output- highest index of subsrting 'SPAM' between index 7 & 21 is : 14
print("highest index of subsrting 'SPAM' between index 7 & 21 is : " + str(loc))

#this time subsrting 'SPAM' is searched between index 7 & 3rd last index i.e. 'SPAMxxSPAMSPAMxxxxSP'
#negative index starts with -1 from end, hence AMx is not included
loc = name.rfind('SPAM', 7, -3)
#output- highest index of subsrting 'SPAM' between 7 & -3 is : 18
print("highest index of subsrting 'SPAM' between 7 & -3 is : " + str(loc))

#index(substring) - returns the position of the first occurrence of substring in a string. It raises ValueError exception if substring not found.
#both index() & find() does the same thing, but find() returns -1 if subsrting is not found, while index() raises an exception when subsrting is not found
line = "This car is red, red is a color, roses are also red"
posOfRed = line.index("red")
#output- first occurrence of substring 'red' is at index : 12
print("first occurrence of substring 'red' is at index : " + str(posOfRed))

#index(substring, startIndex, endIndex) - will return position of first occurrence of substring between startIndex(included) and endIndex(excluded)
posOfRed = line.index('red', 13, 30)
#output- first occurrence of subsrting 'red' between index 13 & 30 is : 17
print("first occurrence of subsrting 'red' between index 13 & 30 is : " + str(posOfRed))
