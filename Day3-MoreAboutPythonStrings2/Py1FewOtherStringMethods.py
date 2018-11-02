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
