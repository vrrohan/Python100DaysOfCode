#Sorting Python dictionary using built-in sorted()
#sorted() - returns list of values which have been sorted (aescending order by default)
#sorted(dictionary-name) - return a sorted list of keys
teams = {4:'PSG', 2:'Barcelona', 5:'madrid', 3:'Chelsea', 8:'arsenal', 6:'manchester'}
sortByKey =  sorted(teams)
print(sortByKey)                                                                #[2, 3, 4, 5, 6, 8]

#sorted(dictionary-name.items()) - will return a sorted list of tuples containing key-value pair. Will sort in aescending order of keys by Default
sortByItems = sorted(teams.items())
print(sortByItems)                                                              #[(2, 'Barcelona'), (3, 'Chelsea'), (4, 'PSG'), (5, 'madrid'), (6, 'manchester'), (8, 'arsenal')]

#sorted(dictionary-name, reverse=True) - passing 2nd argument reverse=True will return list of sorted list of keys in descending order
sortByKeyDesc = sorted(teams, reverse=True)
print(sortByKeyDesc)                                                            #[8, 6, 5, 4, 3, 2]

#sorted(dictionary-name.items(), reverse=True) - will return a descending sorted list of tuples containing key-value pair
#Again reverse sorting will be according to key
sortByItemsDesc = sorted(teams.items(), reverse=True)
print(sortByItemsDesc)                                                          #[(8, 'arsenal'), (6, 'manchester'), (5, 'madrid'), (4, 'PSG'), (3, 'Chelsea'), (2, 'Barcelona')]

#Sorting dictionary values using sorted()
#Till now we are getting sorted collection of keys only, either sorting or reverse sorting - it takes place according to key only
#To sort according to value - we need to pass values() to sorted()
teams = {4:'PSG', 2:'Barcelona', 5:'madrid', 3:'Chelsea', 8:'arsenal', 6:'manchester'}

#This will return a sorted list of values
sortByValue = sorted(teams.values())
print(sortByValue)                                                              #['Barcelona', 'Chelsea', 'PSG', 'arsenal', 'madrid', 'manchester']

#This will return reverse sorted list of values
sortByValueDesc = sorted(teams.values(), reverse=True)
print(sortByValueDesc)                                                          #['manchester', 'madrid', 'arsenal', 'PSG', 'Chelsea', 'Barcelona']

#Traversing over sorted list of key-value pair, sorting by keys
teams = {4:'France', 2:'Germany', 5:'Spain', 3:'England'}
"""
2 : Germany
3 : England
4 : France
5 : Spain
"""
for k in sorted(teams) :
    print(k, ':', teams[k])

#Traversing over reverse sorted list of key-value pair, sorting by keys
"""
5 : Spain
4 : France
3 : England
2 : Germany
"""
for k in sorted(teams, reverse=True) :
    print(k, ':', teams[k])


#Sorting dictionary by keys using dictionary_name.keys()
teams = {4:'PSG', 2:'Barcelona', 5:'madrid', 3:'Chelsea', 8:'arsenal', 6:'manchester'}
sortTeamsByKey = sorted(teams.keys())
print('teams sorted by key : ' + str(sortTeamsByKey))

#To get reverse sorted keys , pass reverse=True as 2nd argument to sorted()
revSortTeamsByKey = sorted(teams.keys(), reverse=True)                                      #teams sorted by key : [2, 3, 4, 5, 6, 8]
print('teams reverse sorted by key : ' + str(revSortTeamsByKey))                            #teams reverse sorted by key : [8, 6, 5, 4, 3, 2]

#Sorting dictionary by values using operator module
#Use sorted() and operator module's itemgetter()
#sorted() takes another 3rd argument key=operator.itemgetter(0/1)
#Since, sorted() returns list of tuples of key-value pair, key is at index 0 & value at index 1, so to get sorted dictionary by key pass 0
print('sorting dictionary using operator\n------------------------------------')
import operator
teams = {4:'PSG', 2:'Barcelona', 5:'madrid', 3:'Chelsea', 8:'arsenal', 6:'manchester'}

#0 is for key, 1 is for value
print(sorted(teams.items(), key=operator.itemgetter(0)))                        #[(2, 'Barcelona'), (3, 'Chelsea'), (4, 'PSG'), (5, 'madrid'), (6, 'manchester'), (8, 'arsenal')]
#this will return sorted by values
print(sorted(teams.items(), key=operator.itemgetter(1)))                        #[(2, 'Barcelona'), (3, 'Chelsea'), (4, 'PSG'), (8, 'arsenal'), (5, 'madrid'), (6, 'manchester')]
#This will return sorted values in reverse order
print(sorted(teams.items(), key=operator.itemgetter(1), reverse=True))          #[(6, 'manchester'), (5, 'madrid'), (8, 'arsenal'), (4, 'PSG'), (3, 'Chelsea'), (2, 'Barcelona')]
#This will return sorted key in reverse order
print(sorted(teams.items(), key=operator.itemgetter(0), reverse=True))          #[(8, 'arsenal'), (6, 'manchester'), (5, 'madrid'), (4, 'PSG'), (3, 'Chelsea'), (2, 'Barcelona')]

#Passing more than tuple range in itemgetter() will result in IndexError, becus only 2 values in tuples, you can either pass 0 or 1
#If your tuple has 3 values, you can pass 0, 1 or 2
"""
print(sorted(teams.items(), key=operator.itemgetter(3)))
IndexError: tuple index out of range
"""

#List of dictionary
lis = [{'name':'wayne', 'age':29, 'country':'england'}, {'name':'paul', 'age':25, 'country':'France'}, {'name':'lucas', 'age':32, 'country':'germany'}]

#To get list sorted by age , use itemgetter('age')
sortByAge = sorted(lis, key=operator.itemgetter('age'))
print(sortByAge)                        #[{'name': 'paul', 'age': 25, 'country': 'France'}, {'name': 'wayne', 'age': 29, 'country': 'england'}, {'name': 'lucas', 'age': 32, 'country': 'germany'}]

#Reverse sort list by age
revSortByAge = sorted(lis, key=operator.itemgetter('age'), reverse=True)
print(revSortByAge)                     #[{'name': 'lucas', 'age': 32, 'country': 'germany'}, {'name': 'wayne', 'age': 29, 'country': 'england'}, {'name': 'paul', 'age': 25, 'country': 'France'}]
