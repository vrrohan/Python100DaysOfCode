#List comprehensions offer a succinct way to create lists based on existing lists. When using list comprehensions, lists can be built by leveraging any iterable, including strings and tuples.
#You can literally build a new list using another list with some conditions in a single line
#[{varName} for {varName} in {listName} {if-conditional}]
name = "Python"
listName = [x for x in name]
print(listName)                             #['P', 'y', 't', 'h', 'o', 'n']

colors = ['red', 'green', 'blue', 'yellow', 'orange']
#col should be same in both places, else if use - [x for col in colors] will give error
listColor2 = [col for col in colors]
print(listColor2)                           #['red', 'green', 'blue', 'yellow', 'orange']

#Create a list of squares of each number
numbers = [1, 2, 3, 4, 5]
squareList = [(n*n) for n in numbers]
print(squareList)                           #[1, 4, 9, 16, 25]

#Create a list of only even numbers
numbers = [12, 13, 5, 8, 4, 99, 101, 144, 72]
evenList = [num for num in numbers if (num%2==0)]
print(evenList)                             #[12, 8, 4, 144, 72]

#Create a list having mutiple of 3 between 1 to 100
list3 = [x for x in range(1, 100) if (x%3==0)]
print(list3)                                #[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]

#Creating list having multiple of both 3 & 5
list4 = [x for x in range(1,100) if (x%3==0) and (x%5==0)]
print(list4)                                #[15, 30, 45, 60, 75, 90]

#Using nested loops for list comprehension
"""
mylist = []
for x in [2, 4, 6] : --> Outer for loop
    for y in [1, 3, 5] : --> Inner for loop
        mylist.append(x+y)
"""
#[(x+y) {outer for loop} {inner for loop}]
#creating list of 1st 25 integers
list1 = [x for x in range(1,4)]
list2 = [x for x in range(4,6)]
print(list1)                        #[1, 2, 3]
print(list2)                        #[4, 5]
finalList = [(x+y) for x in list1 for y in list2]
print(finalList)                    #[5, 6, 6, 7, 7, 8]
