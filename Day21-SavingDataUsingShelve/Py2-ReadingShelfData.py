#Since, data stored in shelf is in key-value form, just like dictionary, shelf has keys() & values()- that will return list like values of keys & values
#But not actual list is returned, Hence to get in form of list, use list()
#First Saving multiple objects to shelf file
import shelve
listOfPlayers = ['conor', 'jon', 'robert']
configList = [{'country':'ireland', 'score':1200, 'powerleft':65, 'resolution':'720p'}, {'country':'england', 'score':700, 'powerleft':88, 'resolution':'1080p'}, {'country':'spain', 'score':1500, 'powerleft':40, 'resolution':'1080p'}]
myShelve = shelve.open('gameData')
myShelve['names'] = listOfPlayers[:2]
myShelve['config'] = configList[:2]
myShelve.close()

#Now lets try to read the saved data from gameData file
myShelve = shelve.open('gameData')
print(myShelve['names'])
print(myShelve['config'])
"""
['conor', 'jon']
[{'country': 'ireland', 'score': 1200, 'powerleft': 65, 'resolution': '720p'}, {'country': 'england', 'score': 700, 'powerleft': 88, 'resolution': '1080p'}]
"""
myShelve.close()

myShelve = shelve.open('gameData')
for keys in myShelve.keys() :
    print(keys, end=', ')
print()
for values in myShelve.values() :
    print(values, end=', ')
"""
names, config,
['conor', 'jon'], [{'country': 'ireland', 'score': 1200, 'powerleft': 65, 'resolution': '720p'}, {'country': 'england', 'score': 700, 'powerleft': 88, 'resolution': '1080p'}],
"""
myShelve.close()
