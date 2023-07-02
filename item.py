import csv


class Item:
    pay_rate = 0.8
    all = []
    def __init__(self, name : str, price : float, quantity=0):
        #To avoid some unnecessary cases we use assert
        assert price>=0, f"Price = {price}, is not greater than zero!"
        assert quantity>=0, f"Quantity = {quantity}, is not greater than zero!"
        self.__name = name #Private attribute
        self.__price = price
        self.quantity = quantity

        Item.all.append(self)
    def calculate_total_price(self):
        return self.__price * self.quantity

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self,increment_value):
        self.__price = self.__price + self.price*increment_value
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
        return f"{self.__class__.__name__}('{self.name}',{self.__price},{self.quantity})"

    @property # Getter, gets read only value of the attribute
    def name(self): # Item.name() will bring the call here to name function and not name attribute
        #and the property will send only read only attribute to the above constructor function
        return self.__name #private attribute

    @name.setter # Setter. Set value ovverruling getter, so when setting value operation is performed, the name function here
    #is excecuted for item1.name, name is not the attribute in constructor
    def name(self,value):
        if len(value) > 10:
            raise Exception("The name is too long!!")
        self.__name = value
    #Abstraction#
    def send_email(self):
        self.__SMTP_connection('')
        self.__Body()
        self.__send()
    def __SMTP_connection(self,smtp_server):
        pass
    def __Body(self):
        return f"""
        Hello, WTH
"""
    def __send(self):
        pass