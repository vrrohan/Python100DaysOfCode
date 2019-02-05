import re
#The Wildcard Character
#The . (or dot) character in a regular expression is called a wildcard and will match any character except for a newline.
atRegex = re.compile(r'.at', re.I)
atRegexFound = atRegex.findall('The cat is at Mat with the Rat on the yellow sat on flat')
print(atRegexFound)                                                             #['cat', ' at', 'Mat', 'Rat', 'sat', 'lat']
#Remember that the dot character will match just one character, which is why the match for the text flat in the previous example matched only lat. That is why 'at' comes with single space ' at'
#To match an actual dot, escape the dot with a backslash \.

#Matching Everything with Dot-Star .*
#Sometimes you will want to match everything and anything.
#For example, say you want to match the string 'First Name:', followed by any and all text, followed by 'Last Name:', and then followed by anything again.
#You can use the dot-star (.*) to stand in for that “anything.” Remember that the dot character means “any single character except the newline,” and the star character means “zero or more of the preceding character.”
nameRegex = re.compile(r'Firstname:(.*) Lastname:(.*)')
nameRegexFound = nameRegex.search('Hello everyone, Firstname:Monty Lastname:Python')
print(nameRegexFound.group())                                                   #Firstname:Monty Lastname:Python
print(nameRegexFound.group(1))                                                  #Monty
print(nameRegexFound.group(2))                                                  #Python

#The dot-star uses greedy mode: It will always try to match as much text as possible.
#To match any and all text in a nongreedy fashion, use the dot, star, and question mark (.*?).
#Like with curly brackets, the question mark tells Python to match in a nongreedy way.
nameRegex = re.compile(r'<.*>')
nameRegexFound = nameRegex.search('<html><head>Hello Python</head></html>')
print(nameRegexFound.group())                                                   #<html><head>Hello Python</head></html>

nameRegex = re.compile(r'<.*?>')
nameRegexFound = nameRegex.search('<html><head>Hello Python</head></html>')
print(nameRegexFound.group())                                                   #<html>

nameRegex = re.compile(r'<.*>')
nameRegexFound = nameRegex.findall('<html><head>Hello Python</head></html>')
print(nameRegexFound)                                                           #['<html><head>Hello Python</head></html>']

nameRegex = re.compile(r'<.*?>')
nameRegexFound = nameRegex.findall('<html><head>Hello Python</head></html>')
print(nameRegexFound)                                                           #['<html>', '<head>', '</head>', '</html>']

#Matching Newlines with the Dot Character
#The dot-star will match everything except a newline. By passing re.DOTALL as the second argument to re.compile(), you can make the dot character match all characters, including the newline character.
noNewlineRegex = re.compile('.*')
no = noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
print(no.group())                                                               #Serve the public trust.
newlineRegex = re.compile('.*', re.DOTALL)
newLine = newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
print(newLine.group())                                                          #Serve the public trust.\nProtect the innocent.\nUphold the law.

#The regex noNewlineRegex, which did not have re.DOTALL passed to the re.compile() call that created it, will match everything only up to the first newline character
#whereas newlineRegex, which did have re.DOTALL passed to re.compile(), matches everything. This is why the newlineRegex.search() call matches the full string, including its newline characters.
