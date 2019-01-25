#{expression-on-left, loop-on-right}
#{expression for variable-name in some-collectionType}
setNum = {x for x in [1, 2, 3, 4]}
print(setNum)                                                                   #{1, 2, 3, 4}

setSquares = {x**2 for x in (1, 2, 3, 4)}
print(setSquares)                                                               #{16, 1, 4, 9}

setAlpha = {x for x in 'maps'}
print(setAlpha)                                                                 #{'m', 's', 'a', 'p'}

setAlpha = {x*4 for x in 'maps'}
print(setAlpha)                                                                 #{'mmmm', 'pppp', 'ssss', 'aaaa'}

#sets can be used to filter duplicates out of other collection, but order may differ becus of unordered nature of sets
list1, list2 = [1, 3, 5, 6, 4], [3, 4, 6, 1, 5]
#False, becus lists are ordered
print(list1==list2)                                                             #False
print(set(list1)==set(list2))                                                   #True
print('spam'=='maps')                                                           #False
print(set('spam')==set('maps'))                                                 #True

num = {num for num in [11, 23, 44, 56, 79, 80, 87, 42] if num%2==0}
print(num)                                                                      #{56, 42, 80, 44}
print(type(num))                                                                #<class 'set'>
