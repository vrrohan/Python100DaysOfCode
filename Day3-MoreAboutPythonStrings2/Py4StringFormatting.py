#string formatting allows us to perform multiple type-specific substitutions on a string in a single step.
#string formatting also returns a new string object each time
#You can format a string by passing specific arguments values by position, by keyword or by relative position using format()
#'my' goes to position 0, 'red' goes to position 1
print("this is {0} {1} car".format('my', 'red'))            #this is my red car

stmt = "this is {} {} car".format('my', 'red')
print(stmt)                 #this is my red car

#formatting by position. mention position inside {} & format it by passing values at that position
stmt = "This is {0} big {1} {2}"
print(stmt.format(1, 'red', 'car'))             #This is 1 big red car

#formatting by keyword, mention keyword inside {} & pass values inside format()
stmt = "There are {number} big {color} {animal}"
print(stmt.format(number=3, color='blue', animal='whales'))             #There are 3 big blue whales

#formatting both by position & keyword
stmt = "There are {0} big {color} {1}"
print(stmt.format(2, 'horses', color='black'))                          #There are 2 big black horses

#you cannot use positional parameters after keyword argument, below both statement will cause SyntaxError: positional argument follows keyword argument
#print(stmt.format(2, color='black', 'horses'))
#print(stmt.format(color='black', 2, 'horses'))
#always use all positional arguments first, then use keyword argument

#using list in string formatting
stmt = "{0} team has total {1} members : {namesList}"
#Manchester United team has total 5 members : ['rooney', 'ronaldo', 'pogba', 'evra', 'rio']
print(stmt.format('Manchester United', 5, namesList=['rooney', 'ronaldo', 'pogba', 'evra', 'rio']))

#formatting by relative position
stmt = "there are {} big {} {}"
print(stmt.format(5, 'red', 'trucks'))                  #there are 5 big red trucks
