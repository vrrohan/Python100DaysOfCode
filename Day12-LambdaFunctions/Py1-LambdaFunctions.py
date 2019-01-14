#Lambda is a keyword in python that provides a shortcut for declaring small anonymous functions
#They behave just like a regular function with def keyword
#Syntax- lambda arguments : expression
lambda x,y : x+y

#This lambda function has no name, takes two arguments x & y & returns sum of x & y
#Similar equivalent function using def keyword
def sum(x, y) :
    return x+y

#Now this lambda function is associated with a name sum, you can pass 2 arguments with sum(x,y)
sum = lambda x,y : x+y
print(sum(5,9))                                 #14

#Lambda function that takes 2 arguments x & y, returns their sum & then immidiately call it will arguments 5, 9
print((lambda x,y : x+y)(5,9))                  #14

#lambda functions are just like inline function
#Above lambda function isn't bind to any name

#Another difference between lambda & regular function is that lambda function restricted to a single expression
#We cannot use mutiple statements or Annotations inside lambda function, not even a return statement
#Passing incorrect number of arguments while calling lambda function result in TypeError
"""
print((lambda x : x*x) (5, 8))
TypeError: <lambda>() takes 1 positional argument but 2 were given
"""

#Lambda function includes an implicit return statement
#lambda function used as a single expression function
#lambda function that returns percentage scored, input is marks obtained vs total marks
print((lambda x,y : x/y * 100) (441,500))                           #88.2
