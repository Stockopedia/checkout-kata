from pyrecord import Record

class Checkout:

    def __init__(self, stock):
        super()
        self._stock_by_id = {i.id: i for i in stock}

    def total(self, items):
        pass


CheckoutItem = Record.create_type('CheckoutItem', 'id', 'label', 'cost')