#To iterate over dictionary items {key-value pairs} use - items()
#items() - returns list of key-value pairs in tuple form
info = {'name':'mark', 'age':22, 'address':{'country':'usa', 'state':'LA', 'pincode':12345}}
"""
name  :  mark
age  :  22
address  :  {'country': 'usa', 'state': 'LA', 'pincode': 12345}
"""
for (k,v) in info.items() :
    print(k , " : " , v)

#Accesing key-value pairs with indexes using enumerate()
"""
('name', 'mark') present at index 0
('age', 22) present at index 1
('address', {'country': 'usa', 'state': 'LA', 'pincode': 12345}) present at index 2
"""
for (index,pairs) in enumerate(info.items()) :
    print(str(pairs) + ' present at index ' + str(index))

#Accesing key-value pair using in operator
#By default only keys are accessed if simple dictionary_name is used
for pairs in info :
    print(pairs, end= ' ')                          #name age address
print()

#To access dictionary value we need - dictionary_name[key-name]
"""
name:mark
age:22
address:{'country': 'usa', 'state': 'LA', 'pincode': 12345}
"""
for pairs in info :
    print(str(pairs) + ':' + str(info[pairs]))

#To access only keys, use - dictionary_name.keys()
info = {'name':'mark', 'age':22, 'address':{'country':'usa', 'state':'LA', 'pincode':12345}}
print(info.keys())                                  #dict_keys(['name', 'age', 'address'])
for k in info.keys() :
    print(k, end=', ')                              #name, age, address,
print()

#To access only values, use - dictionary_name.values()
print(info.values())                                #dict_values(['mark', 22, {'country': 'usa', 'state': 'LA', 'pincode': 12345}])
"""
mark
22
usa, LA, 12345,
"""
for val in info.values() :
    #If value itself is of type dict, print only values from that nested dictionary, Hence we need to check if nested dictionary present or not
    if type(val) == dict :
        for v in val.values() : print(v, end=', ')
    else :
        print(val)
print()

#If we not check for nested dictionary, both key-value pair of nested dictionary will be printed
"""
mark
22
{'country': 'usa', 'state': 'LA', 'pincode': 12345}
"""
for val in info.values() :
    print(val)

#All keys(), values() & items() return list of keys or values or both, but returned value is not a actual list i.e. You cannot modify or append them
#To get the result in form of list use - list() i.e. wrap any 3 of these around list()
info = {'name':'mark', 'age':22, 'address':{'country':'usa', 'state':'LA', 'pincode':12345}}
listOfKeysInfo = list(info.keys())
print(listOfKeysInfo, ' type is : ', type(listOfKeysInfo))                      #['name', 'age', 'address']  type is :  <class 'list'>
listOfValuesInfo = list(info.values())
print(listOfValuesInfo)                                                         #['mark', 22, {'country': 'usa', 'state': 'LA', 'pincode': 12345}]
