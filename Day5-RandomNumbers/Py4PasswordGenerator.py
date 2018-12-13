#This program will generate 10 different strong passwords based on User information
#Username length : minimum 5, maximum 20
#birth year : 1950 - 2018
#birth month : only first 3 characters of month like - Jan, Feb, Sep etc
#phrase : minimum length 5, maximum length 30
#mobile number : length exactly 10 digits & cannot start with 0
import random
import string

username = str(input("Enter username : "))
print("Enter date of birth : ")
day = str(input("Day : "))
month = str(input("Month : "))
year = str(input("Year : "))
mobNumber = str(input("Enter mobile number : "))
#phrase = input("Enter your catch phrase : ")

listOfPossibleUserNames = []


if ((len(username)<5) or (len(username)>20)) :
    print("Too small username")
else :
    #create list of random group of characters from username
    listUserName = username.split(' ')
    trimmedList = ''.join(listUserName)
    for i in range(len(trimmedList)-3) :
        listOfPossibleUserNames.append(trimmedList[i:i+4])


if ((mobNumber.startswith('0')) or (len(mobNumber)!=10)) :
    print('Invalid mobile number')
else :
    listOfPossibleMobileNumbers = [mobNumber[0:5], mobNumber[len(mobNumber)-3:]]

"""
for i in listOfPossibleUserNames :
    print(i, end= ' ')
"""
"""
for i in listOfPossibleMobileNumbers :
    print(i, end=' ')
"""
"""
dobList = [day, month, year]
for i in dobList :
    print(i, end=' ')
"""

digits = [day, year, year[2:], mobNumber[0:5], mobNumber[len(mobNumber)-3:]]
for i in digits :
    print(i)

specialCharacters = string.punctuation
finalPasswordListGenerator = [listOfPossibleUserNames, digits, specialCharacters]
finalStrongPassword = ''

listOfUppercasePassword = [username.split(' ')[0][:2], username.split(' ')[0][]]

for i in range(3) :
    ls = finalPasswordListGenerator[random.randint(0, len(finalPasswordListGenerator)-1)]
    finalStrongPassword += str(ls[random.randint(0, len(ls)-1)])

print("final password is : " + finalStrongPassword)
