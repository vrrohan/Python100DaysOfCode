#2 main elements of flow control - a) condition b) blocks of code
#Condition - always evlaute down to True or False
#A flow control statement decides what to do based on result of condition, whether that condition is True or False
#Example - if(traffic is heavy) : move slow , else : move fast

#Blocks of code : python statement or code grouped together (having same indentation) is in same block
#In Python you can tell a block of code from Indentation of lines of code

#3 rules for blocks :
#a) Blocks begin when indentation increases
#b) Blocks can contain other Blocks
#c) Blocks end when indentation decreases to 0 or to a containing blocks indentation

if (color is red) :
    #block begins as indentation increases
    print('1')
    print('2')
    print('3')
elif (color is blue) :
    #new block begins
    print('4')
    print('5')
        #new block, also one block contains another block
        print('6')
        print('7')      #this block ends here
    #old block continues...
    print('8')
    print('9')
    print('10')
        #new block starts
        print('11')     #this block ends as indentation decreases to 0
else :
    print('12')
