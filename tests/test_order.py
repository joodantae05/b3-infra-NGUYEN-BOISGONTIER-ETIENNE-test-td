import unittest
from datetime import datetime, timedelta
from product import Product
from cart import Cart
from order import Order

class TestOrder(unittest.TestCase):

    def setUp(self):
        """Setup a product and cart for testing."""
        # Create products
        self.product1 = Product(name="Laptop", price=1200.0, stock=5)
        self.product2 = Product(name="Headphones", price=150.0, stock=20)
        
        # Initialize the cart and add products
        self.cart = Cart()
        self.cart.add_product(self.product1, 1)  # Add 1 Laptop
        self.cart.add_product(self.product2, 2)  # Add 2 Headphones
        print("[Setup] Created products and added to cart.")

    def test_order_delivery_date(self):
        """Test the delivery date calculation."""
        # Place an order
        order = Order(self.cart)
        
        # Get the expected delivery date (5 days from now)
        delivery_date = order.get_delivery_date(5)  # Set delivery in 5 days
        print(f"[Test] Expected delivery date: {delivery_date}")
        
        # Calculate the expected delivery date manually
        expected_delivery = (datetime.now() + timedelta(days=5)).strftime("%Y-%m-%d %H:%M")
        
        # Assert that the calculated delivery date matches the expected one
        self.assertEqual(delivery_date, expected_delivery)

if __name__ == "__main__":
    unittest.main(buffer=False)  # Disable buffering to display prints
