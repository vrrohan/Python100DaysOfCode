#You may be familiar with searching for text by pressing ctrl-F and typing in the words you’re looking for. Regular expressions go one step further: They allow you to specify a pattern of text to search for.
#You may not know a business’s exact phone number, but if you live in the United States or Canada, you know it will be three digits, followed by a hyphen, and then four more digits
#This is how you, as a human, know a phone number when you see it: 415-555-1234 is a phone number, but 4,155,551,234 is not.
#even though most modern text editors and word processors, such as Microsoft Word or OpenOffice, have find and find-andreplace features that can search based on regular expressions.
#Regular expressions are huge time-savers, not just for software users but also for programmers.
#A Regular Expression, is a sequence of characters that forms a search pattern. Regular Expression can be used to check if a string contains the specified search pattern.
#Python has a built-in package called re, which can be used to work with Regular Expressions.
#Regular expressions, called regexes for short, are descriptions for a pattern of text. For example, a \d in a regex stands for a digit character— that is, any single numeral 0 to 9.
#The regex \d\d\d-\d\d\d-\d\d\d\d is used by Python to match the same phone number text : a string of three numbers, a hyphen, three more numbers, another hyphen, and four numbers.
#Any other string would not match the \d\d\d-\d\d\d-\d\d\d\d regex.
#But regular expressions can be much more sophisticated. For example, adding a 3 in curly brackets ({3}) after a pattern is like saying, “Match this pattern three times.”
#So the slightly shorter regex \d{3}-\d{3}-\d{4} also matches the correct phone number format.
import re

#Passing a string value representing your regular expression to re.compile() returns a Regex pattern object (or simply, a Regex object).
#To create a Regex object that matches the phone number pattern, enter \d\d\d-\d\d\d-\d\d\d\d is the regular expression for the correct phone number pattern.
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#Now the phoneNumRegex variable contains a Regex object.

#Passing Raw Strings to re.compile( )
#Remember that escape characters in Python use the backslash (\).
#The string value '\n' represents a single newline character, not a backslash followed by a lowercase n. You need to enter the escape character \\ to print a single backslash.
#So '\\n' is the string that represents a backslash followed by a lowercase n. However, by putting an r before the first quote of the string value, you can mark the string as a raw string, which does not escape characters.
#Since regular expressions frequently use backslashes in them, it is convenient to pass raw strings to the re.compile() function instead of typing extra backslashes.
#Typing r'\d\d\d-\d\d\d-\d\d\d\d' is much easier than typing '\\d\\d\\d-\\d\\d\\d-\\d\\d\\d\\d'.

#Matching Regex Objects
#A Regex object’s search() method searches the string it is passed for any matches to the regex.
#The search() method will return None if the regex pattern is not found in the string.
#If the pattern is found, the search() method returns a Match object. Match objects have a group() method that will return the actual matched text from the searched string.

#The mo variable name is just a generic name to use for Match objects.
#we pass our desired pattern to re.compile() and store the resulting Regex object in phoneNumRegex.
#Then we call search() on phoneNumRegex and pass search() the string we want to search for a match.
#In this example, we know that our pattern will be found in the string, so we know that a Match object will be returned.
#we can call group() on isPhoneNumberFound to return the match. Writing isPhoneNumberFound.group() inside our print statement displays the whole match, 415-555-4242.
isPhoneNumberFound = phoneNumRegex.search('My name is Elon Musk. I live in Canada')
print(isPhoneNumberFound)                                                       #None
isPhoneNumberFound = phoneNumRegex.search('My name is Elon Musk. I live in Canada. 999-666-1234 at North')
print(isPhoneNumberFound)                                                       #<re.Match object; span=(40, 52), match='999-666-1234'>
print(isPhoneNumberFound.group())                                               #999-666-1234

#Slightly shorter regex for mobile number, most mobile numbers start with countrycode-9 digit mobile number => +91-987654321
mobileNumRegex = re.compile(r'(\d{2})-(\d{9})')
isMobileNumberFound = mobileNumRegex.search('Hello 12-3398, My mobile number is +91-998877665')
print(isMobileNumberFound.group())                                              #91-998877665

#Grouping with Parentheses
#Say you want to separate the area code or country code from the rest of the phone number.
#Adding parentheses will create groups in the regex: (\d\d\d)-(\d\d\d-\d\d\d\d).
#Then you can use the group() match object method to grab the matching text from just one group.
#The first set of parentheses in a regex string will be group 1. The second set will be group 2.
#By passing the integer 1 or 2 to the group() match object method, you can grab different parts of the matched text.
#Passing 0 or nothing to the group() method will return the entire matched text.
print('country code is :', isMobileNumberFound.group(1))                        #country code is : 91
print('mobile number is :', isMobileNumberFound.group(2))                       #mobile number is : 998877665
print(isMobileNumberFound.group(0))                                             #91-998877665

#For grouping always Remember to use your regex patterns in () paranthesis, else group(number will not work) Example - r'(group1)-(group2)-(group3)'
mobileNumRegex = re.compile(r'(\d{2})-(\d{9}-\d{6})')
isMobileNumberFound = mobileNumRegex.search('hello python regex. number is 91-987654321-110001')
print(isMobileNumberFound.group())                                              #91-987654321-110001
print(isMobileNumberFound.group(1))                                             #91
print(isMobileNumberFound.group(2))                                             #987654321-110001

#To retrieve all groups at once, use - groups(), which returns a tuple of groups
print(isMobileNumberFound.groups())                                             #('91', '987654321-110001')

#Since mo.groups() returns a tuple of multiple values, you can use the multiple-assignment trick to assign each value to a separate variable
#countrycode-mobilenumber-zipcode
mobileNumRegex = re.compile(r'(\d{2})-(\d{9})-(\d{6})')
isMobileNumberFound = mobileNumRegex.search('hello python regex. number is 91-987654321-110001')
countrycode, mobileNum, zipcode = isMobileNumberFound.groups()
print('country code : ' + str(countrycode))
print('mobile number : ' + str(mobileNum))
print('zipcode : ' + str(zipcode))
"""
country code : 91
mobile number : 987654321
zipcode : 110001
"""

#Parentheses have a special meaning in regular expressions, but what do you do if you need to match a parenthesis in your text?
#For instance, maybe the phone numbers you are trying to match have the area code set in parentheses.
#In this case, you need to escape the ( and ) characters with a backslash.
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
isPhoneNumberFound = phoneNumRegex.search('My phone number is (415) 555-4242.')
print(isPhoneNumberFound.group(1))                                              #(415)
print(isPhoneNumberFound.group(2))                                              #555-4242
#The \( and \) escape characters in the raw string passed to re.compile() will match actual parenthesis characters.
