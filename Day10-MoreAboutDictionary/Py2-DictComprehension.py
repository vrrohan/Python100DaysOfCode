#Like List Comprehension, Python allows dictionary comprehensions. We can create dictionaries using simple expressions.
#A dictionary comprehension takes the form {key: value for (key, value) in iterable}
#Standard way to initialize a dictionary dynamically is to combine its keys and values with zip, and pass the result to the dict call.
#The zip built-in function is the hook that allows us to construct a dictionary from key and value lists t
#This way you can achieve the same effect with a dictionary comprehension expression.

#Dictionary comprehensions are also useful for initializing dictionaries from keys lists, in much the same way as the fromkeys()
#Dictionary comprehension is a method for transforming one dictionary into another dictionary.
#During this transformation, items within the original dictionary can be conditionally included in the new dictionary and each item can be transformed as needed.

#Creating dictionary using two lists, 1st list act as key, 2nd list will act as its value
asciiVal = {key:val for (key,val) in zip(['a', 'b', 'c'], [97, 98, 99])}
print(asciiVal)                                                                 #{'a': 97, 'b': 98, 'c': 99}

#Creating dictionary using single list
squareNumDict = {x:x*x for x in [1,2,3,4,5]}
print(squareNumDict)                                                            #{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#Creating dictionary using string
alphaQuadDict = {x:x*4 for x in 'MAPS'}
print(alphaQuadDict)                                                            #{'M': 'MMMM', 'A': 'AAAA', 'P': 'PPPP', 'S': 'SSSS'}

dictLower = {x.lower():x + '!' for x in ['APPLE', 'ORANGE', 'GRAPES']}
print(dictLower)                                                                #{'apple': 'APPLE!', 'orange': 'ORANGE!', 'grapes': 'GRAPES!'}

#Creating dictionary using list & will same values for all keys
dictWithAllZero = {x:0 for x in ['a', 'e', 'i', 'o', 'u']}
print(dictWithAllZero)                                                          #{'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

#Creating dictionary using string with all values initialized to None
dictWithNone = {x.lower():None for x in 'MAPS'}
print(dictWithNone)                                                             #{'m': None, 'a': None, 'p': None, 's': None}

#creating one dictionary from another dictionary using dictionary_name.items()
dictVowels = {'a':1, 'e':5, 'i':9, 'o':15, 'u':21}
dictSquareVowels = {k:val*val for (k,val) in dictVowels.items()}
print(dictVowels)                                                               #{'a': 1, 'e': 5, 'i': 9, 'o': 15, 'u': 21}
print(dictSquareVowels)                                                         #{'a': 1, 'e': 25, 'i': 81, 'o': 225, 'u': 441}

#Creating dictionary using range()
dicOfEvenNumbers = {x:x*x for x in range(0,20) if x%2==0}
print(dicOfEvenNumbers)                                                         #{0: 0, 2: 4, 4: 16, 6: 36, 8: 64, 10: 100, 12: 144, 14: 196, 16: 256, 18: 324}
