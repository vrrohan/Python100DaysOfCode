#all() - returns True if all elements of set are True (or if set is empty)
col = set()
print(all(col))                                             #True
col = {'red', 'blue', 99}
print(all(col))                                             #True
col = {'red', 0}
print(all(col))                                             #False

#any() - returns True if any element of set is True, if set is empty returns False
col = {'', 0, 'hello'}
print(any(col))                                             #True
col = {'', None, 0}
print(any(col))                                             #False

#enumerate() - returns enumerate object, It returns (index, value) of all items of set as a pair
col = {'red', 'blue', 'green', 'white'}
colors = enumerate(col)
print(type(colors))                                                             #<class 'enumerate'>

for (colIndex,c) in colors :
    print('color', c, 'present at index', colIndex)
"""
color blue present at index 0
color red present at index 1
color green present at index 2
color white present at index 3
"""

#max() & min() return maximum & minimum element in a set
num = {23, 89, 45}
print(max(num))                                         #89
print(min(num))                                         #23

#sum() - returns sum of all elements in a set
print('sum is', sum(num))                               #sum is 157

#sort a set
num = {11, 66, 22, 88, 77, 44, 99, 33}
#sorted() - returns list of sorted set
sortedNum = sorted(num)
print(sortedNum)                                        #[11, 22, 33, 44, 66, 77, 88, 99]

#sorted() has attribute reverse=False, if you set reverse=True, it will sorted in reverse order & returns in form of list
sortedNumRev = sorted(num, reverse=True)
print(sortedNumRev)                                     #[99, 88, 77, 66, 44, 33, 22, 11]

#update() - updates & adds elements of set A(which is passed) to set B
#A.update(B)
setA = {11, 22, 33}
setB = {'hello'}
setA.update(setB)
print(setA)                                             #{33, 11, 22, 'hello'}

#To add elements of a list or dictionary
dictName = {'name':'elon', 'age':46}
#By default, only keys will be added to a set, dictName same as dictName.keys()
setA.update(dictName)
print(setA)                                             #{33, 'age', 'name', 22, 'hello', 11}
#To add, values of dictionary to a set, use dictName.value()
setA = {11, 22, 33}
setA.update(dictName.values())
print(setA)                                             #{33, 11, 46, 'elon', 22}
