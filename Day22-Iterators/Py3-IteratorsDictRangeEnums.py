#Using iterators with dictionary
d = {'a':1, 'b':5, 'c':9}
for k in d :
    print(k, d[k])
"""
a 1
b 5
c 9
"""

I = iter(d)
print(next(I))                                                                  #a
print(next(I))                                                                  #b

#Using iterators with range()
