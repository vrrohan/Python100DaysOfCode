#A tuple is just an immutable list i.e. once created you cannot append, remove or change contents of tuple
#Tuples are enclosed with (), unlike [] for lists
#Tuples are immutable like Strings (List are mutables)
#Empty tuple
maps = ()

#Tuple with only 1 element
#If tuple has only 1 value, place a trailing comma after that value. Otherwise, python doesn't treat it like a Tuple
maps = ('hello',)
print(type(('maps')))                   #<class 'str'>
print(type(('maps',)))                  #<class 'tuple'>

#Tuple with 4 items
maps = ('hello', 22.5, True, 99)
print(maps)                             #('hello', 22.5, True, 99)

#Nested tuple
maps = ('Bob', ('dev', 'mgr'))

#paranthesis is optional, you can create tuple without including paranthesis also
maps = 'bob', 'alice',
print(maps, type(maps))                 #('bob', 'alice') <class 'tuple'>

#If you need an ordered sequence of values that never changes - use a tuple
#The commma is what lets python know this is a tuple value
#You can access elements of tuple via []
maps = ('hello', 'python', 3.14, 72, True)
print(maps[3])                          #72
print(maps[1])                          #python

#To get length of tuple use - len(tupleName)
print('length of maps is : ' + str(len(maps)))                  #length of maps is : 5

#Since, tuples are immutable, You cannot assign new value to tuple
#tuples don't have append() like lists
"""
maps[2] = 'newValue'
TypeError: 'tuple' object does not support item assignment
"""
#Although you cannot modify tuple, but you can assign new value to a variable that holds a tuple
dimensions = (200, 50)
print(dimensions)                                              #(200, 50)
dimensions = (400, 200)
print(dimensions)                                              #(400, 200)

#You can also convert a list to a tuple using tuple(listName)
names = ['john', 'wayne', 'paul', 'leo']
print(names, 'type is : ', type(names))                         #['john', 'wayne', 'paul', 'leo'] type is :  <class 'list'>
nameTup = tuple(names)
print(nameTup, 'type is : ', type(nameTup))                     #('john', 'wayne', 'paul', 'leo') type is :  <class 'tuple'>
