import unittest
from cart import Cart
from product import Product  # Assurez-vous que la classe Product est correctement importée

class TestCartCheckout(unittest.TestCase):

    def setUp(self):
        """Prépare un panier avec des produits pour les tests"""
        self.cart = Cart()
        
        # Création des produits pour les tests
        self.laptop = Product("Laptop", 100.0, 10)  # Un produit à 100€
        self.smartphone = Product("Smartphone", 200.0, 5)  # Un produit à 200€
        
        # Ajouter des produits au panier
        self.cart.add_product(self.laptop, 2)  # Ajouter 2 laptops
        self.cart.add_product(self.smartphone, 1)  # Ajouter 1 smartphone
        print("\n[Setup] Création du panier avec des produits pour les tests.")

    def test_checkout_summary(self):
        """Tester le récapitulatif de commande lors du checkout"""
        print("[Test] Test checkout avec des produits dans le panier...")
        
        # Appliquer une remise de 10%
        self.cart.apply_discount(10)

        # Calculer le total attendu sans remise
        expected_total = (self.laptop.price * 2 + self.smartphone.price * 1)
        expected_discount = expected_total * 0.10  # Remise de 10%
        expected_shipping_fee = 5.0  # Frais de livraison hypothétiques (ajustez selon votre logique)
        expected_final_total = (expected_total - expected_discount) + expected_shipping_fee  # Total final après remise et frais

        # Appeler la méthode checkout
        final_total = self.cart.checkout()  # Processus de checkout
        
        # Vérifier que le total final correspond au total attendu
        self.assertEqual(final_total, expected_final_total)
        print(f"[Test] Checkout avec des produits passé. Total à payer : {final_total}€")

    def test_checkout_empty_cart(self):
        """Tester le checkout avec un panier vide"""
        print("[Test] Test checkout avec un panier vide...")
        
        # Créer un panier vide
        empty_cart = Cart()
        
        # Tenter de procéder au checkout avec un panier vide
        with self.assertRaises(ValueError) as context:
            empty_cart.checkout()  # Le checkout ne devrait pas fonctionner
        
        # Vérifier que l'exception a bien été levée et que le message d'erreur est correct
        self.assertEqual(str(context.exception), "Your cart is empty. You must add items to the cart to proceed.")
        print("[Test] Checkout avec un panier vide passé.")

    def test_checkout_without_discount(self):
        """Tester le checkout sans appliquer de remise"""
        print("[Test] Test checkout sans remise...")
        
        # Calculer le total attendu sans remise
        expected_total = (self.laptop.price * 2 + self.smartphone.price * 1)
        expected_shipping_fee = 5.0  # Frais de livraison hypothétiques (ajustez selon votre logique)
        expected_final_total = expected_total + expected_shipping_fee  # Total sans remise, mais avec frais de livraison
        
        # Appeler la méthode checkout sans appliquer de remise
        final_total = self.cart.checkout()  # Processus de checkout
        
        # Vérifier que le total final correspond au total attendu
        self.assertEqual(final_total, expected_final_total)
        print(f"[Test] Checkout sans remise passé. Total à payer : {final_total}€")

if __name__ == "__main__":
    unittest.main(buffer=False)  # Désactive le buffering pour afficher les prints
