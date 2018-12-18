#You can also slice a list i.e. create a sub-list using [a:b]
list_of_city = ['Noida', 'Delhi', 'Bangalore', 'Lucknow', 'Mumbai', 'Gurgaon']

#listName[a:b] means - slice list from index a till index (b-1)
#listName[:] means - slice list from start to end
#listName[a:] means - slice list from a till end of list
#listName[:b] or listName[0:b] means - slice list from start till index (b-1)
print(list_of_city[2:])                     #['Bangalore', 'Lucknow', 'Mumbai', 'Gurgaon']
print(list_of_city[:])                      #['Noida', 'Delhi', 'Bangalore', 'Lucknow', 'Mumbai', 'Gurgaon']
print(list_of_city[0:4])                    #['Noida', 'Delhi', 'Bangalore', 'Lucknow']
print(list_of_city[:5])                     #['Noida', 'Delhi', 'Bangalore', 'Lucknow', 'Mumbai']

#You can slice & get sublist using negative indexes also
#slice list from start till -1-1 = -2
print(list_of_city[:-1])                    #['Noida', 'Delhi', 'Bangalore', 'Lucknow', 'Mumbai']
#create a sublist from 3rd last to end
print(list_of_city[-3:])                    #['Lucknow', 'Mumbai', 'Gurgaon']
#Will return empty list becus a > b
print(list_of_city[-2:-5])                  #[]

#To print a list in reverse order
print(list_of_city[::-1])                   #['Gurgaon', 'Mumbai', 'Lucknow', 'Bangalore', 'Delhi', 'Noida']
