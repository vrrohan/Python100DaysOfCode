#sort() can be used to sort the list in both ascending and descending order.
list_of_city = ['Noida', 'Delhi', 'Bangalore', 'Lucknow', 'Mumbai', 'Gurgaon']
list_of_marks = [78, 89, 65, 92, 70, 56, 45, 82, 70]

print('cities before sort() : ', list_of_city)                      #cities before sort() :  ['Noida', 'Delhi', 'Bangalore', 'Lucknow', 'Mumbai', 'Gurgaon']
print('marks before sort() : ', list_of_marks)                      #marks before sort() :  [78, 89, 65, 92, 70, 56, 45, 82, 70]
list_of_city.sort()
list_of_marks.sort()
print('cities after sort() : ', list_of_city)                       #cities after sort() :  ['Bangalore', 'Delhi', 'Gurgaon', 'Lucknow', 'Mumbai', 'Noida']
print('marks after sort() : ', list_of_marks)                       #marks after sort() :  [45, 56, 65, 70, 70, 78, 82, 89, 92]

#To sort list in descending order, use - list_name.sort(reverse=True)
list_of_marks.sort(reverse=True)
print('marks in reverse order : ', list_of_marks)                   #marks in reverse order :  [92, 89, 82, 78, 70, 70, 65, 56, 45]

#To reverse a list use - listName.reverse()
list_of_marks = [78, 89, 65, 92, 70, 56, 45, 82, 70]
print('marks before erase : ', list_of_marks)                       #marks before erase :  [78, 89, 65, 92, 70, 56, 45, 82, 70]
list_of_marks.reverse()
print('marks after reverse : ', list_of_marks)                      #marks after reverse :  [70, 82, 45, 56, 70, 92, 65, 89, 78]
