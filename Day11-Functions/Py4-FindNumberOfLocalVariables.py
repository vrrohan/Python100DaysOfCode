# co_nlocals() - function which returns the number of local variables used by the function
#functionName.__code__.co_nlocals returns total number of local variables used by a function
name = 'elon'
def getInfo(age) :
    country = 'india'
    print(age, country)

def showInfo(name, age, city, *hobbies) :
    print(name, age, city)
    print(hobbies)

print(getInfo.__code__.co_nlocals)                      #2
print(showInfo.__code__.co_nlocals)                     #4
