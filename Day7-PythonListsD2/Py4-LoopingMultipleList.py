#Iterating or looping over more than 2 lists using zip()
#zip() returns the list of tuples & runs till the length of shortest list
fruits = ['Apple', 'Grapes', 'Pineapple']
cars = ['Lamborgini', 'Bugatti', 'Porsche']
city = ['Berlin', 'Moscow', 'Paris']
"""
Apple, Lamborgini, Berlin
Grapes, Bugatti, Moscow
Pineapple, Porsche, Paris
"""
for (f,ca,ci) in zip(fruits,cars,city) :
    print(f + ', ' + ca + ', ' + ci)

print('loop 2')
#Since zip() runs till the length of shortest list, looping over lists having unequal length
#It will loop till 4th element of each list, since shortest list cars is of length 4
fruits = ['Apple', 'Grapes', 'Pineapple', 'Orange', 'Banana']
cars = ['Lamborgini', 'Bugatti', 'Porsche', 'Nissan']
city = ['Berlin', 'Moscow', 'Paris', 'Delhi', 'Tokyo', 'Sydney']
"""
Apple, Lamborgini, Berlin
Grapes, Bugatti, Moscow
Pineapple, Porsche, Paris
Orange, Nissan, Delhi
"""
for (f,ca,ci) in zip(fruits,cars,city) :
    print(f + ', ' + ca + ', ' + ci)

#Looping over mutiple lists using itertools module zip_longest()
#zip_longest() returns iterator instead of a list
#zip_longest() stops when all lists are exhausted. When the shorter iterator(s) are exhausted, zip_longest() yields a tuple with None value.
fruits = ['Apple', 'Grapes', 'Pineapple', 'Orange', 'Banana']
cars = ['Lamborgini', 'Bugatti', 'Porsche', 'Nissan']
city = ['Berlin', 'Moscow', 'Paris', 'Delhi', 'Tokyo', 'Sydney']
import itertools
"""
Apple ,  Lamborgini ,  Berlin
Grapes ,  Bugatti ,  Moscow
Pineapple ,  Porsche ,  Paris
Orange ,  Nissan ,  Delhi
Banana ,  None ,  Tokyo
None ,  None ,  Sydney
"""
for (a,b,c) in itertools.zip_longest(fruits,cars,city) :
    print(a , ', ' , b  , ', '  , c)

#Generating both offsets(Index number) and item from list
#Using enumerate() - It returns a generator object—a kind of object that supports the iteration protocol
#It has a method called by the next() built-in function, which returns an (index, value) tuple each time through the loop.
#The for steps through these tuples automatically, which allows us to unpack their values with tuple assignment
names = ['mark', 'paul', 'daley', 'wayne']
"""
mark at location 0
paul at location 1
daley at location 2
wayne at location 3
"""
for (index,item) in enumerate(names) :
    print(item + ' at location ' + str(index))

#looping over two lists & their indexes using enumerate() & zip()
#enumerate() runs till length of shortest list
cars = ['Lamborgini', 'Bugatti', 'Porsche', 'Nissan']
city = ['Berlin', 'Moscow', 'Paris', 'Delhi', 'Tokyo', 'Sydney']
"""
Index 1: Lamborgini, Berlin
Index 2: Bugatti, Moscow
Index 3: Porsche, Paris
Index 4: Nissan, Delhi
"""
for index, (ca,ci) in enumerate(zip(cars, city)) :
    print('Index ' + str(index+1) + ': ' + str(ca) + ', ' + str(ci))

#Iterating or looping over string character by character & its index
name = "Python"
"""
character P at location 1
character y at location 2
character t at location 3
character h at location 4
character o at location 5
character n at location 6
"""
for (indx,char) in enumerate(name) :
    print('character ' + str(char) + ' at location ' + str(indx+1))
