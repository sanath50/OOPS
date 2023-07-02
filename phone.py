from item import Item

class Phone(Item):
    def __init__(self, name : str, price : float, quantity=0, broken_phone=0):
        #Call super function to inherit all attributes/methods
        super().__init__(
            name,price,quantity
        )
        #To avoid some unnecessary cases we use assert
        assert broken_phone>=0, f"Quantity = {broken_phone}, is not greater than zero!"

        self.broken_phone = broken_phone