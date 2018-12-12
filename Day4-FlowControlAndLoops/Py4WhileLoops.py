#while loops make a block of code execute over and over again as long as condition in while is True
#while (some condition) : //block of code
#this will print 'spam' 5 times
spam = 0
while spam<5 :
    print('spam ' + str(spam))
    spam = spam + 1

#You can see, by default print() prints everytime in new line when called again & again
#use end=' ' - to print output on same line separated with spaces
#By default python’s print() function ends with a newline.
#Python’s print() function comes with a parameter called ‘end’. By default, the value of this parameter is ‘\n’, i.e. the new line character.
#You can end a print statement with any character/string using this parameter.
spam = 1
while spam<=5 :
    print('spam' + str(spam), end=' ')
    spam += 1

#to print on same line separated with commas , use : end=', '
#previous output still on same line, hence call \n newline to print new while loop print() statements on new line
print(end='\n')
spam = 1
while spam<=5 :
    print('spam' + str(spam), end=', ')
    spam += 1

#In while loop condition is always checked at start of each iteration & loop ends only when condition becomes False
#This is an infinite loop, as condition is always True
"""
i = 0
while True :
    print('Loop ' + str(i))
    i += 1
"""
#while loop that keeps on asking your name, untill your name is 'wizard'
name = ''
while name!='wizard' :
    name = input('Please enter your name : ')
print('Thank you!!!')

#while loop that keeps on repeating what you type , untill you type 'quit'
prompt = "Tell me Something & i will repeat.\nEnter 'quit' to exit : "
messg = ''
while messg!='quit' :
    messg = input(prompt)
    if messg!='quit' :
        print(messg)

#slicing string character by character from start
name = 'maps'
while name!='' :
    print(name, end=' ')            #maps aps ps s
    name = name[1:]

#True & False values for Other data types : 0, 0.0 and ''(empty string) evaluates to False , rest all other values are True
var = 0
while not var :
    var = int(input('Enter any non-zero number to stop : '))
