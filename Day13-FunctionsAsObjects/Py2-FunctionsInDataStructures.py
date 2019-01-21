#You can store functions in a data structure or collection like lists, dictionary, sets etc
def yell(text) :
    return text.upper() + '!'

#You can store any function in a list & you can even call a function object stored in that list without assigning it to any variable
funcList = [yell, str.upper, str.lower]
for f in funcList :
    print(f)
"""
<function yell at 0x000001D9F827C2F0>
<method 'upper' of 'str' objects>
<method 'lower' of 'str' objects>
"""

print(funcList[0])                                      #<function yell at 0x000001494777C2F0>

for f in funcList :
    print(f('elon musk'))
"""
ELON MUSK!
ELON MUSK
elon musk
"""

#You can directly pass an argument to a function when calling
print(funcList[0]('guido van rossum'))                  #GUIDO VAN ROSSUM!

#Nested Functions or Inner functions i.e. functions inside another function
def speak(text) :
    def whis(t) :
        return t.lower()
    return whis(text).capitalize() + '!!!'

#Everytime you call speak(), it defines a new inner function whis() & then calls it
#whis() doesnot exist outside speak()
print(speak('ELON MUSK'))                               #Elon musk!!!

"""
print(whis('hello elon'))
NameError: name 'whis' is not defined
"""

"""
print(speak.whis)
AttributeError: 'function' object has no attribute 'whis'
"""

#This function selects appropriate function object & return it, based on vol
def getSpeak(vol) :
    def whis(t) :
        return t.lower()

    def yell(t) :
        return t.upper()

    if (vol>50) :
        return yell
    else :
        return whis

print(getSpeak(10))                                     #<function getSpeak.<locals>.whis at 0x000001A3B06FEB70>
print(getSpeak(80))                                     #<function getSpeak.<locals>.yell at 0x0000020FE33EEBF8>

retFunc = getSpeak(10)
print(retFunc('Guido Van Rossum'))                      #guido van rossum
retFunc = getSpeak(90)
print(retFunc('Elon Musk'))                             #ELON MUSK
