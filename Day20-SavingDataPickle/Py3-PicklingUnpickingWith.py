import pickle
#Automatically close pickle file using with
#Trying to pickle game data , to pickle multiple data objects we need to pack them into a single collection of either list or dictionary
#Here two lists are there, one list is list of players which is mapped with another list of dictionary, which contains player scores after one game
#players[0] i.e. 'ron' is associated with characters[0] which is a dictionary, so ron has score of 600, his superhero is 'ironman' & has power 'powerleft' as 47
players = ['ron', 'wayne', 'paul']
characters = [{'hero':'ironman', 'powerleft':47, 'score':600}, {'hero':'batman', 'powerleft':78, 'score':1300}, {'hero':'hulk', 'powerleft':65, 'score':1000}]
with open('gamedump', 'wb') as pkObj :
    #Now since, we cannot dump multiple objects at same time in pickle, we need to bind all those objects into a single collection of either list or dictionary
    #Here i am creating a dictionary to store key-value pair
    gameInfo = {}
    gameInfo['playerNames'] = players
    gameInfo['scoreInfo'] = characters
    pickle.dump(gameInfo, pkObj)
    print('All Data dumped...')

#Now, unpickling same old configuration from pickled file
with open('gamedump', 'rb') as pkObj :
    playerNames = pickle.load(pkObj)
    #Why playerNames['scoreInfo'][i]['score'] ?
    #Becus, when we get our first player , we need to extract characters info using key - playerNames['scoreInfo'], which contains a list of all dictionary scores hence, to access a list we use []
    #playerNames['scoreInfo'][i] which contains dictionary, so to access 'score' key we need to use - playerNames['scoreInfo'][i]['score']
    for i in range(len(playerNames['playerNames'])) :
        print('Player', i+1, 'is', playerNames['playerNames'][i].upper(), 'score :', playerNames['scoreInfo'][i]['score'], end=', ')
        print('superhero :', playerNames['scoreInfo'][i]['hero'], end=', ')
        print('powerleft :', playerNames['scoreInfo'][i]['powerleft'])

#One drawback of the pickle module is that it is only capable of pickling one object at the time, which has to be unpickled in one go.
#Let's imagine this data object is a dictionary. It may be desirable that we don't have to save and load every time the whole dictionary, but save and load just a single value corresponding to just one key.
#The shelve module is the solution to this request. A "shelf" - as used in the shelve module - is a persistent, dictionary-like object.
#The difference with dbm databases is that the values (not the keys!) in a shelf can be essentially arbitrary Python objects -- anything that the "pickle" module can handle.
#This includes most class instances, recursive data types, and objects containing lots of shared sub-objects. The keys have to be strings.
