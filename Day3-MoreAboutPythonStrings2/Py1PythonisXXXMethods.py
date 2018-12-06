#Python isXXX() methods
#isupper() & islower() methods
#isupper() - returns True, if atleast 1 character is in uppercase A to Z & all characters must be in uppercase A to Z
#If any lowercase a to z is present in string, it will return False
print("PYTHON".isupper())               #prints- True, becus all characters are in uppercase
print("PYTHon".isupper())               #prints- False, becus 2 lowercase o & n is present
print("PYTHON12345".isupper())          #prints- True, becus all characters are in uppercase, except 12345
print("P!@#{$%^&*()}".isupper())        #prints- True, becus single character present P, is in uppercase
print("12345".isupper())                #prints- False, becus there is none character present
print("".isupper())                     #prints- False, becus no character present here
print("PYTH12345e".isupper())           #prints- False, becus one small e is present at the end

#So, whatever character present in string from a-z, all must present in uppercase , else it will return False
#islower() - returns True, if atleast 1 character is in lowercase a-z & all characters must be in lowercase a to z
#If any uppercase a to z is present in string, or none character in string is in lowercase a to z, it will return False
print("python".islower())               #prints- True
print("Python".islower())               #prints- False, 1 uppercase P is present
print("PYTHON".islower())               #prints- False
print("python12345".islower())          #prints- True
print("012345".islower())               #prints- False
print("PYTHON012345".islower())         #prints- False
print("#{$m@$@$03}".islower())          #prints- True

#isalpha() returns True if the string consists only of letters and is not blank.
print("hello is alpha() : ", "hello".isalpha())                     #True
print("hello123 is alpha() : ", "hello123".isalpha())               #False

#isalnum() returns True if the string consists only of letters and numbers and is not blank.
print("helLLO123 is alnum() : ", "helLLO123".isalnum())             #True
print("[whitespace] is alnum() : ", " ".isalnum())                  #False

#isdecimal() returns True if the string consists only of numeric characters and is not blank.
print("1234s is decimal() : ", "1234s".isdecimal())             #False
print("4.55 is decimal() : ", "4.55".isdecimal())               #returns - False, becus . is there
print("4500 is decimal() : ", "4500".isdecimal())               #True
print("[whitespace] is decimal() : ", " ".isdecimal())          #False

#isspace() returns True if the string consists only of spaces, tabs, and newlines and is not blank.
print("[tab][tab] is space() : ", "     ".isspace())            #True

#istitle() returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters.
print("This Is Title".istitle())            #True
print("THIS Is Title".istitle())            #False
print("This Is Title 123".istitle())        #True
print("12345A".istitle())                   #True

#isdigit() - returns “True” if all characters in the string are digits, Otherwise, It returns “False”.
print("234567".isdigit())                   #True
print("0123a3".isdigit())                   #False
print("".isdigit())                         #False
