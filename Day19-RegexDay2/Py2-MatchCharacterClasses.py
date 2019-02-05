import re
#Most letters and characters will simply match themselves. For example, the regular expression test will match the string test exactly.
#There are exceptions to this rule; some characters are special metacharacters, and don’t match themselves.
#Meta characters are . ^ $ * + ? { } [ ] \ | ( )
#We have already seen *, +, ?(optional), |, {}
#Now lets use - []
#[abc] - will match anyone a, b or c
vowelsRegex = re.compile(r'[aeiou]', re.I)
vowelsFoundRegex = vowelsRegex.findall('Hello Python')
print(vowelsFoundRegex)                                                         #['e', 'o', 'o']

#Will match any digits between 0 to 9
digitRegex = re.compile(r'[0-9]')
digitRegexFound = digitRegex.findall('Hello Python ver 3.75, HTML5, speed is 480 kmps')
print(digitRegexFound)                                                          #['3', '7', '5', '5', '4', '8', '0']

#^ - means that doesnot match any given character in []
charsRegex = re.compile(r'[^abcdefg]')
charsRegexFound = charsRegex.findall('Today is Monday')
print(charsRegexFound)                                                          #['T', 'o', 'y', ' ', 'i', 's', ' ', 'M', 'o', 'n', 'y']

#To match [, ] or \, precede it with a backslash \\ or \[ or \]
anyRegex = re.compile(r'\\')
regexFound = anyRegex.findall('Name is : [Elon Musk], hell\opy')
print(regexFound)                                                               #['\\']

#\d - any decimal number between 0-9, equivalent to [0-9]
#\D - any non-digit character, equivalent to [^0-9]
#\s - matches any whitespace character, equivalent to [ \t\n\r\f\v]
#\S - matches any non-whitespace character, equivalent to [^ \t\n\r\f\v]
#\w - matches any alphanumeric character, equivalent to [a-z0-9A-Z_]
#\W+ - matches any non-alphanumeric character, equivalent to [^a-z0-9A-Z_]
#Example - [\s,.] will match only whitespace, comma & dot .
#[.] will match anything including newline also
#\s+ - means one or more than one whitespace
#\d is shorthand for the regular expression (0|1|2|3|4|5|6|7|8|9). There are many such shorthand character classes like \d, \w, \s
#Character classes are nice for shortening regular expressions. The character class [0-5] will match only the numbers 0 to 5; this is much shorter than typing (0|1|2|3|4|5).
anyRegex = re.compile(r'\d+\w+')
regexFound = anyRegex.findall('Hello Python. 10HTML, 1Python, 3 c++, 7c')
print(regexFound)                                                               #['10HTML', '1Python', '7c']

#Caret and Dollar Sign characters
#You can also use the caret symbol (^) at the start of a regex to indicate that a match must occur at the beginning of the searched text.
#Likewise, you can put a dollar sign ($) at the end of the regex to indicate the string must end with this regex pattern.
#And you can use the ^ and $ together to indicate that the entire string must match the regex—that is, it’s not enough for a match to be made on some subset of the string.

#For example, the r'^Hello' regular expression string matches strings that begin with 'Hello'
beginsWithHello = re.compile(r'^Hello')
print(beginsWithHello.search('Hello world!'))                                   #<_sre.SRE_Match object; span=(0, 5), match='Hello'>
print(beginsWithHello.search('He said hello.') == None)                         #True
print(beginsWithHello.search('Hello Python').group())                           #Hello

#The r'\d$' regular expression string matches strings that end with a numeric character from 0 to 9
endsWithNumber = re.compile(r'\d$')
print(endsWithNumber.search('Your number is 42'))                               #<_sre.SRE_Match object; span=(16, 17), match='2'>
print(endsWithNumber.search('Your number is forty two.') == None)               #True

#The r'^\d+$' regular expression string matches strings that both begin and end with one or more numeric characters.
wholeStringIsNum = re.compile(r'^\d+$')
print(wholeStringIsNum.search('1234567890'))                                    #<_sre.SRE_Match object; span=(0, 10), match='1234567890'>
print(wholeStringIsNum.search('12345xyz67890') == None)                         #True
print(wholeStringIsNum.search('12 34567890') == None)                           #True
print(wholeStringIsNum.search('12helloPython') == None)                         #True

#The last two search() calls demonstrate how the entire string must match the regex if ^ and $ are used.
#“Carrots cost dollars” to remind that the caret comes first and the dollar sign comes last.
