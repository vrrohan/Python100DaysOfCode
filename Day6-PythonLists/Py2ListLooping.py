#You can iterate or traverse a list using many ways
list_of_cars = ['audi', 'porsche', 'lamborgini', 'nissan', 'ferrari', 'bugatti']

#Method 1 - using for loop with list name
#step by step, cars from index 0 will be placed in variable x & it keeps on printing
for x in list_of_cars :
    print(x, end=', ')                     #audi, porsche, lamborgini, nissan, ferrari, bugatti,

#Method 2 - using for loop with range()
"""
car at index 1 is : porsche
car at index 2 is : lamborgini
car at index 3 is : nissan
car at index 4 is : ferrari
car at index 5 is : bugatti
"""
for x in range(len(list_of_cars)) :
    print('car at index ' + str(x) + ' is : ' + list_of_cars[x])

#Method 3 - Using while loop
#There is no ++ or -- operators in python, you have to use index += 1 i.e. index = index + 1
index = 0
while index < len(list_of_cars) :
    print(list_of_cars[index], end=', ')                                        #audi, porsche, lamborgini, nissan, ferrari, bugatti,
    index += 1
print()

#Iterate over only odd position of list
for x in range(len(list_of_cars)) :
    if x%2==0 :
        print(list_of_cars[x], end= ' ')                                        #audi lamborgini ferrari
print()

#Iterate over list using list comprehension, use print() inside []
[print(x, end= ', ') for x in list_of_cars]                                     #audi, porsche, lamborgini, nissan, ferrari, bugatti,
print()

#Print car name ending with 'i' using list comprehension
[print(x, end=' ') for x in list_of_cars if x.endswith('i')]                    #audi lamborgini ferrari bugatti
print()

#print list elements using *(list-name) using print
print('printing list using * : ', *(list_of_cars))                              #printing list using * :  audi porsche lamborgini nissan ferrari bugatti


#Iterating over mutiple list at once using zip()
#In Python, zip returns a list of tuples. This is fine when lists are not massive.
list1 = [2, 4, 6, 8, 10]
list2 = ['mars', 'earth', 'sun', 'jupiter']
list3 = ['apple', 'pie', 'grapes', 'orange', 'pineapple', 'banana']
#print list elements separated by ,
#By default, if list are of different sizes it will print till smallest list size & then it stops
for (l1,l2,l3) in zip(list1, list2, list3) :
    print(l1, l2, l3, sep=', ')
