#To add elements to a set using- add()
#Initially colors is an empty set
colors = set()
print(colors)                                                                   #set()

colors.add('blue')
colors.add('red')
colors.add('white')
print(colors)                                                                   #{'blue', 'red', 'white'}

#Sets are designed in such a way that you cannot add mutables as an element in sets
newColors = ['green', 'yellow', 'purple']
#Since, list is mutable type, you cannot add whole list as an element to a set
"""
colors.add(newColors)
TypeError: unhashable type: 'list'
"""
#So, you cannot add mutables like list, dictionary as an element in set
#But we can add immutables like string, tuples, numbers, floats as an element in set
colors.add(('green', 'yellow', 'cyan'))
print(colors)                                                                   #{'blue', 'red', 'white', ('green', 'yellow', 'cyan')}

#4th element in colors is a tuple

#clear() - remove all elements from the set
colors.clear()
print(colors)                                                                   #set()
colors = {'red', 'blue', 'green', 'black', 'pink'}

#pop() - removes & returns an arbitary element from set, if set if empty it raises KeyError
print(colors.pop())                                                             #pink
print(colors.pop())                                                             #blue

colors = set()
"""
print(colors.pop())
KeyError: 'pop from an empty set'
"""

#discard(e) - element e will be removed from set, if e is not present in set, nothing will be done
colors = {'red', 'blue', 'green', 'black', 'pink'}
colors.discard('blue')
colors.discard('white')
colors.discard('pink')
print(colors)                                                                   #{'black', 'green', 'red'}

#remove(e) - works just like discard, but if e element is not present in set, it raises KeyError
colors = {'black', 'green', 'red'}
colors.remove('black')
print(colors)                                                                   #{'red', 'green'}
"""
colors.remove('defi')
KeyError: 'defi'
"""
