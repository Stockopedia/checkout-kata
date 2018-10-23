from nose.tools import eq_
from checkout import Checkout, CheckoutItem, Discount

STUB_ITEM_NO_DISCOUNT = CheckoutItem('tomatoes', 'Tomatoes', 10)

STUB_ITEM_PERCENT_DISCOUNT = CheckoutItem(
    'batteries', 
    'Batteries', 
    20, 
    Discount(2, 10),
)

STUB_ITEM_FREE_ITEM = CheckoutItem(
    'ready-meal', 
    'Ready meal', 
    50, 
    Discount(3, 100),
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
    
    def test_free_item_below_threshhold(self):
        assert False, 'Implement test'

    def test_free_item_at_threshold(self):
        assert False, 'Implement test'
    
    def test_free_item_above_threshold(self):
        assert False, 'Implement test'
    
    def test_free_item_exact_multiple(self):
        assert False, 'Implement test'
    
    def test_free_item_multiple_additional(self):
        assert False, 'Implement test'
    
    def test_threshold_save_below_threshold(self):
        assert False, 'Implement test'
    
    def test_threshold_save_at_threshold(self):
        assert False, 'Implement test'

    def test_threshold_save_above_threshold(self):
        assert False, 'Implement test'

    def test_other_discount_disqualifies(self):
        assert False, 'Implement test'