from pyrecord import Record

class Checkout:

    def __init__(self, stock, threshold_discount=None):
        super()
        self._stock_by_id = {i.id: i for i in stock}
        self._threshold_discount = threshold_discount

    def total(self, items):
        return 0


CheckoutItem = Record.create_type(
    'CheckoutItem', 
    'id', 
    'label', 
    'cost', 
    'discount', 
    discount=None,
)

ItemDiscount = Record.create_type('ItemDiscount', 'items', 'rate')

ThresholdDiscount = Record.create_type('ThresholdDiscount', 'threshold', 'rate')