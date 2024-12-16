from product import Product

class Cart:
    def __init__(self):
        self.items = {}  # {product: quantity}
        self.discount = 0  # Pour stocker le montant de la remise appliquée

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
        total = sum(product.price * quantity for product, quantity in self.items.items())
        total_after_discount = total - (total * self.discount)
        return total_after_discount
    def display_cart(self):
        if not self.items:
            return "Your cart is empty."
        cart_display = "\n".join([f"{product.name} x {quantity} - {product.price * quantity}€"
                                  for product, quantity in self.items.items()])
        total = self.calculate_total()
        return f"{cart_display}\nTotal (after discount): {total:.2f}€"
    def clear_cart(self):
        """Supprime tous les articles du panier"""
        if not hasattr(self, 'items') or not isinstance(self.items, (list, dict)):
            print("Erreur : Le panier n'existe pas ou n'est pas correctement défini.")
            return
        if len(self.items) == 0:
            print("Votre panier est déjà vide.")
        else:
            self.items.clear()
            print("Votre panier a été vidé.")
    def apply_discount(self, discount_percentage: float):
        """Applique une réduction et calcule le total réduit."""
        if discount_percentage < 0 or discount_percentage > 100:
            raise ValueError("Discount percentage must be between 0 and 100.")
        self.calculate_total()  # Assure le calcul du total brut avant la réduction
        self.discounted_total = (self.base_total * discount_percentage) / 100
        return self.discounted_total

