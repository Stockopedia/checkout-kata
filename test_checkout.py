from nose.tools import eq_
from checkout import Checkout, CheckoutItem, ItemDiscount, ThresholdDiscount

STUB_ITEM_NO_DISCOUNT = CheckoutItem('tomatoes', 'Tomatoes', 10)

STUB_ITEM_PERCENT_DISCOUNT = CheckoutItem(
    'batteries', 
    'Batteries', 
    20, 
    ItemDiscount(2, 10),
)


class TestCheckout:

    def test_simple_total(self):
        checkout = Checkout((STUB_ITEM_NO_DISCOUNT, ))
        eq_(20, checkout.total((STUB_ITEM_NO_DISCOUNT.id, STUB_ITEM_NO_DISCOUNT.id)))
    
    def test_empty(self):
        checkout = Checkout((STUB_ITEM_NO_DISCOUNT, ))
        eq_(0, checkout.total([]))
    
    def test_percentage_discount_not_qualifed(self):
        checkout = Checkout((STUB_ITEM_PERCENT_DISCOUNT, ))
        eq_(20, checkout.total((STUB_ITEM_PERCENT_DISCOUNT.id, )))

    def test_percentage_discount_qualified(self):
        checkout = Checkout((STUB_ITEM_PERCENT_DISCOUNT, ))
        discounted_item_id = STUB_ITEM_PERCENT_DISCOUNT.id
        eq_(36, checkout.total((discounted_item_id, discounted_item_id)))
    
    def test_percentage_discount_additional(self):
        checkout = Checkout((STUB_ITEM_PERCENT_DISCOUNT, ))
        discounted_item_id = STUB_ITEM_PERCENT_DISCOUNT.id
        eq_(56, checkout.total((discounted_item_id, discounted_item_id, discounted_item_id)))
    
    def test_percentage_discount_multiple_exact(self):
        checkout = Checkout((STUB_ITEM_PERCENT_DISCOUNT, ))
        discounted_item_id = STUB_ITEM_PERCENT_DISCOUNT.id
        eq_(72, checkout.total((discounted_item_id, discounted_item_id, discounted_item_id, discounted_item_id)))
    
    def test_percentage_discount_multiple_additional(self):
        checkout = Checkout((STUB_ITEM_PERCENT_DISCOUNT, ))
        discounted_item_id = STUB_ITEM_PERCENT_DISCOUNT.id
        eq_(92, checkout.total((discounted_item_id, discounted_item_id, discounted_item_id, discounted_item_id, discounted_item_id)))
    
    def test_threshold_save_below_threshold(self):
        threshold_discount = ThresholdDiscount(11, 10)
        checkout = Checkout((STUB_ITEM_NO_DISCOUNT, ), threshold_discount)
        eq_(10, checkout.total((STUB_ITEM_NO_DISCOUNT.id, )))
    
    def test_threshold_save_at_threshold(self):
        threshold_discount = ThresholdDiscount(10, 10)
        checkout = Checkout((STUB_ITEM_NO_DISCOUNT, ), threshold_discount)
        eq_(9, checkout.total((STUB_ITEM_NO_DISCOUNT.id, )))

    def test_threshold_save_above_threshold(self):
        threshold_discount = ThresholdDiscount(10, 10)
        checkout = Checkout((STUB_ITEM_NO_DISCOUNT, ), threshold_discount)
        eq_(18, checkout.total((STUB_ITEM_NO_DISCOUNT.id, STUB_ITEM_NO_DISCOUNT.id)))

    def test_other_discount_disqualifies(self):
        threshold_discount = ThresholdDiscount(40, 10)
        checkout = Checkout((STUB_ITEM_PERCENT_DISCOUNT, ), threshold_discount)
        discounted_item_id = STUB_ITEM_PERCENT_DISCOUNT.id
        eq_(36, checkout.total((discounted_item_id, discounted_item_id)))
