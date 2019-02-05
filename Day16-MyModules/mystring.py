import operator
import itertools
import re

#Dictionary that maintains the codepoint values of each lowercase a-z
codePointsLower = {chr(alpha):alpha for alpha in range(97, 123)}
#Dictionary that maintains the codepoint values of each uppercase A-Z
codePointsUpper = {chr(alpha):alpha for alpha in range(65, 91)}
codePointsDigits = {chr(dig):dig for dig in range(0,10)}

"""This method returns list of all dictinct characters in a string"""
def getDistinctChars(string) :
    return list(set(string))

"""This method returns list of all vowels present in a string"""
def getVowels(string) :
    return [v for v in string if v in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']]

"""This method returns list of all consonants present in a string"""
def getConsonants(string) :
    return [c for c in string if c not in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']]

"""This method returns list of All special characters present in a string, except \\"""
def getSpecialChars(string) :
    return [spec for spec in string if spec in ['!', ' ', '@', '#', '$', '%', '^', '&', '*', '(', ')', '.', '?', ';', ':', '<', '>', ',', '{', '}', '[', ']', '|', '/']]

"""This method returns all digits present in string in form of list"""
def getAllDigits(string) :
    return [dig for dig in string if dig in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']]

"""This method process html tag & returns it name"""
def getTagName(string) :
    return str(string[1:len(string)-1])

"""This method returns a reversed string"""
def getReverse(string) :
    return str(string[::-1])

"""This method returns codepoint or(ascii value) of passed character"""
def getCodePoint(chrPoint) :
    return codePointsLower[chrPoint] if (chrPoint in codePointsLower) else codePointsUpper[chrPoint]

"""This method returns character present at specified index in a string"""
def getCharAt(index, string) :
    return string[index] if (index<len(string)) else None

"""This method returns frequency of each character in a string in form of dictionary"""
def getAllCharFrequency(string) :
    dictChars = {}
    for i in string :
        if i in dictChars :
            dictChars[i] = dictChars[i] + 1
        elif i not in dictChars :
            dictChars[i] = 1
    return dictChars

"""This method returns list of all duplicate characters present in a string"""
def getAllDuplicates(string) :
    return list({x for x in string if string.count(x) > 1})

"""This method removes all duplicate characters from a string & return new string with all dictinct characters"""
def removeAllDuplicates(string) :
    emptyString = ''
    for s in string :
        if string.count(s)==1 :
            emptyString = emptyString + str(s)
    return emptyString

"""This method returns character which occurs maximum time in a string"""
def getMaximumOccuringCharacter(string) :
    dictAllCharacters = getAllCharFrequency(string)
    return sorted(dictAllCharacters.items(), key=operator.itemgetter(1), reverse=True)[0][0]

"""This method reverses each word one by one & returns list of those reversed words"""
def reverseByWords(string) :
    lis = string.split(' ')
    stringRev = ''
    for s in [x[::-1] for x in lis] :
        stringRev = stringRev + s + ' '
    return stringRev[:len(stringRev)-1]

"""This method returns frequency of each word in form of dictionary"""
def countAllWordsFrequency(string) :
    listOfWords = string.split(' ')
    dictOfWords = {}
    for w in listOfWords :
        if w in dictOfWords :
            dictOfWords[w] = dictOfWords[w] + 1
        elif w not in dictOfWords :
            dictOfWords[w] = 1
    return dictOfWords

"""This method returns word which appears maximum time in a string. If more than one word have same maximum occurence, it will return word which is smaller"""
def getWordWithMaximumFrequency(string) :
    dictOfWordsWithMaxFrequency = countWordFrequency(string)
    return sorted(dictOfWordsWithMaxFrequency.items(), key=operator.itemgetter(1), reverse=True)[0][0]

"""This method uses itertools module in-built permutations method to return list of all permutations of a passed string"""
def getAllPermutations(string) :
    listOfAllPermutations = []
    for perm in itertools.permutations(string) :
        joinedPerm = ''
        for p in perm :
            joinedPerm = joinedPerm + str(p)
        listOfAllPermutations.append(joinedPerm)
    return listOfAllPermutations;

"""This method returns combinations of word pass as an argument, combOf is integer which determines the length of that combination, if length > length of string, empty string will be returned"""
def getAllCombinations(string, combOf) :
    listOfAllCombinations = []
    for comb in itertools.combinations(string, combOf) :
        joinedComb = ''
        for c in comb :
            joinedComb = joinedComb + str(c)
        listOfAllCombinations.append(joinedComb)
    return listOfAllCombinations

"""This method trims all leading whitespaces, trailing whitespaces & if more than one whitespaces is present between two words"""
def trimWhitespaces(string) :
    listOfWords = re.split("\s+", string)
    str = ''
    for elem in listOfWords :
        if(elem!='') :
            str = str + elem + ' '
    string = str
    return string[:len(string)-1]

"""This method returns list of substrings of given length by sliding window of length from start"""
def getSlidingWindowStrings(string, length) :
    listOfSlidingStrings = []
    for i in range(0, len(string)-length+1) :
        listOfSlidingStrings.append(string[i:length+i])
    return listOfSlidingStrings

"""This method returns boolean value whether string is palindrome or not"""
def isStringPalindrome(string) :
    return True if string==string[::-1] else False

"""This method returns maximum element in a string"""
def getMaxCharacter(string) :
     return sorted([chars for chars in string], reverse=True)[0]

"""This method returns minimum element in a string"""
def getMinCharacter(string) :
    return sorted([chars for chars in string])[0]

def getStringWithDifferentCharacters(stringOne, stringTwo) :
    setOne = set(stringOne)
    setTwo = set(stringTwo)
    concatStringSet = set()
    for s1 in setOne :
        concatStringSet.add(s1)
    for s2 in setTwo :
        concatStringSet.add(s2)
    print(concatStringSet)


print(getStringWithDifferentCharacters('hello', 'jekko'))
