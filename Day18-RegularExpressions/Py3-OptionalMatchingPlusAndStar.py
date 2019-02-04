import re
#Optional Matching with the Question Mark
#Sometimes there is a pattern that you want to match only optionally. That is, the regex should find a match whether or not that bit of text is there.
#The ? character flags the group that precedes it as an optional part of the pattern.
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())                                                              #Batman
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())                                                              #Batwoman

#The (wo)? part of the regular expression means that the pattern wo is an optional group. The regex will match text that has zero instances or one instance of wo in it.
#This is why the regex matches both 'Batwoman' and 'Batman'.

#Using the earlier phone number example, you can make the regex look for phone numbers that do do or do not have an area code.
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
print(mo1.group())                                                              #415-555-4242

mo2 = phoneRegex.search('My number is 555-4242')
print(mo2.group())                                                              #555-4242

#You can think of the ? as saying, “Match zero or one of the group preceding this question mark.”
#If you need to match an actual question mark character, escape it with \?.

#Matching Zero or More with the Star
#The * (called the star or asterisk) means “match zero or more” — the group that precedes the star can occur any number of times in the text.
#It can be completely absent or repeated over and over again.
batRegex = re.compile(r'Bat(wo)*man')
isBatFound = batRegex.search('The Adventures of Batman')
print(isBatFound.group())                                                       #Batman
isBatFound = batRegex.search('The Adventures of Batwoman')
print(isBatFound.group())                                                       #Batwoman
isBatFound = batRegex.search('The Adventures of Batwowowowoman')
print(isBatFound.group())                                                       #Batwowowowoman

#For 'Batman', the (wo)* part of the regex matches zero instances of wo in the string
#for 'Batwoman', the (wo)* matches one instance of wo
#and for 'Batwowowowoman', (wo)* matches four instances of wo.
#If you need to match an actual star character, prefix the star in the regular expression with a backslash, \*.

#Matching One or More with the Plus
#While * means “match zero or more,” the + (or plus) means “match one or more.”
#Unlike the star, which does not require its group to appear in the matched string, the group preceding a plus must appear at least once. It is not optional.
batRegex = re.compile(r'Bat(wo)+man')
isBatFound = batRegex.search('The Adventures of Batwoman')
print(isBatFound.group())                                                       #Batwoman
isBatFound = batRegex.search('The Adventures of Batwowowowoman')
print(isBatFound.group())
isBatFound = batRegex.search('The Adventures of Batman')                        #Batwowowowoman
print(isBatFound)                                                               #None
#If you need to match an actual plus sign character, prefix the plus sign with a backslash to escape it: \+.

#Matching Specific Repetitions with Curly Brackets
#If you have a group that you want to repeat a specific number of times, follow the group in your regex with a number in curly brackets.
#For example, the regex (Ha){3} will match the string 'HaHaHa', but it will not match 'HaHa', since the latter has only two repeats of the (Ha) group.
#Instead of one number, you can specify a range by writing a minimum, a comma, and a maximum in between the curly brackets.
#For example, the regex (Ha){3,5} will match 'HaHaHa', 'HaHaHaHa', and 'HaHaHaHaHa'.
#You can also leave out the first or second number in the curly brackets to leave the minimum or maximum unbounded. For example, (Ha){3,} will match three or more instances of the (Ha) group, while (Ha){,5} will match zero to five instances.
#Curly brackets can help make your regular expressions shorter.
#These two regular expressions match identical patterns: (Ha){3} , (Ha)(Ha)(Ha)
#And these two regular expressions also match identical patterns: (Ha){3,5}, ((Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha)(Ha))
haRegex = re.compile(r'(Ha){3}')
isThreeHaFound = haRegex.search('HaHaHa')
print(isThreeHaFound.group())                                                   #HaHaHa
isThreeHaFound = haRegex.search('Ha')
print(isThreeHaFound == None)                                                   #True

haRegex = re.compile(r'(Ha){3,5}')
isThreeHaFound = haRegex.search('HaHaHaHa')
print(isThreeHaFound.group())                                                   #HaHaHaHa
isThreeHaFound = haRegex.search('today is Sunday, HaHa')
print(isThreeHaFound==None)                                                     #True
