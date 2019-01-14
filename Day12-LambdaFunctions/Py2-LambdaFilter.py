#You can filter elements of a list or dictionary using filter() and lambda function
#filter(function, list) takes 2 arguments one is functions that returns True if certain condition gets true, while 2nd argument is a list to process
li = [5, 12, 7, 97, 100, 60, 17]

#1st arguments is a lambda function that returns boolean True if condition x%2!=0 satisfies i.e. filters only odd elements from the list
oddlist = filter(lambda x : (x%2!=0), li)
print(oddlist)                                  #<filter object at 0x000001F51B7F8B38>
print(type(oddlist))                            #<class 'filter'>

#By default filter() returns iterable or filter object i.e. you cannot access elements of filter object with index nor you can use len()
#use list() to convert & get the result in list form
oddlist = list(filter( lambda x : (x%2!=0), li))
print(oddlist)                                  #[5, 7, 97, 17]

#Using filter to get list of strings having length > 10
names = ['manchester united', 'arsenal', 'liverpool', 'fc barcelona', 'real madrid', 'chelsea']
newNames = list(filter( lambda x : len(x)>=10, names))
print(newNames)                                 #['manchester united', 'fc barcelona', 'real madrid']

#Get list of palindrome strings only
#reversed(str) - reverses a string
li = ['maps', 'keek', 'geeg', 'spam', 'aaa', 'print', 'spinnips']
palin = list(filter( lambda x : x=="".join(reversed(x)), li))
print(palin)                                    #['keek', 'geeg', 'aaa', 'spinnips']
