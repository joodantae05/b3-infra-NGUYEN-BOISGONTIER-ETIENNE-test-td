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
        print(f"[apply_discount] Tentative d'application d'une remise de {discount_percentage}%")
    
        if discount_percentage < 0 or discount_percentage > 100:
            print(f"[apply_discount] Erreur : {discount_percentage}% n'est pas un pourcentage valide. Il doit être entre 0 et 100.")
            raise ValueError("Discount percentage must be between 0 and 100.")
    
        # Calcul du total brut
        self.base_total = sum(product.price * quantity for product, quantity in self.items.items())
        print(f"[apply_discount] Total brut calculé : {self.base_total}€")
    
        # Application de la remise
        self.discounted_total = self.base_total * (1 - discount_percentage / 100)
        print(f"[apply_discount] Remise appliquée : {self.base_total - self.discounted_total}€")
    
        return self.discounted_total
