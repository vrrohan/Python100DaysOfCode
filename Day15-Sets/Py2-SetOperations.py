#Set collection type also supports set operations like union, intersection, disjoint, subset etc
employees = {'bob', 'sue', 'ann', 'alice'}
managers = {'alex', 'sue'}

#union() or | i.e. It returns all elements that are present in either sets
print(employees.union(managers))                                                #{'bob', 'ann', 'alex', 'sue', 'alice'}

#or we can either use employees | managers
print(employees | managers)                                                     #{'bob', 'ann', 'alex', 'sue', 'alice'}

#intersection() or & i.e. it returns all elements that are in both sets
#x.intersection(y) or x&y - only sue is present in both sets
print(employees.intersection(managers))                                         #{'sue'}
print(employees & managers)                                                     #{'sue'}

#isdisjoint() - returns True, if two sets have null intersection i.e. no elements in common
print(employees.isdisjoint(managers))                                           #False

set1 = {'a', 'b', 'c'}
set2 = {'d', 'e'}
print(set1.isdisjoint(set2))                                                    #True

#issubset() or <= , returns True if x is subset of y
#x.issubset(y) or x<=y , here <= means (subset of) so, x <= y means Is x (subset of) y ?
print(managers.issubset(employees))                                             #False

set1 = {'a', 'b', 'c', 'd', 'e'}
set2 = {'c', 'e'}
print(set1.issubset(set2))                                                      #False
print(set2.issubset(set1))                                                      #True

#issuperset() or >= , returns True if x is superset of y
#x.issuperset(y) or x>=y, means if x is superset of y ? , >= means superset of ==> x>=y means Is x (superset of) y ?
print(managers.issuperset(employees))                                           #False

set1 = {'a', 'e', 'i', 'o', 'u'}
set2 = {'a', 'e', 'u'}
print(set1.issuperset(set2))                                                    #True
print(set1>=set2)                                                               #True

#< means proper subset i.e. x<y means if x is proper subset of y [A set can never be proper subset of itself]
#> means proper superset i.e. x>y means if x is proper superset of y
#This means - are all managers employees ?
print(managers < employees)                                                     #False
#Are both sue & alice are employees
print({'sue', 'alice'} < employees)                                             #True

#Are all managers employees ?
print(employees > managers)                                                     #False

#difference() - returns a difference of two or more sets
#use difference() or x-y
x = {'a', 'e', 'i', 'o', 'u'}
y = {'e', 'o'}
print(x.difference(y))                                                          #{'a', 'u', 'i'}
print(x-y)                                                                      #{'a', 'u', 'i'}
print(employees - managers)                                                     #{'ann', 'bob', 'alice'}

#difference_update() - removes all elements of one set from another set
#x.difference_update(y) - means , x=x-y
print(x)                                                                        #{'u', 'a', 'i', 'e', 'o'}
x.difference_update(y)
print(x)                                                                        #{'u', 'a', 'i'}

employees = {'bob', 'sue', 'ann', 'alice'}
managers = {'alex', 'sue'}
#employees which are not managers
print(employees - managers)                                                     #{'bob', 'ann', 'alice'}
#managers which are not employees
print(managers - employees)                                                     #{'alex'}

#^ - means present in any one set, but not both
employees = {'bob', 'sue', 'ann', 'alice'}
managers = {'alex', 'sue', 'alice'}
print(managers ^ employees)                                                     #{'bob', 'ann', 'alex'}
