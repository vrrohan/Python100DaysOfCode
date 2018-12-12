#syntax : if (some condition that evaluates to either True or False) :
                #block of code
#         else :
                #block of code
#if condition in if is True, then run if-statement, else run else block
#else part is optional in if-else statements
name = 'audi'
if name == 'audi' :
    print('this is a car')          #this is a car
else :
    print('not a car')

#you can also use paranthesis around condition for better code readability
if (name=='bmw') :
    print('car is bmw')
else :
    print('car is audi')            #car is audi

#If statement without else clause
#check if name is 'admin', then only grant access
name = 'admin'
if (name == 'admin') :
    print('Access Granted!!!')      #Access Granted

#multiple if-else using elif
#if (some condition) :    //statement
#elif (some condition) :    //statement
#elif (some condition) :    //statement
#else :     //statement
marks = 75
if (marks >= 90) :
    print('student is best')
elif ((marks>=80) and (marks<90)) :
    print('student is better')
elif ((marks>=70) and (marks<80)) :
    print('student is good')                    #student is good
else :
    print('student is average')

#check if number is odd or even using % modulus
num = 17
#here we check if number is divisible by 2, hence has 0 remainder, hence number is even
if (num%2==0) :
    print('number ' + str(num) + ' is even')
else :
    print('number ' + str(num) + ' is odd')
