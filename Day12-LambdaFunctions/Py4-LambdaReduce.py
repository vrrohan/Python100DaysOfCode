#reduce() - reduces whole list or dictionary to a single value
#each element is processed one by one using some lambda function
from functools import reduce
num = [5, 7, 12, 4, 1]
totalSum = reduce(lambda x,y : x+y, num)
print(totalSum)                                     #29

#using reduce to get maximum element from list
num = [5, 7, 12, 4, 1, 99, 68]
maxElement = reduce(lambda x,y : x if x>y else y, num)
print(maxElement)                                   #99

name = ['ferrari', 'bmw', 'lamborgini', 'tesla', 'audi', 'porsche', 'volkswag']
longestName = reduce(lambda x,y : x if len(x)>=len(y) else y, name)
print(longestName)                                  #lamborgini
