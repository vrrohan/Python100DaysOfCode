#sort() can be used to sort the list in both ascending and descending order.
list_of_city = ['Noida', 'Delhi', 'Bangalore', 'Lucknow', 'Mumbai', 'Gurgaon']
list_of_marks = [78, 89, 65, 92, 70, 56, 45, 82, 70]

print('cities before sort() : ', list_of_city)                      #cities before sort() :  ['Noida', 'Delhi', 'Bangalore', 'Lucknow', 'Mumbai', 'Gurgaon']
print('marks before sort() : ', list_of_marks)                      #marks before sort() :  [78, 89, 65, 92, 70, 56, 45, 82, 70]
list_of_city.sort()
list_of_marks.sort()
print('cities after sort() : ', list_of_city)                       #cities after sort() :  ['Bangalore', 'Delhi', 'Gurgaon', 'Lucknow', 'Mumbai', 'Noida']
print('marks after sort() : ', list_of_marks)                       #marks after sort() :  [45, 56, 65, 70, 70, 78, 82, 89, 92]

#To sort list in descending order, use - list_name.sort(reverse=True)
list_of_marks.sort(reverse=True)
print('marks in reverse order : ', list_of_marks)                   #marks in reverse order :  [92, 89, 82, 78, 70, 70, 65, 56, 45]

#To reverse a list use - listName.reverse()
list_of_marks = [78, 89, 65, 92, 70, 56, 45, 82, 70]
print('marks before erase : ', list_of_marks)                       #marks before erase :  [78, 89, 65, 92, 70, 56, 45, 82, 70]
list_of_marks.reverse()
print('marks after reverse : ', list_of_marks)                      #marks after reverse :  [70, 82, 45, 56, 70, 92, 65, 89, 78]

#Get sum of list having integers or floats only
#Python provide an inbuilt function sum() which sums up the numbers in the list.
#sum(listName)
listOfNums = [1, 2, 3, 4, 5]
print('sum of numbers is : ', sum(listOfNums))                           #sum of numbers is :  15
#sum(listName, start) - returns sum of all numbers + start
print('sum of numbers is : ', sum(listOfNums, 20))                       #sum of numbers is :  35

#TypeError : This error is raised in the case when there is anything other then numbers in the list.
"""
listOfNames = ['abc', 'xyz', 'mno']
print('sum of names : ', sum(listOfNames))
TypeError: unsupported operand type(s) for +: 'int' and 'str'
"""

lis = [2.3, 4.5, 6.7]
print(sum(lis))                 #13.5

#Using in & not in with lists
#(itemToSearch in listName) will return True if item is present in list , Otherwise returns False
#not in will return True, if item is not present in the list
list_of_marks = [78, 89, 65, 92, 70, 56, 45, 82, 70]
print(27 in list_of_marks)                          #False
print(70 in list_of_marks)                          #True
print(99 not in list_of_marks)                      #True

#Convert String to list in python using :- list(stringName)
name = "Lamborgini"
listName = list(name)
print(listName)                                     #['L', 'a', 'm', 'b', 'o', 'r', 'g', 'i', 'n', 'i']

#Converting a list back into String using join(listName)
newName = ''.join(listName)
print(newName + " , type is : " + str(type(newName)))                   #Lamborgini , type is : <class 'str'>

#To get max() & min() item in list use - max(listName) or min(listName)
list_of_city = ['Noida', 'Delhi', 'Bangalore', 'Lucknow', 'Mumbai', 'Gurgaon']
list_of_marks = [78, 89, 65, 92, 70, 56, 45, 82, 70]
print("maximum marks : ", max(list_of_marks))                           #maximum marks :  92
print("minimum marks : ", min(list_of_marks))                           #minimum marks :  45
#Becus N has highest ascii value, while B has lowest ascii value
print("max in cities : ", max(list_of_city))                            #max in cities :  Noida
print("min in cities : ", min(list_of_city))                            #min in cities :  Bangalore
