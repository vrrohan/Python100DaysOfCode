#using python's standard library - random, that gives access to random numbers
#you need to import this module using : import random
#To access any function inside module, use : moduleName.functionName()
import random

#randint(a,b) : returns a random integer between range a to b including both a and b
##randint(a,b) : both must be integer type values
#following randint(1,10) will generate 10 random numbers between 1 to 10, including both 1 & 10
for i in range(10) :
    print(random.randint(1, 10), end=' ')               #5 2 2 3 5 6 10 7 3 1
print()

#you can pass negative integer value also. This will generate 5 random numbers between -5 & +5
for i in range(5) :
    print(random.randint(-5, 5), end=' ')               #-5 -5 4 2 -2

#This method gives ValueError, when float values are passed
#print(random.randint(1.23, 4.5)) :- ValueError: non-integer arg 1 for randrange()

#This method gives TypeError, when any other numeric values are passed like string
#print(random.randint('a', 'z'), end=' ') :- TypeError: can only concatenate str (not "int") to str

#To select a random number from any list [item1, item2, item3, item4, item5]
#choice() :- This function is used to generate 1 random number from a container.
"""
Output:-
randomly choosen number from list is : 1
randomly choosen number from list is : 7
randomly choosen number from list is : 12
"""
for i in range(3) :
    print('randomly choosen number from list is : ' + str(random.choice([1, 3, 12, 10, 7, 5])))

#You can also pass strings inside list & randomly choose it
print(random.choice(['orange', 'apple', 'mango', 'guava']))             #apple
print(random.choice(['orange', 'apple', 'mango', 'guava']))             #mango

#random() : Method used to generate float random numbers between 0.0 & 1.0 [0.0, 1.0) i.e. 0.0 is included & 1.0 is excluded
#This will generate 5 float random numbers between 0.0(included) and 1.0(excluded)
"""
Output:-
random number 0 : 0.2215040927244697
random number 1 : 0.8176362285643867
random number 2 : 0.9046961570086512
random number 3 : 0.8842596242884939
random number 4 : 0.2024283415947915
"""
for i in range(5) :
    print('random number ' + str(i) + ' : ' + str(random.random()))

#To generate float random numbers upto 2 places after decimal , we can use format()
"""
Output:-
random number 0 : 0.41
random number 1 : 0.20
random number 2 : 0.64
random number 3 : 0.69
random number 4 : 0.88
"""
for i in range(5) :
    print('random number ' + str(i) + ' : {:.2f}'.format(random.random()))

#uniform(a, b) :- Used to generate a floating point random number between a(included) and b(excluded).
#This will generate 3 random float numbers between 3.0 & 8.0 [upto 3 places after decimal using format()]
"""
Output:-
random number 0 : 3.940
random number 1 : 7.778
random number 2 : 6.677
"""
for i in range(3) :
    print('random number ' + str(i) + ' : {:.3f}'.format(random.uniform(3,8)))

#randrange(a, b, c) : Generate random integer number within given range a(included) and b(included), c part is optional, a is also optional - by default it starts with 0
#c has default step value of 1, i.e. it skips each element by 1
#To skips elements by k between two numbers call rangerange(a, b, k)
print('random number between 3 & 30 is : ' + str(random.randrange(3, 30)))              #random number between 3 & 30 is : 11
print('random number between 3 & 30 is : ' + str(random.randrange(3, 30)))              #random number between 3 & 30 is : 6

#To print 5 random numbers that is multiple of 3 only, we take step argument as 3
"""
Output:-
random number between (3,30) is : 24
random number between (3,30) is : 18
random number between (3,30) is : 27
random number between (3,30) is : 18
random number between (3,30) is : 24
"""
for i in range(5) :
    print('random number between (3,30) is : ' + str(random.randrange(3, 30, 3)))

#This will print random numbers between 5 & 15, stepping every 3rd number
#start with 5, (+3)8, (+3)11, (+3)14 Hence, it will generate random number between - (5, 8, 11, 14) only
for i in range(5) :
    print(random.randrange(5, 15, 3), end=' ')                      #5 14 8 5 14
print()

#Similarly to print random multiples of 5 between 5 & 50, take step argument as 5
"""
Output1:- 30 10 20 35 10
Output2:- 5 40 20 30 10
Output3:- 25 15 5 15 5
"""
for i in range(5) :
    print(random.randrange(5, 50, 5), end= ' ')
print()

#randrange() raises ValueError if b<=a & number is non-integral
#print(random.randrange(3.5, 9)) :- ValueError: non-integer arg 1 for randrange()
#print(random.randrange(5, 2)) :- ValueError: empty range for randrange() (5,2, -3)

#Random numbers and seed()
#Pseudo-random number generators work by performing some operation on a value.
#Generally this value is the previous number generated by the generator. However, the first time you use the generator, there is no previous value.
#Seeding a pseudo-random number generator gives it its first "previous" value.
#Each seed value will correspond to a sequence of generated values for a given random number generator.
#That is, if you provide the same seed twice, you get the same sequence of numbers twice.
#the random module uses the seed value as a base to generate a random number. if seed value is not present it takes system current time.
print('Random number1 : {:.3f}'.format(random.random()))                                #Random number1 : 0.435
print('Random number2 : {:.3f}'.format(random.random()))                                #Random number2 : 0.467
random.seed(5)
#Now 0.623 is associated with seed(5), whenever you call random.seed(5), it will return 0.623
print('Random number with seed(5) : {:.3f}'.format(random.random()))                    #Random number with seed(5) : 0.623
print('Random number3 : {:.3f}'.format(random.random()))                                #Random number3 : 0.742
random.seed(8)
#Now 0.227 is associated with seed(8), whenever you call random.seed(8), it will return 0.227
print('Random number with seed(8) : {:.3f}'.format(random.random()))                    #Random number with seed(8) : 0.227
print('Random number4 : {:.3f}'.format(random.random()))                                #Random number4 : 0.962
random.seed(5)
print('Random number with seed(5) : {:.3f}'.format(random.random()))                    #Random number with seed(5) : 0.623
random.seed(8)
print('Random number with seed(8) : {:.3f}'.format(random.random()))                    #Random number with seed(8) : 0.227
print('Random number5 : {:.3f}'.format(random.random()))                                #Random number5 : 0.962
print('Random number6 : {:.3f}'.format(random.random()))                                #Random number6 : 0.126
print('Random number7 : {:.3f}'.format(random.random()))                                #Random number7 : 0.705
random.seed(8)
print('Random number with seed(8) : {:.3f}'.format(random.random()))                    #Random number with seed(8) : 0.227
