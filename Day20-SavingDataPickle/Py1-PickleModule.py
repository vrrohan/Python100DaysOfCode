#When working with data, your data gets destroyed when your program ends.
#Suppose you are working with any game, after end of game, you need to store your data to some specific location so that when next new game started, same old configuration settings or players scores will be there.
#What is pickling?
#Pickle is used for serializing and de-serializing Python object structures, also called marshalling or flattening.
#Serialization refers to the process of converting an object in memory to a byte stream that can be stored on disk or sent over a network.
#Later on, this character stream can then be retrieved and de-serialized back to a Python object.

#What Can You Do With pickle?
#Pickling is useful for applications where you need some degree of persistency in your data. Your program's state data can be saved to disk, so you can continue working on it later on.
#It can also be used to send data over a Transmission Control Protocol (TCP) or socket connection, or to store python objects in a database.

#When Not To Use pickle
#If you want to use data across different programming languages, pickle is not recommended. Its protocol is specific to Python, thus, cross-language compatibility is not guaranteed.
#The same holds for different versions of Python itself. Unpickling a file that was pickled in a different version of Python may not always work properly, so you have to make sure that you're using the same version and perform an update if necessary.
#You should also try not to unpickle data from an untrusted source. Malicious code inside the file might be executed upon unpickling.

#Storing data with pickle. What can be pickled?
#You can pickle objects with the following data types:Booleans, Integers, Floats, Complex numbers, (normal and Unicode) Strings, Tuples, Lists, Sets, and Dictionaries that contain picklable objects.
#All the above can be pickled, but you can also do the same for classes and functions, for example, if they are defined at the top level of a module.
#Not everything can be pickled (easily), though: examples of this are generators, inner classes, lambda functions and defaultdicts.
#In the case of lambda functions, you need to use an additional package named dill. With defaultdicts, you need to create them with a module-level function.
import pickle
person_info = [{'name':'Guido', 'age':47, 'country':'usa'}, {'name':'elon', 'age':45, 'country':'canada'}, {'name':'lio', 'age':34, 'country':'spain'}]

#To pickle this dictionary, you first need to specify the name of the file you will write it to, which is persons in this case.
#Note that the file does not have an extension.
#To open the file for writing, simply use the open() function.
#The first argument should be the name of your file. The second argument is 'wb'. The w means that you'll be writing to the file, and b refers to binary mode. This means that the data will be written in the form of byte objects.
#If you forget the b, a TypeError: must be str, not bytes will be returned. You may sometimes come across a slightly different notation; w+b, but don't worry, it provides the same functionality.
writePickle = open('persons','wb')
#Once the file is opened for writing, you can use pickle.dump(), which takes two arguments: the object you want to pickle and the file to which the object has to be saved.
#pickle.dump(pickleObject, filename), Don't forget to close the file with close()
pickle.dump(person_info, writePickle)
writePickle.close()

#Python pickle module is used for serializing and de-serializing a Python object structure. Any object in Python can be pickled so that it can be saved on disk.
#What pickle does is that it “serializes” the object first before writing it to file. Pickling is a way to convert a python object (list, dict, etc.) into a character stream.
#The idea is that this character stream contains all the information necessary to reconstruct the object in another python script.
