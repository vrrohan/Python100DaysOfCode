#Sets are unordered collection with no duplicate elements & enclosed with {}
#Sets contains only immutable elements i.e. you can add strings, numbers, tuples to a set but you cannot add mutable elements like list, dictionary
#Sets are implemented in a way, which doesn't allow mutable objects
#2 ways to create set - a) using set() b) using {}
colors = {'red', 'black', 'blue'}
print(colors)                                                                   #{'red', 'blue', 'black'}
print(type(colors))                                                             #<class 'set'>

#To create an empty set - use set(), not {} becus that will create an empty dictionary
s = set('aeiou')
print(s)                                                                        #{'a', 'i', 'o', 'e', 'u'}
s = set()
print(s)                                                                        #set()
s2 = {}
print(type(s))                                                                  #<class 'set'>
print(type(s2))                                                                 #<class 'dict'>

#Since, set doesn't allow duplicate elements, add same element which was already in set will not allow
colors = {'red', 'blue', 'black', 'yellow', 'blue', 'green', 'red'}
print(colors)                                                                   #{'blue', 'red', 'green', 'yellow', 'black'}

#len() returns number of elements in a set
print(len(colors))                                                              #5

#Membership of element in a set, checks whether element is present in set or not
print('elon' in colors)                                                         #False
print('red' in colors)                                                          #True
print('guido' not in colors)                                                    #True

#creating set from a list, using set()
listOfNames = ['elon', 'steve', 'mark', 'wayne', 'elon', 'mark']
print(listOfNames)                                                              #['elon', 'steve', 'mark', 'wayne', 'elon', 'mark']
setOfNames = set(listOfNames)
print(setOfNames)                                                               #{'wayne', 'steve', 'mark', 'elon'}

#creating set from a string
name = 'casablanca'
nameSet = set(name)
print(nameSet)                                                                  #{'b', 'a', 'n', 'c', 's', 'l'}

#Add elements to a set
setOfNames.add('newName')
setOfNames.add('wayne')
print(setOfNames)                                                               #{'wayne', 'newName', 'elon', 'mark', 'steve'}

#Iterate over a set using for-loop
for s in setOfNames :
    print(s, end=' ')                                                           #mark wayne elon newName steve

#sets doesnot support indexing or slicing
#You can iterate over sets using enumerate()
colors = {'red', 'blue', 'black', 'yellow', 'blue', 'green', 'red'}
for (colIndex, col) in enumerate(colors) :
    print('color', '{'+col+'}', 'present at index', colIndex)
"""
color {blue} present at index 0
color {green} present at index 1
color {red} present at index 2
color {black} present at index 3
color {yellow} present at index 4
"""
