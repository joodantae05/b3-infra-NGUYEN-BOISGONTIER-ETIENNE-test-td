from product import Product
from cart import Cart

def main():
    # Création des produits
    p1 = Product("Laptop", 1200.0, 5)
    p2 = Product("Headphones", 150.0, 20)
    p3 = Product("Mouse", 25.0, 50)

    # Initialisation du panier
    cart = Cart()

    try:
        # Ajout des produits au panier
        cart.add_product(p1, 1)
        cart.add_product(p2, 2)

        # Affichage du contenu du panier
        print("\nContenu du panier:")
        print(cart.display_cart())

        # Calcul du total avant réduction
        base_total = cart.calculate_total()
        print(f"\nPrix avant réduction : {base_total:.2f}€")

        # Application d'une réduction de 20%
        discounted_total = cart.apply_discount(30)
        print(f"Prix de la réduction : {discounted_total:.2f}€")
        print(f"Montant après la réduction (30%): {(base_total - discounted_total):.2f}€")
        

    except ValueError as e:
        print(f"Erreur : {e}")

    # Exemple de vidage du panier

if __name__ == "__main__":
    main()
