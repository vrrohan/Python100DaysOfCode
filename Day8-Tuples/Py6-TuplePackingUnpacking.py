#Tuples packing
#All 4 values are packed into t
t = ('foo', 'bar', 'alice', 'joe')
print(t)                                    #('foo', 'bar', 'alice', 'joe')

#Tuples unpacking
(s1, s2, s3, s4) = t
print(s1)                                   #foo
print(s3)                                   #alice

#when unpacking, number of variables on left must match number of variables on right tuple
t = 1,2,3
print(t)                                    #(1, 2, 3)
a,b,c = t
print(c)                                    #3

#Using advantage of tuple packing & unpacking, we can swap values of 2 variables in a single line
admin = 'john'
user = 'usernormal'
admin, user = user, admin
print('admin : ', admin)                    #admin :  usernormal
print('user : ', user)                      #user :  john
