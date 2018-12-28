#you can sort a tuple using - sorted(tupleName)
#But sorted() returns a sorted list, to convert it back into tuple use - tuple(listName)
maps = (12, 5, 7, 19, 15, 8, 4)
print('before sorting : ', maps)                        #before sorting :  (12, 5, 7, 19, 15, 8, 4)
maps = tuple(sorted(maps))
print('after sorting : ', maps)                         #after sorting :  (4, 5, 7, 8, 12, 15, 19)

#By default, sorted(tupleName) sorts tuple in aescending order, to sort it into descending order use, sorted(reverse=True)
maps = (12, 5, 7, 19, 15, 8, 4)
revSortedMaps = tuple(sorted(maps, reverse=True))
print('reverse sorted : ', revSortedMaps)               #reverse sorted :  (19, 15, 12, 8, 7, 5, 4)

#To reverse a tuple we can use tuple slicing
maps = (12, 5, 7, 19, 15, 8, 4)
revMap = maps[::-1]
print('maps : ', maps)                                  #maps :  (12, 5, 7, 19, 15, 8, 4)
print('reverse maps : ', revMap)                        #reverse maps :  (4, 8, 15, 19, 7, 5, 12)

#Another way to reverse a tuple is to use built-in reversed()
#But reversed() returns a reverse iterator, which runs in reverse order
#We can use tuple concatenation to create a new reversed tuple
maps = (12, 5, 7, 19, 15, 8, 4)
newMaps = ()
for k in reversed(maps) :
    newMaps += (k,)

print('maps : ', maps)                                  #maps :  (12, 5, 7, 19, 15, 8, 4)
print('reverse maps : ', newMaps)                       #reverse maps :  (4, 8, 15, 19, 7, 5, 12)
