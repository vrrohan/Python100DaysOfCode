#You can add a key-value pair in existing dictionary using []
#dictionary_name[key] = value
teams = {1:'France', 2:'Germany'}
print(teams)                                        #{1: 'France', 2: 'Germany'}
teams[3] = 'Brazil'
teams[4] = 'Argentina'
print(teams)                                        #{1: 'France', 2: 'Germany', 3: 'Brazil', 4: 'Argentina'}

#Adding key-value pair using setDefault(key, value[optional]) - Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
#Since, 3 is already present in dictionary, it will return its value
print(teams.setdefault(3, 'Spain'))                                             #Brazil
print(teams)                                                                    #{1: 'France', 2: 'Germany', 3: 'Brazil', 4: 'Argentina'}

#Now 6 key is not present in dictionary, it will enter new key 6 and 'England' as its value
print(teams.setdefault(6, 'England'))                                           #England
print(teams)                                                                    #{1: 'France', 2: 'Germany', 3: 'Brazil', 4: 'Argentina', 6: 'England'}

#Removing an existing key from a dictionary using pop()
#pop(keyName, valueToReturn[optional]) returning its associated value
print(teams.pop(4))                                 #Argentina
print(teams)                                        #{1: 'France', 2: 'Germany', 3: 'Brazil', 6: 'England'}

#If a key is not present in the dictionary, it will show KeyError
"""
print(teams.pop(8))
KeyError: 8
"""
#To avoid that error, pass that 2nd argument, that value will be returned
print(teams.pop(10, 'Not in dict'))                 #Not in dict
print(teams)                                        #{1: 'France', 2: 'Germany', 3: 'Brazil', 6: 'England'}

#You can also use del to delete existing key-value pair
#del[key-name]
teams = {1:'France', 2:'Germany', 3:'Brazil', 4:'Argentina', 5:'Spain'}
del teams[4]
print(teams)                                        #{1: 'France', 2: 'Germany', 3: 'Brazil', 5: 'Spain'}

#If key is not present in dictionary, it will show KeyError
"""
del teams[9]
KeyError: 9
"""

#clear() - removes all elements (key-value pair) from dictionary
print(teams)                                        #{1: 'France', 2: 'Germany', 3: 'Brazil', 5: 'Spain'}
teams.clear()
print(teams)                                        #{}

#update() - just like concatenation i.e. It merges key-value pair of one dictionary into Another, overwriting values of same key if there is a clash
teams = {1:'France', 2:'Germany', 3:'Brazil', 4:'Argentina', 5:'Spain'}
teams2 = {11:'India', 12:'Australia', 3:'Africa', 5:'New Zealand'}
#key 3 clashes - so its new updated value is 'Africa', so on with key 5
teams.update(teams2)
print(teams)                                        #{1: 'France', 2: 'Germany', 3: 'Africa', 4: 'Argentina', 5: 'New Zealand', 11: 'India', 12: 'Australia'}

nameDict = {}
nameDict.update({'key1':'value1', 'key2':'value2'})
print(nameDict)                                     #{'key1': 'value1', 'key2': 'value2'}

#popitem() method removes the item that was last inserted into the dictionary.
teams = {1:'France', 2:'Germany', 3:'Brazil', 4:'Argentina', 5:'Spain', 6:'England'}
teams.popitem()
print(teams)                                        #{1: 'France', 2: 'Germany', 3: 'Brazil', 4: 'Argentina', 5: 'Spain'}
teams.popitem()
print(teams)                                        #{1: 'France', 2: 'Germany', 3: 'Brazil', 4: 'Argentina'}
