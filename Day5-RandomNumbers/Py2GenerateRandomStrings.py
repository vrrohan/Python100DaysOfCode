import random
import string

#To generate random string of length 5 of only lowercase letters
list = string.ascii_lowercase
randomString = ''
for i in range(5) :
    randomString+=random.choice(list)
print('Random string is : ' + randomString)                     #Random string is : nqsyf

#To generate random string of length 5 including both lowercase and uppercase letters
listUpper = string.ascii_letters
randomString = ''
for i in range(5) :
    randomString+=random.choice(listUpper)
print('Random string of both uppercase & lowercase is : ' + randomString)                   #Random string of both uppercase & lowercase is : ykJKW

#To generate random string of non-repeated characters use random.sample()
#sample() returns list of non-repeated items, so cannot use + to concatenate
#so, use join() to get non-repeated strings
listBoth = string.ascii_letters
nonRepeatString = ''
#sample(list of items, length of string)
nonRepeatString = nonRepeatString.join(random.sample(listBoth, 10))
print('Random string with no repeated characters : ' + str(nonRepeatString))                #Random string with no repeated characters : JSIprnXlfB

#sample() : ValueError If the sample size is larger than the population (i.e. list or set) size
"""
alphabet_list = ["a","b","c","e","f"]
print ("random.sample() value error ", random.sample(alphabet_list,15))
ValueError: Sample larger than population or is negative
"""
#sample() : TypeError if any of the two arguments is missing.
"""
alphabet_list = ["a","b","c","e","f"]
print ("random.sample() value error ",random.sample(alphabet_list))
TypeError: sample() missing 1 required positional argument: 'k'
"""

#Generate a random string from specific letters only
strList = 'asdfqwerty'
strSpec = ''
for i in range(5) :
    strSpec += random.choice(strList)
print('Random string with few specific letters only : ' + strSpec)                          #Random string with few specific letters only : aatqs

#Generate random string with both letters & digits
listAll = string.ascii_letters + string.digits
strAll = ''
for i in range(5) :
    strAll += random.choice(listAll)
print('Random string of both letters & digits are : ' + strAll)                             #Random string of both letters & digits are : kj72r

#Generate a random password string with Special characters, letters, and digits
#Generally Strong passwords have good minimum length (around min of 8) & combination of special characters, letters & digits
#You can generate these kinds of string in 2 ways -
#1) use combination of string.ascii_letters, string.digits, string.punctuation
#2) or, simply use string.printable, which contains all lowercase, uppercase, digits & special characters

#Approach 1
listOfAll = string.ascii_letters + string.digits + string.punctuation
specString = ''
#creating a special Password string of minimum length 8
for i in range(8) :
    specString += random.choice(listAll)
print('Random password string : ' + specString)
"""
Output1:- Random password string : keJ05lnw
Output2:- Random password string : K70TPi5j
Output3:- Random password string : 2E1DCxPU
"""

#Approach 2 - using string.printable [contains whitespace & newline(\n) character also]
listOfAll = string.printable
specPassString = ''
#creating special password string minimum length of 10
for i in range(10) :
    specPassString += random.choice(listOfAll)
print('Random Special password string : ' + specPassString)
"""
Output1:- Random Special password string : n;qGHVCA$W
Output2:- Random Special password string : hA%9noT8n_
Output3:- Random Special password string : a}ys[,n.s~
"""
