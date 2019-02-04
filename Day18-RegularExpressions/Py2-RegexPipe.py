import re
#Matching Multiple Groups with the Pipe
#The | character is called a pipe. You can use it anywhere you want to match one of many expressions.
#For example, the regular expression r'Batman|Tina Fey' will match either 'Batman' or 'Tina Fey'.
#When both Batman and Tina Fey occur in the searched string, the first occurrence of matching text will be returned as the Match object.
superHeros = re.compile(r'Batman|Superman|Hulk|Spiderman')
isSuperHeroFound = superHeros.search('Both hulk and superman is present. But only Batman will fight Superman')
#Remember, searching is case-sensitive, hence hulk != Hulk, so first occurrence of Batman is returned
print(isSuperHeroFound.group())                                                 #Batman
isSuperHeroFound = superHeros.search('Both hulk and Superman is present. But only Batman will fight Superman')
print(isSuperHeroFound.group())                                                 #Superman

#You can find all matching occurrences with the findall() method, which returns list of all Matching keywords
isSuperHeroFound = superHeros.findall('Both hulk and Superman is present. But only Batman will fight Spiderman')
print(isSuperHeroFound)                                                         #['Superman', 'Batman', 'Spiderman']
print(isSuperHeroFound[1])                                                      #Batman

#You can also use the pipe to match one of several patterns as part of your regex.
#For example, say you wanted to match any of the strings 'Batman', 'Batmobile', 'Batcopter', and 'Batbat'. Since all these strings start with Bat, it would be nice if you could specify that prefix only once. This can be done with parentheses.
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
isBatFound = batRegex.search('Batmobile lost a wheel.')
print(isBatFound.group())                                                       #Batmobile
print(isBatFound.group(1))                                                      #mobile

#The method call mo.group() returns the full matched text 'Batmobile', while mo.group(1) returns just the part of the matched text inside the first parentheses group, 'mobile'.
#By using the pipe character and grouping parentheses, you can specify several alternative patterns you would like your regex to match.
#If you need to match an actual pipe character, escape it with a backslash, like \|.
