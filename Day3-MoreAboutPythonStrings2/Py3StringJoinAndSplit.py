#join() - takes list & returns a string value
#The join() method is useful when you have a list of strings that need to be joined together into a single string value.
#The join() method is called on a string, gets passed a list of strings, and returns a string. The returned string is the concatenation of each string in the passed-in list.
#Remember that join() is called on a string value and is passed a list value.
fruits = ['apple', 'orange', 'plum', 'guava', 'blueberry']

string_of_fruits = ", ".join(fruits)
print("fruits are : " + string_of_fruits)                       #fruits are : apple, orange, plum, guava, blueberry

address = ['C142', 'Gail Vihar', 'Sector 23', 'Noida', 'UP']
string_of_address = " ".join(address)
print("address is : " + string_of_address)                      #address is : C142 Gail Vihar Sector 23 Noida UP

songList = ['My', 'Name', 'is', 'Slim', 'Shady']
string_of_song = "---".join(songList)
print("song name is : " + string_of_song)                       #song name is : My---Name---is---Slim---Shady

#The split() - method does the opposite: It’s called on a string value and returns a list of strings.
#By default, the string 'My name is Rohan' is split wherever whitespace characters such as the space, tab, or newline characters are found.
comment = "My name is Rohan\n This is split"
listComment = comment.split()
print(listComment)                  #['My', 'name', 'is', 'Rohan', 'This', 'is', 'split']

#You can pass a delimiter string to the split() method to specify a different string to split upon.
comment2 = "Java is oop, c++ is oop, html is not oop"
#whereever 'oop' is encountered, it will split it or break the string
#last 'oop' will again break the string & returns empty string
listComment2 = comment2.split("oop")
print(listComment2)                 #['Java is ', ', c++ is ', ', html is not ', '']

#The rjust() and ljust() string methods return a padded version of the string they are called on, with spaces inserted to justify the text.
#The first argument to both methods is an integer length for the justified string.
name = "Rohan"
#name rohan justified to 20 places from right
#since, rohan itself is 5 letters long, technically it will shift to 15 places from right padded with whitespaces + 5 letters of word - 'rohan' = 20
print(name.rjust(20))                  #               Rohan
#name rohan now justified to 20 places from the left
#similarly, it will write 5 places from word - 'rohan' & padd 15 whitespaces to right of rohan
print(name.ljust(20))                  #Rohan               |

#by default, ljust() & rjust() padd it with whitespace
#An optional second argument to rjust() and ljust() will specify a fill character other than a space character.
#it will now write - rohan + 15 * will be padded after rohan
print(name.ljust(20, '*'))                  #Rohan***************
#15 * will be paded before rohan
print(name.rjust(20, '*'))                  #***************Rohan
print(name.rjust(20, '='))                  #===============Rohan

#The center() string method works like ljust() and rjust() but centers the text rather than justifying it to the left or right.
print(name.center(20))
print(name.center(20, '*'))

#The startswith() and endswith() methods return True if the string value they are called on begins or ends (respectively) with the string passed to the method; otherwise, they return False.
team = "Manchester United 20"
print(team.startswith("Man"))                   #True
print(team.endswith("20"))                      #True
print(team.startswith("manc"))                  #False
print(team.endswith("united 20"))               #False
print(team.endswith("ted20"))                   #False
