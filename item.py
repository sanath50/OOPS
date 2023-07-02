import csv


class Item:
    pay_rate = 0.8
    all = []
    def __init__(self, name : str, price : float, quantity=0):
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
    @staticmethod
    def is_integer(num):
        if isinstance(num,float):
            return num.is_integer()
        #is_integer function will not count a number as flot if there are only zeroes after the decimal
        elif isinstance(num,int):
            return True
        else:
            return False
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})"