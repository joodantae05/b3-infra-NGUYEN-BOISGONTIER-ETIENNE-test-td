from cart import Cart
from datetime import datetime, timedelta

class Order:
    def __init__(self, cart: Cart):
        if not cart.items:
            raise ValueError("Cart is empty. Cannot place an order.")
        self.items = cart.items
        self.total = cart.calculate_total()
        self.order_date = datetime.now()

    def place_order(self):
        for product, quantity in self.items.items():
            product.reduce_stock(quantity)
        return f"Order placed successfully! Total: {self.total:.2f}€"

    def view_order(self):
        return "\n".join([f"{product.name} x {quantity}" for product, quantity in self.items.items()]) + \
               f"\nTotal: {self.total:.2f}€"

    def get_delivery_date(self, delivery_days: int = 3):

        delivery_datetime = self.order_date + timedelta(days=delivery_days)
        return delivery_datetime.strftime("%Y-%m-%d %H:%M")
