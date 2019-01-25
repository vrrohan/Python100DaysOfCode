#Though sets cannot contain mutable objects, sets itself are mutable i.e. you can add or remove elements from a set
colors = {'red', 'blue'}
colors.add('green')
colors.add(3.145)
print(colors)                                                                   #{'green', 3.145, 'blue', 'red'}
print(colors.pop(), 'is removed from colors')                                   #green is removed from colors
print(colors)                                                                   #{3.145, 'red', 'blue'}

#Frozen sets - are Immutable sets, similar like sets, but they cannot be changed
#You can create Frozenset by using frozenset(), pass setname as an argument to frozenset()
col = frozenset(colors)
print(col)                                                                      #frozenset({'red', 'blue', 'green'})
print(type(col))                                                                #<class 'frozenset'>

#adding or removing from frozenset will give AttributeError, as there is no add() or pop() or remove() in frozenset set
"""
col.add('newColor')
AttributeError: 'frozenset' object has no attribute 'add'
"""

#comparing 2 sets, using ==
set1 = {'a', 'e', 'i'}
set2 = {'b'}
set3 = {'i', 'a', 'e'}
print(set1==set2)                                                               #False
print(set1==set3)                                                               #True

#Since , sets doesn't maintain elements in any particular order, hence set1 & set3 both are same
#Copying a set
#Method1 : using = ,we can copy a set, but changes in any one set will reflect changes into another set also, its just like two names referring to same set
colors = {'red', 'blue', 'green', 'yellow'}
col = colors
print(colors)                                                                   #{'blue', 'green', 'yellow', 'red'}
print(col)                                                                      #{'blue', 'green', 'yellow', 'red'}
col.pop()
print(colors)                                                                   #{'blue', 'red', 'green'}
print(col)                                                                      #{'blue', 'red', 'green'}
colors.add(99)
print(colors)                                                                   #{99, 'green', 'red', 'yellow'}
print(col)                                                                      #{99, 'green', 'red', 'yellow'}

#Method2 : copy sets using copy(), but that creates shallow copy i.e. if sets itself contains any other set as an elements, that will copy just its reference
#It means copy() creates shallow copy & if inner set changes, that will be reflected in both outer sets
colors = {'red', 'blue', 'green', 'yellow'}
col = colors.copy()
print(colors)                                                                   #{'blue', 'red', 'green', 'yellow'}
print(col)                                                                      #{'blue', 'red', 'green', 'yellow'}
#sets doesnot support indexing or slicing
"""
print(colors[0])
TypeError: 'set' object does not support indexing
"""

#Method3 : copy sets using deepcopy()
import copy
colors = {'red', 'blue', 'green', 'yellow', ('tuple1', 'tuple2')}
col = copy.deepcopy(colors)
print(colors)                                                                   #{'yellow', 'green', 'red', 'blue', ('tuple1', 'tuple2')}
print(col)                                                                      #{'yellow', 'green', 'red', 'blue', ('tuple1', 'tuple2')}
