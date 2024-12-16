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
        """Calcule le total brut du panier sans appliquer de remise"""
        total = sum(product.price * quantity for product, quantity in self.items.items())
        return total
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
        
        # Calcul du total brut avant remise
        total = self.calculate_total()  # Utilisez la méthode calculate_total() pour obtenir le total
        print(f"[apply_discount] Total brut calculé : {total}€")
        
        # Application de la remise
        discount_amount = (total * discount_percentage) / 100  # Calcul de la remise
        discounted_total = total - discount_amount  # Appliquer la remise
        
        print(f"[apply_discount] Remise appliquée : {discount_amount}€, Total après remise : {discounted_total}€")
        
        return discounted_total
    def checkout(self):
        """Processus de validation du panier pour la page de paiement"""
        if not self.items:
            raise ValueError("Your cart is empty. You must add items to the cart to proceed.")
        
        print("--------- Checkout Summary ---------")
        print("Product Details:")
        
        # Affichage des produits dans le panier
        for product, quantity in self.items.items():
            print(f"{product.name} x {quantity} - {product.price * quantity}€")

        # Calcul de la remise
        discount_amount = self.base_total * self.discount
        print(f"Discount applied: {discount_amount:.2f}€")

        # Calcul des frais de livraison (si applicable)
        total_with_shipping = self.calculate_total() + self.shipping_fee
        print(f"Shipping Fee: {self.shipping_fee:.2f}€")

        # Affichage du total
        total_final = total_with_shipping
        print(f"Total to pay (including shipping): {total_final:.2f}€")
        
        print("------------------------------------")
        print("Proceed to payment...")

        return total_final

