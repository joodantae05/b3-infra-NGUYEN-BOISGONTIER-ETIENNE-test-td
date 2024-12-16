import unittest
from cart import Cart

class TestCart(unittest.TestCase):

    def setUp(self):
        """Prépare un panier pour les tests"""
        self.cart = Cart()
        print("\n[Setup] Création d'un panier pour les tests.")

    def test_clear_cart_when_empty(self):
        """Tester clear_cart quand le panier est vide"""
        print("[Test] Test clear_cart quand le panier est vide...")
        self.cart.clear_cart()  # Le panier est vide au départ
        self.assertEqual(len(self.cart.items), 0)  # Le panier doit être vide
        print("[Test] Test clear_cart quand le panier est vide passé.")

    def test_clear_cart_when_not_empty(self):
        """Tester clear_cart quand il y a des articles dans le panier"""
        print("[Test] Test clear_cart quand le panier contient des articles...")
        self.cart.items.append("Laptop")
        self.cart.items.append("Smartphone")
        self.cart.clear_cart()  # Le panier contient des articles
        self.assertEqual(len(self.cart.items), 0)  # Le panier doit être vidé
        print("[Test] Test clear_cart quand le panier contient des articles passé.")

    def test_clear_cart_with_non_list_items(self):
        """Tester clear_cart avec une structure non valide pour items"""
        print("[Test] Test clear_cart avec une structure non valide pour items...")
        self.cart.items = "Invalid type"  # Type incorrect
        self.cart.clear_cart()  # Devrait imprimer un message d'erreur
        print("[Test] Test clear_cart avec une structure non valide pour items passé.")

    def test_clear_cart_when_no_items_attribute(self):
        """Tester clear_cart quand il n'y a pas d'attribut items"""
        print("[Test] Test clear_cart sans attribut 'items'...")
        del self.cart.items  # Supprimer l'attribut 'items'
        self.cart.clear_cart()  # Devrait imprimer un message d'erreur
        print("[Test] Test clear_cart sans attribut 'items' passé.")

if __name__ == "__main__":
    unittest.main(buffer=False)  # Disable buffering pour afficher les prints
