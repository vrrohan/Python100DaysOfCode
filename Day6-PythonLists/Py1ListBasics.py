#In Python, list is a type of container in Data Structures, which is used to store multiple data at the same time.
#You can store as many data in the list.
#A list begins with an opening square bracket and ends with a closing square bracket, []. Values inside the list are also called items. Items are separated with comma.
list_of_fruits = ['apple', 'orange', 'pineapple', 'grapes', 'guava']

#A list can store more that 1 Data Type items
list_of_items = [3, 5, 9, 'apple', 3.14, True, False, 'orange']

#A list can store other list also
list_of_address = ['bangalore', 'india']
list_of_info = ['mark', 'wayne', 27, list_of_address]

#Empty List
listEmpty = []

#list with None data type
noneList = [None]

#To print a list, use print
print(list_of_fruits)                           #['apple', 'orange', 'pineapple', 'grapes', 'guava']
print(list_of_items)                            #[3, 5, 9, 'apple', 3.14, True, False, 'orange']

#To get individual value from a list use [index]
#List Indexing starts with 0, so 1st element in a list is at index 0
list_of_cars = ['audi', 'porsche', 'ferrari', 'nissan', 'lamborgini']
print('car at index 2 in list is : ' + list_of_cars[2])                 #car at index 2 in list is : ferrari
print('car at index 3 in list is : ' + list_of_cars[3])                 #car at index 3 in list is : nissan

#Python will give you an IndexError error message if you use an index that exceeds the number of values in your list value.
"""
print(list_of_cars[9])
IndexError: list index out of range
"""

#Indexes can be only integer values, not floats. The following example will cause a TypeError error
"""
print(list_of_cars[2.0])
TypeError: list indices must be integers or slices, not float
"""
#But converting that float value back to int, will work
print(list_of_cars[int(2.0)])                   #ferrari
print(list_of_cars[int(2.6)])                   #ferrari

#Lists can also contain other list values. The values in these lists of lists can be accessed using multiple indexes
spam = [2, 4, 6, ['earth', 'mars', 'jupiter'], ['india', 'australia', 'japan', 'russia', 'france']]
#4th item in spam list is a list of planets
print("4th item in spam is a list : ", spam[3])                                 #4th item in spam is a list :  ['earth', 'mars', 'jupiter']
#To access 'mars', we use multiple []
#First [] access the list, 2nd [] access the item in the list
print('2nd item in list of planets is : ' + spam[3][1])                         #2nd item in list of planets is : mars

#You can access list elements using negative indexes also, -1 starts from back
list_of_cars = ['audi', 'porsche', 'ferrari', 'nissan', 'lamborgini']
print('last car in list is : ' + list_of_cars[-1])                              #last car in list is : lamborgini
print('3rd last car in list is : ' + list_of_cars[-3])                          #3rd last car in list is : ferrari
print(list_of_cars[-1] + ' is faster than ' + list_of_cars[-5])                 #lamborgini is faster than audi

#To get number of items in a list use - len(nameOfList)
print('Number of cars are : ', len(list_of_cars))                               #Number of cars are :  5
