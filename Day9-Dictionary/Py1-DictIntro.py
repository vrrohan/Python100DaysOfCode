#Dictionary is a collection of key-value pairs, enclosed within {}
#Each key in dictionary is associated with some value. They are sometimes called Associative Arrays becus each key is associated with some value
#Unlike lists, dictionary elements are not accessed via some offset value(only integers starting with 0), they are accessed by their keys & these keys can be of any type
#key & value pairs are separated by colon : {key:value}
#Empty dictionary
info = {}

#Dictionary with key-value pair
#Here keys are - 'name', 'age' & 'country' while values are - 'mark', 22, 'india'
info = {'name':'mark', 'age':22, 'country':'india'}

#Dictionary with integer keys
info = {1:'Spain', 2:'France', 3:'Germany'}

#Dictionary containing nested lists
info = {'name':'mark', 'age':22, 'hobbies':['reading', 'running', 'travel']}

#Dictionary with nested Dictionary
info = {'name':'mark', 'age':22, 'address':{'country':'usa', 'state':'LA', 'pincode':12345}}

#Creating Dictionary using zip(list-of-keys, list-of-values) passing two lists, one list contains key, other list contains values
#passing that zip() inside dict(zip([], [])), dict() creates a dictionary in python
info = dict(zip(['name','age','country'], ['mark', 22, 'usa']))
print(type(info))                                           #<class 'dict'>
print(info)                                                 #{'name': 'mark', 'age': 22, 'country': 'usa'}

#Creating Dictionary using dict.fromKeys()
#The dict.fromkeys() method returns a dictionary with the specified keys and value.
#fromKeys(someSequence, singleValue[optional]) - each value from sequence becomes key & each key is initialized with one singleValue. If no value is provided, each key initialized with - None
#Since no value is passed as 2nd argument in fromKeys(), each key will be assigned None
info = dict.fromkeys('rohan')
print(info)                                                 #{'r': None, 'o': None, 'h': None, 'a': None, 'n': None}
#Now each key initialized with 1
info = dict.fromkeys('rohan', 1)
print(info)                                                 #{'r': 1, 'o': 1, 'h': 1, 'a': 1, 'n': 1}
#creating dictionary from list of values using fromKeys()
listName = ['a', 'e', 'i', 'o', 'u']
info = dict.fromkeys(listName, 99)
print(info)                                                 #{'a': 99, 'e': 99, 'i': 99, 'o': 99, 'u': 99}

#To access Dictionary elements, we need to know its key using - dictionary_name[key-name]
info = {'name':'mark', 'age':22, 'country':'usa'}
print('name is : ' + info['name'])                          #name is : mark
print('age is : ' + str(info['age']))                       #age is : 22

#Trying to access a key, that doesn't exist in Dictionary gives - KeyError
"""
print(info['salary'])
KeyError: 'salary'
"""

#Accessing dictionary elements with nested list
info = {'name':'mark', 'age':22, 'hobbies':['reading', 'running', 'travel']}
print(info['hobbies'][2])                                   #travel
print(info['hobbies'][0])                                   #reading

#Accessing dictionary elements with nested dictionary
info = {'name':'mark', 'age':22, 'address':{'country':'usa', 'state':'LA', 'pincode':12345}}
print(info['address']['state'])                             #LA
print(info['address']['pincode'])                           #12345

#If a key is not present in dictionary & you access it, you will get a KeyError.
#In case, you don't know about the dictionary & try to access a key which is not present in dictionary or you want to avoid KeyError, use - get()
#get(key-name) returns None if key is not present in dictionary
info = {'name':'mark', 'age':22, 'address':{'country':'usa', 'state':'LA', 'pincode':12345}}
print(info.get('salary'))                                   #None
print(info.get('age'))                                      #22

#Another version of get(key, value) - In case you don't want None & want some other value to return if key is not present in dictionary
#Since, 'salary' key is not present in dictionary info, -1 is returned
print(info.get('salary', -1))                               #-1

#To get number of items (key-value pairs) in dictionary use - len(dictionary_name)
info = {'name':'mark', 'age':22, 'address':{'country':'usa', 'state':'LA', 'pincode':12345}}
print('length of info is : ' + str(len(info)))              #length of info is : 3

#We can access a value using key, To access a key using its value, we have 2 ways to do That
#Access dictionary key using dictionary value using list index()
#index() returns index of corresponding value in a list
info = {'name':'mark', 'age':22, 'address':{'country':'usa', 'state':'LA', 'pincode':12345}}
#Approach is - create two separate list of keys and values, so valuelist[0] contains its respective key at keylist[0], value at valuelist[2] contains its respective key at keylist[2]
#so first we need to know the index of that specific value, value present at that index, has its respective key at same index in keylist
listKeys = list(info.keys())
listValues = list(info.values())
print('22 has key :', listKeys[listValues.index(22)])                           #22 has key : age

#Method2 - Access key using dictionary value using items()
info = {'name':'mark', 'age':22, 'address':'usa'}

def getKey(val) :
    for k,v in info.items() :
        if v==val : return k

print('usa has key = ' + getKey('usa'))                                         #usa has key = address
