import csv


class Item:
    pay_rate = 0.8
    all = []
    def __init__(self, name : str, price : float, quantity : int):
        #To avoid some unnecessary cases we use assert
        assert price>=0, f"Price = {price}, is not greater than zero!"
        assert quantity>=0, f"Quantity = {quantity}, is not greater than zero!"
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)
    def calculate_total_price(self):
        return self.price*self.quantity
    def apply_discount(self):
        return self.price*self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity'))
            )
    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"

Item.instantiate_from_csv()

item1 = Item('Phone',1234,3)
item2 = Item('Laptop', 1888, 4)
item3 = Item('Cable',1992,3)
item4 = Item('Mouse', 1888, 4)
item5 = Item('Keyboard', 1888, 4)
print(Item.all)