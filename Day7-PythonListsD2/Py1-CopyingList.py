#List Copying Method 1 - Using Assignment Operator (=)
#Assignment operator (=) doesn't make a new copy of list, instead it makes 2 variables point to same list
#Here both demo_list & copylist1 point to same list. Hence, changes made by any one variable will affect both
#id(object) - accepts a single parameter and is used to return the identity of an object. This identity has to be unique and constant for this object during the lifetime.
demo_list = ['wayne', 'paul', 25, ['manchester', 'uk']]
copylist1 = demo_list
print('demo_list : ', demo_list, ' at id : ', id(demo_list))                    #demo_list :  ['wayne', 'paul', 25, ['manchester', 'uk']]  at id :  2200279796808
print('copylist1 : ', copylist1, ' at id : ', id(copylist1))                    #copylist1 :  ['wayne', 'paul', 25, ['manchester', 'uk']]  at id :  2200279796808

#changing 25 to 31 using demo_list, Both list will be affected
demo_list[2] = 31
print('demo_list : ', demo_list, ' at id : ', id(demo_list))                    #demo_list :  ['wayne', 'paul', 31, ['manchester', 'uk']]  at id :  2200279796808
print('copylist1 : ', copylist1, ' at id : ', id(copylist1))                    #copylist1 :  ['wayne', 'paul', 31, ['manchester', 'uk']]  at id :  2200279796808

#changing inner list ['manchester'] to ['arsenal'] using copylist1, Both list will be affected
copylist1[3][0] = 'arsenal'
print('demo_list : ', demo_list, ' at id : ', id(demo_list))                    #demo_list :  ['wayne', 'paul', 31, ['arsenal', 'uk']]  at id :  2200279796808
print('copylist1 : ', copylist1, ' at id : ', id(copylist1))                    #copylist1 :  ['wayne', 'paul', 31, ['arsenal', 'uk']]  at id :  2200279796808

#List Copying Method 2 - Shallow Copying
#Shallow copy is different than Assignment(=), becus it creates a new object. i.e. New copy of list is made
#So if you make changes to this new list, it won't affect other list
colors = ['red', 'green', [4, 16, 25]]

#You can achieve shallow copy using slice[:] or using copy module's copy() or listName.copy()
#Shallow Copy Method 1 : using list slicing[:]
colorcopy1 = colors[:]
print('colors : ', colors, ' at id : ', id(colors))                             #colors :  ['red', 'green', [4, 16, 25]]  at id :  2004701037832
print('colorcopy1 : ', colorcopy1, ' at id : ', id(colorcopy1))                 #colorcopy1 :  ['red', 'green', [4, 16, 25]]  at id :  2004702359752

#Both list are at different id's
colors.append(99)
colorcopy1[2][0] = 36
print('colors : ', colors, ' at id : ', id(colors))                             #colors :  ['red', 'green', [36, 16, 25], 99]  at id :  2004701037832
print('colorcopy1 : ', colorcopy1, ' at id : ', id(colorcopy1))                 #colorcopy1 :  ['red', 'green', [36, 16, 25]]  at id :  20047023597520

#Shallow copy has 1 problem with it. If the original list is a compound object (e.g. a list of lists), the elements in the new object are referenced to the original elements.
#Which is why it is called a shallow copy. So, if you modify the mutable elements like lists, the changes will be reflected on the original elements.
#Hence, changing 4 to 36 using colorcopy1, make changes in both the list
#Shallow copy Method 2 : Using copy()
colors = ['red', 'green', [4, 16, 25]]
colorcopy2 = colors.copy()
print('colors : ', colors)                                          #colors :  ['red', 'green', [4, 16, 25]]
print('colorcopy2 : ', colorcopy2)                                  #colorcopy2 :  ['red', 'green', [4, 16, 25]]

#2 different copies of list is created, changing 1 will not affect another
colors[0] = 'blue'
print('colors : ', colors)                                          #colors :  ['blue', 'green', [4, 16, 25]]
print('colorcopy2 : ', colorcopy2)                                  #colorcopy2 :  ['red', 'green', [4, 16, 25]]
#But again, if list contains another list, change in one list will affect other list also
#This will remove 25 from both the list
colors[2].pop()
print('colors : ', colors)                                          #colors :  ['blue', 'green', [4, 16]]
print('colorcopy2 : ', colorcopy2)                                  #colorcopy2 :  ['red', 'green', [4, 16]]

#Shallow copy Method 3 : using copy module's copy()
import copy
colors = ['red', 'green', [4, 16, 25]]
colorcopy3 = copy.copy(colors)
print('colors : ', colors)                                          #colors :  ['red', 'green', [4, 16, 25]]
print('colorcopy3 : ', colorcopy3)                                  #colorcopy3 :  ['red', 'green', [4, 16, 25]]

#Same problem arises here, if one list changes inner list data, other list will also be affected
colorcopy3[2][2] = 144
print('colors : ', colors)                                          #colors :  ['red', 'green', [4, 16, 144]]
print('colorcopy3 : ', colorcopy3)                                  #colorcopy3 :  ['red', 'green', [4, 16, 144]]

#Hence with shallow copy using slice[:], copy.copy(listName) or listName.copy(), if anyone item is list itself, no separate copies are created. Infact, that Inner list Reference is passed to both lists.
#Therefore, changes made into 1 inner list, will affect other inner list also

#Solution is - Deep Copying using copy.deepcopy(listName)
#The deep copy is different from shallow copy in that the copied elements have their own pointers and are not referenced to the original elements.
#Therefore, no matter how you modify the deep copy, the changes will NOT be reflected on the original list.
#Creating a deep copy is slower, because you are making new copies for everything.
colors = ['red', 'green', [4, 16, 25]]
deepcopycolor = copy.deepcopy(colors)
print('colors : ', colors)                                          #colors :  ['red', 'green', [4, 16, 25]]
print('deepcopycolor : ', deepcopycolor)                            #deepcopycolor :  ['red', 'green', [4, 16, 25]]

#Now with deepcopy() inner lists are also copied element by element
colors[2][0] = 36
print('colors : ', colors)                                          #colors :  ['red', 'green', [36, 16, 25]]
print('deepcopycolor : ', deepcopycolor)                            #deepcopycolor :  ['red', 'green', [4, 16, 25]]
