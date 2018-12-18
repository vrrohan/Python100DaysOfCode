#This program will generate 10 different strong passwords based on User information
#Username length : minimum 5, maximum 20
#birth year : 1950 - 2018
#birth month : only first 3 characters of month like - Jan, Feb, Sep etc
#mobile number : length exactly 10 digits & cannot start with 0
import random
import string

username = str(input("Enter username : "))
print("Enter date of birth : ")
day = str(input("Day : "))
month = str(input("Month : "))
year = str(input("Year : "))
mobNumber = str(input("Enter mobile number : "))

#String which stores our generated password , which is strong & minimum length of 10
finalStrongPassword = ''
#Strong password contains combinations of - uppercase, lowercase, digits & special Characters
#So we create list of all these to store our all combinations of user information
listOfLowerCaseUserNames = []
listOfLowerCaseUserNameInitials = []
listOfUpperCaseUserNames = []
listOfUpperCaseUserNameInitials = []
listOfPossibleMobileNumbers = []
listOfPossibleDigits = []
listOfPossibleSpecialCharacters = []

#Here check whether length of username is less than 5 or not
if ((len(username)<5) or (len(username)>30)) :
    print("Too small username")
else :
    #Splitting user's firstname & lastname into a list separated by spaces
    listUserName = username.split(' ')
    #We trimmed & remove spaces between user's firstname & lastname
    trimmedUserName = ''.join(listUserName)
    #get both uppercase & lowercase form of trimmed username
    trimmedUpperUserName = trimmedUserName.upper()
    trimmedLowerUserName = trimmedUserName.lower()
    #Creating & appending all different (group of 4) possible username's into a list
    #Example- If name is 'wayne rooney' , possible group of 4 characters combination is : ['wayn', 'ayne', 'yner', 'nero', 'eroo', 'roon', 'oone', 'oney']
    for i in range(len(trimmedUserName)-3) :
        listOfLowerCaseUserNames.append(trimmedUserName[i:i+4])
    #Creating possible use cases from initials of username
    #If name is - 'Wayne Rooney' - initials created were ['wa', 'ne', 'ro', 'ey', 'wr', 'waro']
    #All this possible combinations were stored in another list of initials
    for i in range(2) :
        listOfLowerCaseUserNameInitials.append(listUserName[i][:2])
        listOfLowerCaseUserNameInitials.append(listUserName[i][len(listUserName[i])-2:])
    listOfLowerCaseUserNameInitials.append(listUserName[0][:2] + listUserName[1][:2])
    listOfLowerCaseUserNameInitials.append(listUserName[0][0] + listUserName[1][0])

#We check if lowercase username list is filled, it means we have all possible combinations of username saved
#We then save all these combinations into another parallel list of uppercase combinations
#Example:- lowercase group of 4 username :- 'wayn' --> 'WAYN' is saved into listOfUpperCaseUserNames
#Similarly , each lowercase combination is converted into uppercase combination & stored in different list
if(len(listOfLowerCaseUserNames)>0) :
    for i in range(len(listOfLowerCaseUserNames)) :
        listOfUpperCaseUserNames.append(listOfLowerCaseUserNames[i].upper())

#Example -initials in lowercase : ['wa', 'ne', 'ro', 'ey', 'wr', 'waro'] is parallely saved into listOfUpperCaseUserNameInitials[]
#initials in uppercase : ['WA', 'NE', 'RO', 'EY', 'WR', 'WARO']
if(len(listOfLowerCaseUserNameInitials)>0) :
    for i in range(len(listOfLowerCaseUserNameInitials)) :
        listOfUpperCaseUserNameInitials.append(listOfLowerCaseUserNameInitials[i].upper())

#Checking whether mobile number is exactly of length = 10 & didn't start with 0
if ((mobNumber.startswith('0')) or (len(mobNumber)!=10)) :
    print('Invalid mobile number')
else :
    #If not, append first 5 & last 3 digits of mobile number to list of possible mobile numbers
    listOfPossibleMobileNumbers.append(mobNumber[0:5])
    listOfPossibleMobileNumbers.append(mobNumber[len(mobNumber)-3:])

#appending both combinations of mobile number into list of digits , from which we select a pair of digit for our password
for i in range(2) :
    listOfPossibleDigits.append(listOfPossibleMobileNumbers[i])

#Now add date of birth & birth year & last 2 digits of birth year to listOfPossibleDigits[]
listOfPossibleDigits.append(day)
listOfPossibleDigits.append(year)
listOfPossibleDigits.append(year[len(year)-2:])

#Now also append month of birth to both upper & lowercase list
listOfLowerCaseUserNames.append(month.lower())
listOfUpperCaseUserNames.append(month.upper())

#Selecting 4 different special characters & store into possible list of special characters
specialCharacters = string.punctuation
for i in range(4) :
    listOfPossibleSpecialCharacters.append(random.choice(specialCharacters))

#We create this list to randomly select any 1 i.e. username's or username initials list
lower_random_list = [listOfLowerCaseUserNames, listOfLowerCaseUserNameInitials]
#We create this list to randomly select any 1 i.e. uppercase username's or uppercase username initials list
upper_random_list = [listOfUpperCaseUserNames, listOfUpperCaseUserNameInitials]

#Now randomly select anyone, we now have 1 random uppercase list & 1 random lowercase list
lower_selected_list = random.choice(lower_random_list)
upper_selected_list = random.choice(upper_random_list)

#This is final list, which contains 1 uppercase list, 1 lowercase list, 2 list of special characters & 1 list of possible digits to make our password strong
finalSelectedList = [lower_selected_list, upper_selected_list, listOfPossibleDigits, listOfPossibleSpecialCharacters, listOfPossibleSpecialCharacters]
#now shuffle the list, so that password pattern is not specific to elements position in list i.e. first lowercase in passwordm then uppercase in password
random.shuffle(finalSelectedList)

#Now loop through the shuffled list. Here we get 1st list from shuffled list
#Then, we randomly select anyone combination from that list & concatenate it to our password which is in string form
for i in finalSelectedList :
    num = random.randint(0, len(i)-1)
    finalStrongPassword += i[num]

#finally again check if password length is less than 10
#If password length < 10, we keep on choosing randomly between uppercase, lowercase, digits & specialCharacters from finalSelectedList[]
#We keep on shuffling & keep on choosing random elements
while(len(finalStrongPassword)<10) :
    random.shuffle(finalSelectedList)
    anyList = random.choice(finalSelectedList)
    anyNum = random.choice(anyList)
    finalStrongPassword += anyNum

print('Strong Password generated is : ' + finalStrongPassword)
