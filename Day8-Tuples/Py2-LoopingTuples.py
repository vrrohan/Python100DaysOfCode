fruits = ('apple', 'orange', 'mango', 'plum', 'grapes')

#using for loop , to loop over any tuple
for f in fruits :
    print(f, end=' ')                   #apple orange mango plum grapes
print()

#using enumerate() to loop over both index & its element
"""
apple present at index 0
orange present at index 1
mango present at index 2
plum present at index 3
grapes present at index 4
"""
for (index, elem) in enumerate(fruits) :
    print(elem + ' present at index ' + str(index))

#using for loop and range()
for x in range(len(fruits)) :
    print(fruits[x], end=', ')                      #apple, orange, mango, plum, grapes,
print()

#using while loop
index = 0
while (index<len(fruits)) :
    print(fruits[index], end=', ')                  #apple, orange, mango, plum, grapes,
    index += 1
