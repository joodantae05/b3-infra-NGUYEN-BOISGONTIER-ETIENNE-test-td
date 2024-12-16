from product import Product

class Cart:
    def __init__(self):
        self.items = {}  # {product: quantity}
        self.discounted_total = 0  # Total après application de la réduction
        self.base_total = 0        # Total avant réduction

    def add_product(self, product: Product, quantity: int):
        if product.stock < quantity:
            raise ValueError(f"Cannot add {quantity} of {product.name}. Only {product.stock} left.")
        self.items[product] = self.items.get(product, 0) + quantity

    def remove_product(self, product: Product):
        if product in self.items:
            del self.items[product]
        else:
            raise KeyError(f"{product.name} is not in the cart.")

    def calculate_total(self):
        """Calcule le total brut sans réduction."""
        self.base_total = sum(product.price * quantity for product, quantity in self.items.items())
        return self.base_total

    def apply_discount(self, discount_percentage: float):
        """Applique une réduction et calcule le total réduit."""
        if discount_percentage < 0 or discount_percentage > 100:
            raise ValueError("Discount percentage must be between 0 and 100.")
        self.calculate_total()  # Assure le calcul du total brut avant la réduction
        self.discounted_total = (self.base_total * discount_percentage) / 100
        return self.discounted_total
