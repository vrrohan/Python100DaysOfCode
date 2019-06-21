#FileNotFoundError - exception occurs when you try to read from a file which is not present
filename = 'hello.txt'
"""
with open(filename) as fObject :
    contents = fObject.read()
>>>FileNotFoundError: [Errno 2] No such file or directory: 'hello.txt'
"""
"""
#To handle this, we need to handle this exception
try :
    with open(filename) as fObject :
        contents = fObject.read()
    print('file read success')
except FileNotFoundError as fnf :
    print('file not present', fnf)
finally :
    print('closing the file')

>>>file not present [Errno 2] No such file or directory: 'hello.txt'
>>>closing the file
"""

#lets suppose we need to count number of words from a given list of filenames
#read each filename from the list & count number of words from it
#Failing Silently :- Sometimes when exception occurs, you want your code to run as nothing happend. So you use - pass inside except block
#pass - tells python to do nothing & keep on running the program if exception occurs
def countWordsInFile(filename, contents) :
    words = contents.split()
    print('total number of words in file', filename, 'are :', len(words))

listOfFiles = ['fileOne.txt', 'fileTwo.txt', 'fileThree.txt', 'fileFour.txt']
for files in listOfFiles :
    try :
        with open(files) as f :
            contents = f.read()
            countWordsInFile(files, contents)
    except FileNotFoundError as nofile :
        pass

#ValueError - occurs when your type is right but values inside that are inappropriate
#Raised when an operation or function receives an argument that has the right type but an inappropriate value
"""
print('number is', num)
num = int(input('enter number : '))
>>> ValueError: invalid literal for int() with base 10: 'we'
"""

#TypeError - occurs when you try to add int to diffent object type like - num = 9 + 'hello'
#TypeError: unsupported operand type(s) for +: 'int' and 'str'
#Raised when an operation or function is applied to an object of inappropriate type.

#A syntax error occurs when parser detects an incorrect statement
