import re
#You can split any string using the split()
line = 'Hello Everyone, Today is Monday'
lineList = line.split(' ')
print(lineList)                                                                 #['Hello', 'Everyone,', 'Today', 'is', 'Monday']

#Substituting Strings with the sub() Method
#Regular expressions can not only find text patterns but can also substitute new text in place of those patterns.
#The sub() method for Regex objects is passed two arguments. The first argument is a string to replace any matches. The second is the string for the regular expression.
#The sub() method returns a string with the substitutions applied.
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))                    #CENSORED gave the secret documents to CENSORED.

#Sometimes you may need to use the matched text itself as part of the substitution.
#In the first argument to sub(), you can type \1, \2, \3, and so on, to mean “Enter the text of group 1, 2, 3, and so on, in the substitution.”
#For example, say you want to censor the names of the secret agents by showing just the first letters of their names.
#To do this, you could use the regex Agent (\w)\w* and pass r'\1****' as the first argument to sub().
#The \1 in that string will be replaced by whatever text was matched by group 1 — that is, the (\w) group of the regular expression.

agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))                 #A**** told C**** that E**** knew B**** was a double agent.'

#The subn() method does the same work, but returns a 2-tuple containing the new string value and the number of replacements that were performed
p = re.compile('(blue|white|red)')
print(p.subn('colour', 'blue socks and red shoes'))                             #('colour socks and colour shoes', 2)
print(p.subn('colour', 'no colours at all'))                                    #('no colours at all', 0)
