#Unlike string objects, lists are mutable i.e. You can change list elements at any index
#String is immutable, So to change string content, you need to assign new string object to new variable
list_of_names = ['rooney', 'ronaldo', 'scholes', 'zidane', 'messi', 'neymar']
print(list_of_names[3])                     #zidane
list_of_names[3] = 'beckham'
print(list_of_names[3])                     #beckham

#Elements can be added to the List by using built-in append() function. Only one element at a time can be added to the list by using append() method
list_of_cars = ['audi', 'bugatti', 'porsche']
print('list of cars before append : ', list_of_cars)                    #list of cars before append :  ['audi', 'bugatti', 'porsche']
#'ferrari' will be added to end of list
list_of_cars.append('ferrari')
list_of_cars.append('porsche')
print('list of cars after append : ', list_of_cars)                     #list of cars after append :  ['audi', 'bugatti', 'porsche', 'ferrari', 'porsche']

#Lists can also be added to the existing list with the use of append() method.
list_of_cars2 = ['dodge viper', 'Agera']
#This will be added as list in list_of_cars
list_of_cars.append(list_of_cars2)
print('after appending list1 to list2 : ', list_of_cars)                #after appending list1 to list2 :  ['audi', 'bugatti', 'porsche', 'ferrari', 'porsche', ['dodge viper', 'Agera']]

#append() method only works for addition of elements at the end of the List, for addition of element at the desired position, insert() method is used.
#Unlike append() which takes only one argument, insert() method requires two arguments(position, value).
print('car at index 4 is : ' + list_of_cars[4])                         #element at index 4 is : porsche
list_of_cars.insert(4, 'nissan')
"""
Output:- after inserting new car nissan at index 4 :  ['audi', 'bugatti', 'porsche', 'ferrari', 'nissan', 'porsche', ['dodge viper', 'Agera']]
"""
print('after inserting new car nissan at index 4 : ', list_of_cars)
list_of_cars.insert(0, 'Bmw')
"""
Output:- after inserting new car bmw at index 0 :  ['Bmw', 'audi', 'bugatti', 'porsche', 'ferrari', 'nissan', 'porsche', ['dodge viper', 'Agera']]
"""
print('after inserting new car bmw at index 0 : ', list_of_cars)

#There’s one more method for Addition of elements, extend(takes list), this method is used to add multiple elements at the same time at the end of the list.
list_of_cars2.extend(['NewCar1', 'NewCar2', 'Newcar3'])
print(list_of_cars2)                        #['dodge viper', 'Agera', 'NewCar1', 'NewCar2', 'Newcar3']

#To add more than 1 items to end of list in form of list use append()
#To add more that 1 items to end of list in from of single item, use extend()

#The del statement will delete values at an index in a list. All of the values in the list after the deleted value will be moved up one index.
print('list2 : ', list_of_cars2)                            #list2 :  ['dodge viper', 'Agera', 'NewCar1', 'NewCar2', 'Newcar3']
del list_of_cars2[3]
print('after deleting 4th element from list2 : ', list_of_cars2)                    #after deleting 4th element from list2 :  ['dodge viper', 'Agera', 'NewCar1', 'Newcar3']

#Elements can be removed from the List by using built-in remove() function but an Error arises if element doesn’t exist in the set.
#Remove() method only removes one element at a time & 1st occurence of element is removed from the list
list_of_city = ['Noida', 'Delhi', 'Bangalore', 'Lucknow', 'Mumbai', 'Gurgaon', 'Noida', 'Lucknow']
print('cities : ', list_of_city)                    #cities :  ['Noida', 'Delhi', 'Bangalore', 'Lucknow', 'Mumbai', 'Gurgaon', 'Noida', 'Lucknow']
list_of_city.remove('Lucknow')
print('cities after removing lucknow : ', list_of_city)                 #cities after removing lucknow :  ['Noida', 'Delhi', 'Bangalore', 'Mumbai', 'Gurgaon', 'Noida', 'Lucknow']
#ValueError arises if item is not present in the list
"""
list_of_city.remove('Pune')
ValueError: list.remove(x): x not in list
"""
#pop() removes the last element from the list
print('cities before pop : ', list_of_city)                             #cities before pop :  ['Noida', 'Delhi', 'Bangalore', 'Mumbai', 'Gurgaon', 'Noida', 'Lucknow']
list_of_city.pop()
print('cities after pop : ', list_of_city)                              #cities after pop :  ['Noida', 'Delhi', 'Bangalore', 'Mumbai', 'Gurgaon', 'Noida']
#Remove element at specific index, use pop(index)
list_of_city.pop(3)
print('cities after popping 4th city : ', list_of_city)                 #cities after popping 4th city :  ['Noida', 'Delhi', 'Bangalore', 'Gurgaon', 'Noida']

#clear() : To remove all elements from a list
print('cities before erase(): ', list_of_city)                          #cities before erase():  ['Noida', 'Delhi', 'Bangalore', 'Gurgaon', 'Noida']
list_of_city.clear()
print('cities after erase(): ', list_of_city)                           #cities after erase():  []
