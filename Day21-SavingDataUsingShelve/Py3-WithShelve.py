import shelve
#using with while opening shelf file to read & write data, will Automatically closes the file
with shelve.open('gameData') as shel :
    shel['marks'] = (34, 48, 25, 42)
    #Now trying to read all keys & values
    for k in shel.keys() :
        print('key:', k, end=', ')
        print('has values:', shel[k])
"""
key: names, has values: ['conor', 'jon']
key: config, has values: [{'country': 'ireland', 'score': 1200, 'powerleft': 65, 'resolution': '720p'}, {'country': 'england', 'score': 700, 'powerleft': 88, 'resolution': '1080p'}]
key: marks, has values: (34, 48, 25, 42)
"""
