#Generate a ten-character alphanumeric password with at least one lowercase character, at least one uppercase character, at least one digits and at least one special character.
import random
import string

#First things first, lets shuffle a string
#In python, you can shuffle a string using 2 ways
#Approach 1:- concatenate all characters of string to empty string using sample(), becus sample() selects only non-repeated character each time
#we need to create random string same as length of actual string hence, pass 2nd argument in sample() as len(actualString)
name = 'Lamborgini'
randomName = ''
randomName = randomName.join(random.sample(name, len(name)))
"""
Output1:- Random string is : rbiLongmia
Output2:- Random string is : ormgaiLbin
Output3:- Random string is : Loiibnagrm
"""
print('Random string is : ' + randomName)

#Approach 2:- Use random.shuffle(list), that takes list as argument, but first need to convert string back to list using list(string)
name = 'Manchester'
#change string to list
lisName = list(name)
#now shuffle the list simply
random.shuffle(lisName)
#convert list back to string using join()
shuffledName = ''.join(lisName)
"""
Output1:- Shuffled name is : rehstcnMae
Output2:- Shuffled name is : ntMcreesah
Output3:- Shuffled name is : cahesMretn
"""
print('Shuffled name is : ' + shuffledName)

#first create a password with single uppercase, single lowercase, single digit & single special character
password = random.choice(string.ascii_lowercase)
password += random.choice(string.ascii_uppercase)
password += random.choice(string.digits)
password += random.choice(string.punctuation)

#now since password contains atleast one uppercase, one lowercase, one digit & one special character
#now need to work on length of password, to generate a strong password, it must have minimum length of 10
#lets create a collection of all uppercase + lowercase + punctuation, we will choose remaining characters of password from this collection
passCollection = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits

#since password is already of length 4, we need loop till 6 to make password of length 10
for i in range(6) :
    password += random.choice(passCollection)

#since password first 4 characters are guessable, we need to shuffle the password
print("Strong password without shuffle : " + password)
strongPassword = ''.join(random.sample(password, len(password)))
"""
Output1:- Strong password is : jF#7Ik_[K6
Output2:- Strong password is : JZI<q7")a#
Output3:- Strong password is : jI?>L7h'Ri
"""
print('Strong password is : ' + strongPassword)
