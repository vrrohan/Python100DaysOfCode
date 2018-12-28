#Tuple indexing is just like list - it starts with 0 from begining & -1 from end
names = ('john', 'paul', 'wayne', 'leo', 'jack')
print(names[:3])                    #('john', 'paul', 'wayne')
print(names[2:5])                   #('wayne', 'leo', 'jack')

newNames = names[0], names[3:]
print(newNames)                     #('john', ('leo', 'jack'))

#remember if tuple has single value, use a trailing comma
# x = (40) is a integer
# x = (40,) is a tuple
# x = 50, is also a tuple

#print tuple in reverse order
print(names[:])                     #('john', 'paul', 'wayne', 'leo', 'jack')
print(names[::-1])                  #('jack', 'leo', 'wayne', 'paul', 'john')
