#Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type.
#Make a method called describe_restaurant() that prints these two pieces of information
#and a method called open_restaurant() that prints a message indicating that the restaurant is open.
#Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.
class Restaurant :
    def __init__(self, restaurant_name, cuisine_type) :
        """this method runs during initialization of Restaurant class and will set Restaurant name & type of cuisine it provides"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self) :
        """this method displays all information about the Restaurant and its cuisine"""
        print('Restaurant name is :', self.restaurant_name)
        print('This Restaurant serves cuisines like :', self.cuisine_type)

    def open_restaurant(self) :
        """this method helps displays whether Restaurant is open or not"""
        if 'chinese' in self.cuisine_type :
            print('Restaurant is currently closed')
        else :
            print('Restaurant is currently open')

restOne = Restaurant('Dominos Pizza', 'pizza')
restTwo = Restaurant('Asia Kitchen', 'chinese, thai')
restOne.describe_restaurant()
restOne.open_restaurant()

restTwo.describe_restaurant()
restTwo.open_restaurant()
