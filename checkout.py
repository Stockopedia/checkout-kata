from collections import Counter

from pyrecord import Record

class Checkout:

    def __init__(self, stock, threshold_discount=None):
        super()
        self._stock_by_id = {i.id: i for i in stock}
        self._threshold_discount = threshold_discount

    def total(self, items):
        total_cost = 0

        items_counter = Counter(items)
        for item_id, count in items_counter.items():
            total_cost += self._total_item(item_id, count)
        
        return total_cost
    
    def _total_item(self, item_id, count):
        item = self._stock_by_id[item_id]
        if item.discount:
            discounts_qualified, items_unqualified_for_discount = divmod(count, item.discount.items)
            items_qualified_for_discount = item.discount.items * discounts_qualified
            discounted_item_cost = item.cost * (100 - item.discount.rate) / 100.0
            total_item_cost = item.cost * items_unqualified_for_discount + discounted_item_cost * items_qualified_for_discount
        else:
            total_item_cost = item.cost * count
        
        return total_item_cost


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