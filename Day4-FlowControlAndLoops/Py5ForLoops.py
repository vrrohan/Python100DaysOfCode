#while keeps looping while its condition is True but for-loop execute a block of code only a certain number of times
#using for loops with range()
#Syntax :
"""
for {variable-name} in range(startValue,stopValue,stepArgument) :
    //indentated block of code
"""

#loop to print 'hello' 5 times on same line
#variable i sets to 0, incremented by +1 each time & will go till (5-1) 4
for i in range(5) :
    print('hello', end=' ')                     #hello hello hello hello hello

for i in range(5) :
    print('hello' + str(i), end=' ')            #hello0 hello1 hello2 hello3 hello4

#range(a,b) : loop will start with a(not with 0) & goes till (b-1)
#range(4,9) : will go from 4, 5, 6, 7, 8
for i in range(12,18) :
    print(i)                                    #12 13 14 15 16 17

#range(a,b,stepArgument) : by default value increases by +1, stepArgument is how many times you want to increment i
for i in range(0,11,2) :
    print(i, end=' ')                           #0 2 4 6 8 10

#you can use negative number also for step argument to move back
for i in range(10,0,-1):
    print(i, end=' ')                           #10 9 8 7 6 5 4 3 2 1

#print character by character from a string using for loop
name = 'rohan'
for c in name :
    print(c, end=', ')                          #r, o, h, a, n,

#print vowels characters only from a string else print -1 for consonants
name = 'rohan'
for c in name :
    if c=='a' or c=='e' or c=='i' or c=='o' or c=='u' :
        print(c, end=' ')
    else :
        print('-1', end=' ')                    #-1 o -1 a -1
