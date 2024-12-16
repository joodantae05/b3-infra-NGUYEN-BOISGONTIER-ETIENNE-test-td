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

    def apply_discount(self):
        # Calcul de la remise : par exemple, 10% de remise si l'utilisateur a plus de 5 articles dans le panier
        total_items = sum(self.items.values())
        if total_items >= 5:  # Remise si 5 articles ou plus
            self.discount = 0.10  # 10% de remise
        elif total_items >= 3:  # Remise si 3 à 4 articles
            self.discount = 0.05  # 5% de remise
        else:
            self.discount = 0  # Pas de remise
        print(f"Discount applied: {self.discount * 100}%")

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


    def checkout(self):
        """Affiche le récapitulatif de la commande avant le paiement"""
        if not self.items:
            return "Your cart is empty. Please add items to your cart before proceeding to checkout."
        self.apply_discount()  # Applique la remise avant le calcul du total
        total = self.calculate_total()
        return f"Proceeding to checkout...\n{self.display_cart()}\nTotal to pay: {total:.2f}€"

