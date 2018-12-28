#To get maximum value in a tuple - use max(), for minimum value use min()
marks = (23, 45, 67, 89, 40, 66)
print('maximum marks in tuple is : ', max(marks))                       #maximum marks in tuple is :  89
print('minimum marks in tuple is : ', min(marks))                       #minimum marks in tuple is :  23

#You can concatenate a tuple using +
maps = (1, 2, 3,)
newMaps = maps + maps + ('end',)
print(newMaps)                          #(1, 2, 3, 1, 2, 3, 'end')

#You can multiply tuple using *
maps = (1, 2)
maps = maps*4
print(maps)                             #(1, 2, 1, 2, 1, 2, 1, 2)

#To get index of any element in a tuple, use - index(element)
#If no element is found, a ValueError exception is raised indicating the element is not found.
#If element is found, it returns the smallest(lowest) index from start
marks = (4, 6, 7, 2, 4, 1, 2, 9, 9, 4, 2)
print('index of 2 : ', marks.index(2))                      #index of 2 :  3

#by default, index() start searching from index 0
#To start searching from any specific index, use index(element, indexNumber)
print('index of 2 after index 5 : ', marks.index(2, 5))                         #index of 2 after index 5 :  6

#count() returns the number of times an element occurs in a tuple
print('2 is', marks.count(2), 'times in a tuple')                               #2 is 3 times in a tuple

#use sum() to get sum of all values in a tuple
marks = (23, 45, 67, 89, 40, 66)
print('sum is :', sum(marks))                                                   #sum is : 330
