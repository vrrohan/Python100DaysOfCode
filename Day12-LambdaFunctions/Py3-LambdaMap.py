#map() is same like filter() takes 2 arguments, 1st is a function that maps each element of list according to given statement in lambda function, while 2nd argument is name of list
#unlike filter() -  map can take any number of lists
#map() modifies items according to lambda function
num = [1, 2, 3, 4, 5]
sqNum = map(lambda x : x*x, num)
print(sqNum)                                                #<map object at 0x00000226C3B73C50>
print(type(sqNum))                                          #<class 'map'>

#By default map() also returns an iterator or map object - to get result in list form cast it using list()
#Hence, you cannot access elements of map object using index[] or can use len()
sqNum = list(map( lambda x : x*x, num))
print(sqNum)                                                #[1, 4, 9, 16, 25]

#add sum of two lists according to index number & create new list
list1 = [12, 4, 17]
list2 = [3, 8, 13]
sumList = list(map( lambda x, y: x+y, list1, list2))
print(sumList)                                              #[15, 12, 30]

#Iterate over list of dictionary having key as names
lis = [{'name':'rohan', 'age':22}, {'name':'elon', 'age':47}, {'name':'guido', 'age':17}]
nameList = list(map( lambda x:x['name'], lis))
print(nameList)                                             #['rohan', 'elon', 'guido']
