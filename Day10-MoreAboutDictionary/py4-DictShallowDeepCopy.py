info = {'name':'Guido', 'age':25, 'salary':25000, 'address':{'state':'LA', 'country':'usa', 'zip':12345}}
print(info)

#Copying using =
#When = operator is used, a new reference to the original dictionary is created.
#Since, reference is created, change in new dictionary will affect original dictionary elements also
info2 = info
print(info2)                                            #{'name': 'Guido', 'age': 25, 'salary': 25000, 'address': {'state': 'LA', 'country': 'usa', 'zip': 12345}}
info2['age'] = 35
print(info)                                             #{'name': 'Guido', 'age': 35, 'salary': 25000, 'address': {'state': 'LA', 'country': 'usa', 'zip': 12345}}
print(info2)                                            #{'name': 'Guido', 'age': 35, 'salary': 25000, 'address': {'state': 'LA', 'country': 'usa', 'zip': 12345}}
info2['address']['state'] = 'San Fran'
print(info)                                             #{'name': 'Guido', 'age': 35, 'salary': 25000, 'address': {'state': 'San Fran', 'country': 'usa', 'zip': 12345}}
print(info2)                                            #{'name': 'Guido', 'age': 35, 'salary': 25000, 'address': {'state': 'San Fran', 'country': 'usa', 'zip': 12345}}

#Copying dictionary using copy()
#When copy() method is used, a new dictionary is created which is filled with a copy of the references from the original dictionary.
print('copy()\n---------------')
info = {'name':'Guido', 'age':25, 'salary':25000, 'address':{'state':'LA', 'country':'usa', 'zip':12345}}
info2 = info.copy()
print(info)                                             #{'name': 'Guido', 'age': 25, 'salary': 25000, 'address': {'state': 'LA', 'country': 'usa', 'zip': 12345}}
print(info2)                                            #{'name': 'Guido', 'age': 25, 'salary': 25000, 'address': {'state': 'LA', 'country': 'usa', 'zip': 12345}}

#Now changing new dictionary will not change contents or elements of original dictionary
info2['age']=35
info2['name']='NewName'
print(info)                                             #{'name': 'Guido', 'age': 25, 'salary': 25000, 'address': {'state': 'LA', 'country': 'usa', 'zip': 12345}}
print(info2)                                            #{'name': 'NewName', 'age': 35, 'salary': 25000, 'address': {'state': 'LA', 'country': 'usa', 'zip': 12345}}

#copy() returns shallow copy of the dictionary, means all elements are copied into new dictionary & if it contains another list, tuple, any object or dictionary it creates a reference to original
#when dictionary contains another dictionary, list, tuples or any other object, there it creates a reference to original
#So, change in that inner dictionary will affect change in original inner dictionary
#Here, since address is itself a dictionary, it creates a reference into info2 dictionary, so zip of both info & info2 is changed
info2['address']['zip'] = 99999
print(info['address'])                                  #{'state': 'LA', 'country': 'usa', 'zip': 99999}
print(info2['address'])                                 #{'state': 'LA', 'country': 'usa', 'zip': 99999}

#Using copy module's deepcopy()
#deepcopy() - creates & returns a deep copy of original dictionary
#so even if dictionary contains some other dictionary or list, change in one dictionary will not affect change in original dictionary
import copy
info = {'name':'Guido', 'age':25, 'salary':25000, 'address':{'state':'LA', 'country':'usa', 'zip':12345}}
info2 = copy.deepcopy(info)
print(info)                                             #{'name': 'Guido', 'age': 25, 'salary': 25000, 'address': {'state': 'LA', 'country': 'usa', 'zip': 12345}}
print(info2)                                            #{'name': 'Guido', 'age': 25, 'salary': 25000, 'address': {'state': 'LA', 'country': 'usa', 'zip': 12345}}
info2.pop('address')
print(info)                                             #{'name': 'Guido', 'age': 25, 'salary': 25000, 'address': {'state': 'LA', 'country': 'usa', 'zip': 12345}}
print(info2)                                            #{'name': 'Guido', 'age': 25, 'salary': 25000}
