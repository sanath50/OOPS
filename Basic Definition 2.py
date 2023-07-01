class Item:
    def __init__(self, name : str, price : float, quantity : int):
        #To avoid some unnecessary cases we use assert
        assert price>=0, f"Price = {price}, is not greater than zero!"
        assert quantity>=0, f"Quantity = {quantity}, is not greater than zero!"
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total_price(self):
        return self.price*self.quantity

item1 = Item('Phone',-1,3)
item2 = Item('Laptop', 1888, 4)

print(item1.calculate_total_price())