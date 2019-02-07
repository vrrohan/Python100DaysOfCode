#Unpickling files
#The process of loading a pickled file back into a Python program. Use the open() function again, but this time with 'rb' as second argument (instead of wb).
#The r stands for read mode and the b stands for binary mode. You can use 'rb' or 'r+b'
#You'll be reading a binary file. Assign this to infile. Next, use pickle.load(), with infile as argument, and assign it to a variable
#The contents of the file are now assigned to this new variable. Again, you'll need to close the file at the end.
import pickle
readPickle = open('persons', 'r+b')
personsInfo = pickle.load(readPickle)
for per in personsInfo :
    print(per)
readPickle.close()
