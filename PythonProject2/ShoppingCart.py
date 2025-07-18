"""
─────────────────────────────────────────────────────────────────────────────

    NB: IMPLEMENT THE LOGIC TO PRINT THE DISCOUNTED AND TAXED CART ON TERMINAL

─────────────────────────────────────────────────────────────────────────────

As discussed in today's class, this code showcases the concepts of OOP in Python.
Notice we have 3 classes in this code: one super class and two subclasses.

[Inheritance:]
    DiscountShoppingCart and TaxedShoppingCart classes inherit
    all methods and properties from the base class ShoppingCart.
    They don’t have to re-implement add_item, remove_item, or summary() methods.

[Polymorphism:]
    All 3 classes share the same interface (e.g., calculate_total(), summary()).

    This function --> checkout(cart: ShoppingCart), treats all carts as ShoppingCart instances.
    But each call to calculate_total() dispatches to the correct overridden method at runtime.

[Method Overriding:]
    The 2 subclasses override only the necessary behavior
    (e.g., applying a discount or tax), while using super().calculate_total()
    to reuse logic from the base class.
"""


class ShoppingCart:

    def __init__(self): #initilaize empty cart
        self.items = [] #a list of tuples

    def add_item(self, item_name: str, qty: int, unit_price: float):  #adds items to cart
        self.items.append((item_name, qty, unit_price))

    def remove_item(self, item_name: str): #removes an item by name
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break

    def calculate_total(self) -> float:  #adds up the total cost
        total = 0.0
        for name, qty, price in self.items:
            total += qty * price
        return total

    def cart_contents(self):
        print("Cart Contents: ")
        for name, qty, price in self.items:
            print(f"  {name}:- {qty} @ Ksh {price:.2f} each")
        print(f"Total: Ksh {self.calculate_total():.2f}\n")


# Subclass 1: applies a discount rate
class DicountedCart(ShoppingCart):
    def __init__(self, discount_rate: float):
        super().__init__()
        self.discount_rate = discount_rate  # e.g. 0.10 for 10%

    def calculate_total(self) -> float:
        initial_total = super().calculate_total()
        discount = initial_total * self.discount_rate
        return initial_total - discount


# Subclass 2: applies a sales tax
class TaxedCart(ShoppingCart):
    def __init__(self, tax_rate: float):
        super().__init__()
        self.tax_rate = tax_rate

    def calculate_total(self) -> float:
        initial_total = super().calculate_total()
        tax = initial_total * self.tax_rate
        return initial_total + tax


# A polymorphic function that works on any ShoppingCart subclass
def checkout(cart: ShoppingCart):
    cart.cart_contents()
    print(f"Total amount: Ksh {cart.calculate_total():.2f}\n")


# IMPLEMENTATION
if __name__ == "__main__":
    # 1) Instantiate an Ordinary Cart
    obj_cart = ShoppingCart()
    obj_cart.add_item("Papaya", 76, 6.20)
    obj_cart.add_item("Orange", 96, 11.50)
    obj_cart.add_item("Kiwi", 85, 9.60)
    print(">>> Ordinary Cart Without Tax & Discount <<<")
    checkout(obj_cart)

    # 2) Instantiate and Apply Discount
    disc_cart = DicountedCart(discount_rate=0.15)
    disc_cart.add_item("Papaya", 76, 6.20)
    disc_cart.add_item("Orange", 96, 11.50)
    disc_cart.add_item("Kiwi", 85, 9.60)
    print(">>> Applying a 15% Discount <<<")
    checkout(disc_cart)  # ✅ Discounted Cart printed here

    # 3) Instantiate and Apply Tax
    taxed_cart = TaxedCart(tax_rate=0.12)
    taxed_cart.add_item("Papaya", 5, 2.00)
    taxed_cart.add_item("Orange", 96, 11.50)
    taxed_cart.add_item("Kiwi", 3, 1.50)
    print(">>> Applying a 12% Tax <<<")
    checkout(taxed_cart)  # ✅ Taxed Cart printed here
