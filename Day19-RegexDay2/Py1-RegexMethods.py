import re
#Greedy and Nongreedy Matching
#Since (Ha){3,5} can match three, four, or five instances of Ha in the string 'HaHaHaHaHa', you may wonder why the Match object’s call to group() in the previous curly bracket example returns 'HaHaHaHaHa' instead of the shorter possibilities.
#After all, 'HaHaHa' and 'HaHaHaHa' are also valid matches of the regular expression (Ha){3,5}.

#Python’s regular expressions are greedy by default, which means that in ambiguous situations they will match the longest string possible.
#The nongreedy version of the curly brackets, which matches the shortest string possible, has the closing curly bracket followed by a question mark.
greedyPieRegex = re.compile(r'(Pie){3,5}')
getGreedyPie = greedyPieRegex.search('PiePiePiePie')
print(getGreedyPie.group())                                                     #PiePiePiePie

nongreedyPieRegex = re.compile(r'(Pie){3,5}?')
getNonGreedyPie = nongreedyPieRegex.search('PiePiePiePiePie')
print(getNonGreedyPie.group())                                                  #PiePiePie
#Note that the question mark can have two meanings in regular expressions: declaring a nongreedy match or flagging an optional group. These meanings are entirely unrelated.

#match() - search for RE only at the beginning of string
#The match() function only checks if the RE matches at the beginning of the string while search() will scan forward through the string for a match.
#It’s important to keep this distinction in mind. Remember, match() will only report a successful match which will start at 0; if the match wouldn’t start at zero, match() will not report it.
batRegex = re.compile(r'Bat')
isBatRegexFound = batRegex.match('Batman is superhero')
print(isBatRegexFound.group()) if isBatRegexFound else print('Nothing Found')                   #Bat
isBatRegexFound = batRegex.match('Superher is Batman')
print(isBatRegexFound.group()) if isBatRegexFound else print('Nothing Found')                   #Nothing Found
isBatRegexFound = batRegex.search('superhero is Batman')
print(isBatRegexFound.group(), 'at location', isBatRegexFound.span()) if isBatRegexFound else print('Nothing Found')
"""
Bat at location (13, 16)
"""

isBatRegexFound = batRegex.search('Batman is superhero')
print(isBatRegexFound.group(), 'at location', isBatRegexFound.span()) if isBatRegexFound else print('Nothing Found')
"""
Bat at location (0, 3)
"""

#To make a case-insensitive search, use re.IGNORECASE
#It looks for BAT all uppercase
batRegex = re.compile(r'BAT')
isBatRegexFound = batRegex.search('Superhero is BAtman')
print(isBatRegexFound.group()) if isBatRegexFound else print('Nothing Found')                   #Nothing Found

#To search for case-insensitive bat, use I or IGNORECASE
batRegex = re.compile(r'BAT', re.IGNORECASE)
isBatRegexFound = batRegex.search('Superhero is batman')
print(isBatRegexFound.group(), 'at location', isBatRegexFound.span()) if isBatRegexFound else print('Nothing Found')
"""
bat at location (13, 16)
"""

#findall() - will not return match object, it will return list of all strings that were matched
superHerosRegex = re.compile(r'Batman|Superman|Hulk|Spiderman|Ironman', re.IGNORECASE)
#search() will return a Match object of the first matched text in the searched string
isSuperHeroFound = superHerosRegex.search('LA has Ironman, Paris has Batman')
print(isSuperHeroFound.group(), 'at location', isSuperHeroFound.span()) if isSuperHeroFound else print('Nothing Found')
"""
Ironman at location (7, 14)
"""

isSuperHeroFound = superHerosRegex.findall('LA has Ironman, Paris has batman but spain has spiderman')
print(isSuperHeroFound) if isSuperHeroFound else print('Nothing Found')
"""
['Ironman', 'batman', 'spiderman']
"""

#findall() will not return a Match object but a list of strings—as long as there are no groups in the regular expression.
#If there are groups in the regular expression, then findall() will return a list of tuples. Each tuple represents a found match, and its items are the matched strings for each group in the regex.
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
isPhoneNumberFound = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(isPhoneNumberFound) if isPhoneNumberFound else print('Nothing Found')                             #[('415', '555', '9999'), ('212', '555', '0000')]

superHerosRegex = re.compile(r'(Batman)|(Ironman)', re.IGNORECASE)
isSuperHeroFound = superHerosRegex.findall('LA has Ironman, Paris has batman but spain has spiderman')
print(isSuperHeroFound) if isSuperHeroFound else print('Nothing Found')                                 #[('', 'Ironman'), ('batman', '')]

#finditer() method returns a sequence of match object instances as an iterator
superHerosRegex = re.compile(r'Batman|Ironman', re.I)
isSuperHeroFound = superHerosRegex.finditer('LA has Ironman, Paris has batman but spain has spiderman, but Uk also has ironman')
for heros in isSuperHeroFound :
    print('Found', heros.group(), 'at location', heros.span())
"""
Found Ironman at location (7, 14)
Found batman at location (26, 32)
Found ironman at location (74, 81)
"""
