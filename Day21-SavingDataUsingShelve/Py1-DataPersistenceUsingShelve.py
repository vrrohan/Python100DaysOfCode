#Save your variables to binary shelf files using shelve module
#Remember pickle module has one disadvantage - it is only capable of pickling one object at the time, which has to be unpickled in one go.
#Let's imagine this data object is a dictionary. It may be desirable that we don't have to save and load every time the whole dictionary, but save and load just a single value corresponding to just one key.
#The shelve module is the solution to this request. A "shelf" - as used in the shelve module - is a persistent, dictionary-like object.
#You can save or presist any many objects you want to, unlike in pickle where you save only one collection at a time
import shelve
nameList = ['jon', 'tony', 'daniel', 'robert', 'conor']
cityList = [{'country':'spain', 'state':'barcelona'}, {'country':'france', 'state':'paris'}, {'country':'usa', 'state':'LA'}]
shelfFile = shelve.open('myData')
shelfFile['playerNames'] = [x for x in nameList if 'on' in x]
shelfFile.close()

#pass filename to open(filename) - which returns a shelf value which you can store in a variable
#Here i store list of player names as value(shelf value) which is associated with key 'playerNames'
#After this code runs, 3 files gets created - myData.bak, myData.dat, myData.dir , these binary files contain the data you stored in your shelf
#Shelf values donot have to be opened in read or write mode, they can do both once opened.
sFile = shelve.open('myData')
print(type(sFile))                                                              #<class 'shelve.DbfilenameShelf'>
print(sFile['playerNames'])                                                     #['jon', 'tony', 'conor']
sFile.close()
