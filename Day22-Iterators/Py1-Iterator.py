num = [1, 2, 3, 4, 5]
for n in num :
    print(n, end=' ')                                                           #1 2 3 4 5
print()

#This for-in loop in python works with iterators only
#Objects that support the __iter__ & __next__  methods automatically work with for-in loops
#An iterator can be seen as pointer to a container example list, dictionary, sets etc , to access all elements of a container.
#for-in loops on python implicitly uses iterators
cities = ['paris', 'la', 'madrid', 'london']
for c in cities :
    print(c, end=' ')                                                           #paris la madrid london
print()

#Internally iter() is called on the iterable collection, return value of iter() is an iterable, we can iterate over this iterable using next()
#when iterable reaches end, it returns StopIteration Exception
cityIter = iter(cities)
print(cityIter)                                                                 #<list_iterator object at 0x0000022602EA6198>
print(next(cityIter))                                                           #paris
print(next(cityIter))                                                           #la

#Internally for-loop calls this next() & terminates when it gets StopIteration exception
cityIter = iter(cities)
while cityIter :
    try :
        print(next(cityIter), end=' ')
    except StopIteration :
        print('--list ended--')
        break
"""
paris la madrid london --list ended--
"""

#Incase of dictionary, iterator runs over keys of dictionary
#for-in loops work over any iterable object that scans elements from left to right
name = 'Monty Python'
for c in name :
    print(c, end=' ')                                                           #M o n t y   P y t h o n
print()

nameIter = iter(name)
print(next(nameIter))                                                           #M
print(next(nameIter))                                                           #o

#Python iterator object must implement __iter__() & __next__() [called as iterator protocol]
#An object is called iterable, if we get iterator from it example- list, strings, dictionary etc
#iter() - which Internally calls __iter__() returns an iterator
