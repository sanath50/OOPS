class Item: # class is a template definition of the methods and variables in a particular kind of object.
    def calculate_total_price(self,x,y): #The functions defined in a class are called methods and outside they are called functions
        return x * y #The self is used as python sends the object itself as the first argument hence self is used to avoid any confusion

item1 = Item() #The item1 created is called a an object/instance, when an instance is created it gains access to the methods defined in the class
item1.name = 'Phone'
item1.price = 130
item1.quantity = 21
print(item1.calculate_total_price(item1.price,item1.quantity))


item2 = Item()
item2.name = 'Laptop'
item2.price = 13021
item2.quantity = 212
print(item2.calculate_total_price(item2.price,item2.quantity))