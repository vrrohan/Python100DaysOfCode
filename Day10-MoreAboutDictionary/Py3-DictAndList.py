#Unlike list, Dictionary items are unordered.
#Lists are ordered, hence when comparing two lists using == order of items matter
list1 = ['cats', 'dogs', 'birds']
list2 = ['dogs', 'birds', 'cats']
#Becus both list have same elements but order of elements are different
print(list1==list2)                             #False
list1 = ['cats', 'dogs', 'birds']
list2 = ['cats', 'dogs', 'birds']
print(list1==list2)                             #True

#While dictionary are unordered
dict1 = {'name':'mark', 'country':'france', 'rank':2}
dict2 = {'country':'france', 'name':'mark', 'rank':2}
print(dict1==dict2)                             #True

#True, becus content is same, but order is different
#Since dictionaries are unordered, they can't be sliced like list
#Also, dictionary elements are accessed via key values not by any index offset value

#Check if a key or value is present in dictionary or not
userInfo = {'name':'rohan', 'age':25, 'country':'india'}
#Using in, in by default checks for key only
if 'address' in userInfo :
    print('address is present')
else :
    print('address is not present')                     #address is not present

#To check for values, use dictionary_name.values()
if 25 in userInfo.values() :
    print('age 25 found')                               #age 25 found
else :
    print('no age 25 found')

#Merging two dictionaries into one single dictionary
#Method1 : using update()
dict1 = {'a':1, 'e':5, 'i':9}
dict2 = {'b':2, 'd':4, 'e':-1, 'j':13}
dict1.update(dict2)
print(dict1)                                            #{'a': 1, 'e': -1, 'i': 9, 'b': 2, 'd': 4, 'j': 13}

#Merging two dictionaries using **
#This is generally considered a trick in Python where a single expression is used to merge two dictionaries and stored in a third dictionary.
#The single expression is **. This does not affect the other two dictionaries unlike update().
#Using this we first pass all the elements of the first dictionary into the third one and then pass the second dictionary into the third. This will replace the duplicate keys of the first dictionary.
#** are known as kwargs in python, means keyworded variable length arguments
dict1 = {'a':1, 'e':5, 'i':9}
dict2 = {'b':2, 'd':4, 'e':-1, 'j':13}
dict3 = {**dict1, **dict2}
print('dict1=', dict1)                                  #dict1= {'a': 1, 'e': 5, 'i': 9}
print('dict2=', dict2)                                  #dict2= {'b': 2, 'd': 4, 'e': -1, 'j': 13}
print('dict3=', dict3)                                  #dict3= {'a': 1, 'e': -1, 'i': 9, 'b': 2, 'd': 4, 'j': 13}

dict4 = {**dict1, 'foo':1, 'bar':2, **dict2}
print(dict4)                                            #{'a': 1, 'e': -1, 'i': 9, 'foo': 1, 'bar': 2, 'b': 2, 'd': 4, 'j': 13}
