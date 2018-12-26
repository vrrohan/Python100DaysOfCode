#You can search or look for an item in a list using in or not in
marks = [45, 89, 92, 70, 66, 56]
#in or not in returns boolean value
print(30 in marks)                      #False
print(99 not in marks)                  #True

countries = ['India', 'Japan', 'USA', 'France', "Russia"]
if 'France' in countries :
    print('France is present in the list')                          #France is present in the list
else :
    print('France not present in the list')

#index(itemToSearch, start{optional}, end{optional}) -  searches for given element from start of the list and returns the lowest index where the element appears.
colors = ['red', 'blue', 'green', 'blue', 'pink']
print(colors.index('blue'))             #1

#If any element which is not present is searched, it returns a ValueError
#print(colors.index('brown'))
#ValueError: 'brown' is not in list

#count(element):- returns the occurrence count of given element in the list. If its greater than 0, it means given element exists in list.
colors = ['red', 'blue', 'green', 'blue', 'pink']
print(colors.count('blue'))                 #2
print(colors.count('black'))                #0
