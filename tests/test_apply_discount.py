import unittest
from product import Product
from cart import Cart

class TestCart(unittest.TestCase):

    def setUp(self):
        """Prépare un panier pour les tests"""
        self.cart = Cart()
        # Créez quelques produits pour tester
        laptop = Product("Laptop", 1200.0, 10)
        smartphone = Product("Smartphone", 800.0, 10)
        self.cart.add_product(laptop, 1)
        self.cart.add_product(smartphone, 2)
        print("\n[Setup] Création du panier avec des articles pour les tests.")

    def test_apply_discount_valid(self):
        """Tester apply_discount avec un pourcentage valide"""
        print("[Test] Test apply_discount avec un pourcentage valide...")
        discount_percentage = 10  # Réduction de 10%
        discounted_total = self.cart.apply_discount(discount_percentage)

        # Calcul du total brut avant remise
        expected_discounted_total = (self.cart.base_total * discount_percentage) / 100
        self.assertEqual(discounted_total, expected_discounted_total)
        print("[Test] apply_discount avec un pourcentage valide passé.")

    def test_apply_discount_invalid_negative(self):
        """Tester apply_discount avec un pourcentage de réduction invalide (négatif)"""
        print("[Test] Test apply_discount avec un pourcentage invalide (négatif)...")
        with self.assertRaises(ValueError) as context:
            self.cart.apply_discount(-5)
        self.assertEqual(str(context.exception), "Discount percentage must be between 0 and 100.")
        print("[Test] apply_discount avec un pourcentage invalide (négatif) passé.")

    def test_apply_discount_invalid_too_high(self):
        """Tester apply_discount avec un pourcentage de réduction invalide (trop élevé)"""
        print("[Test] Test apply_discount avec un pourcentage invalide (trop élevé)...")
        with self.assertRaises(ValueError) as context:
            self.cart.apply_discount(150)
        self.assertEqual(str(context.exception), "Discount percentage must be between 0 and 100.")
        print("[Test] apply_discount avec un pourcentage invalide (trop élevé) passé.")

    def test_apply_discount_zero(self):
        """Tester apply_discount avec un pourcentage de réduction de 0%"""
        print("[Test] Test apply_discount avec un pourcentage de réduction de 0%...")
        discount_percentage = 0
        discounted_total = self.cart.apply_discount(discount_percentage)

        # Vérifier que le total est inchangé à 0% de réduction
        self.assertEqual(discounted_total, self.cart.base_total)
        print("[Test] apply_discount avec un pourcentage de réduction de 0% passé.")

    def test_apply_discount_when_empty(self):
        """Tester apply_discount quand le panier est vide"""
        print("[Test] Test apply_discount quand le panier est vide...")
        empty_cart = Cart()  # Créer un panier vide
        discounted_total = empty_cart.apply_discount(10)  # Appliquer une remise
        self.assertEqual(discounted_total, 0)  # Le total doit être 0 pour un panier vide
        print("[Test] apply_discount quand le panier est vide passé.")

if __name__ == "__main__":
    unittest.main(buffer=False)  # Désactive le buffering pour afficher les prints
