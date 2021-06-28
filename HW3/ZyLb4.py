# Itzel Munoz Monroy PSID: 1888446
class ShoppingCart:
    def __init__(self, name="none", date="January 1, 2016"):
        self.customer_name = name
        self.current_date = date
        self.cart_items = []
        self.item_purchase = self.ItemToPurchase()

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, label):
        if label in self.cart_items:
            self.cart_items.pop(label)
        else:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_purchase, new_quantity):
        if item_purchase in self.cart_items:
            self.item_purchase.item_quantity = new_quantity
        else:
            print("Item not found in cart. Nothing removed.")

    def get_num_items_in_cart(self):
        total_count = 0
        if not self.cart_items:
            return total_count
        else:
            for item in self.cart_items:
                total_count += self.item_purchase.count_quantity(item)
            return total_count

    def get_cost_of_cart(self):
        total = 0
        for item in self.cart_items:
            total += item
        return total

    def print_cost(self):
        for item in self.cart_items:
            self.item_purchase.print_item_cost(item)

    def print_total(self):
        if not self.cart_items:
            print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
            print("Number of Items:", self.get_num_items_in_cart())
            print("")
            print("SHOPPING CART IS EMPTY")
            print("")
            print("Total: ${:.0f}".format(self.get_cost_of_cart()))
        else:
            print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
            print("Number of Items:", self.get_num_items_in_cart())
            print("")
            self.print_cost()
            print("")
            print("Total: ${:.0f}".format(self.get_cost_of_cart()))

    def print_descriptions(self):
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        print("")
        print("Item Descriptions")
        for item in self.cart_items:
            self.item_purchase.print_item_description(item)

    class ItemToPurchase:
        def __init__(self):
            self.item_name = "none"
            self.item_price = 0
            self.item_quantity = 0
            self.item_description = "none"

        def print_item_cost(self, label):
            if not label:
                print(self.item_name, self.item_quantity,
                      "@ ${:.0f} = ${:.0f}".format(self.item_price, self.item_price * self.item_quantity))
            else:
                print(label.item_name, label.item_quantity,
                      "@ ${:.0f} = ${:.0f}".format(label.item_price, label.item_price * label.item_quantity))

        def count_quantity(self, label):
            if not label:
                count = self.item_quantity
                return count
            else:
                count = label.item_quantity
                return count

        def __add__(self, other):
            total = (self.item_price * self.item_quantity) + other
            return total

        def __radd__(self, other):
            if other == 0:
                return self
            else:
                return self.__add__(other)

        def print_item_description(self, label):
            if not label:
                print("{}: {}".format(self.item_name, self.item_description))
            else:
                print("{}: {}".format(label.item_name, label.item_description))


def print_menu(cart):
    # cart = ShoppingCart()
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")
    print("")
    commands = ["a", "r", "c", "i", "o"]
    command = ""
    position_items = []
    prices = []
    descriptions = []
    while command != "q":
        command = input("Choose an option:")
        print("")
        if command == "a":
            print("ADD ITEM TO CART")
            item = ShoppingCart().ItemToPurchase()
            item.item_name = input("Enter the item name:\n")
            item.item_description = input("Enter the item description:\n")
            item.item_price = float(input("Enter the item price:\n"))
            item.item_quantity = int(input("Enter the item quantity:\n"))
            cart.add_item(item)
            prices.append(item.item_price)
            descriptions.append(item.item_description)
            position_items.append(item.item_name)

        elif command == "r":
            print("REMOVE ITEM FROM CART")
            name = input("Enter name of item to remove:\n")
            if name in position_items:
                index = position_items.index(name)
                cart.cart_items.pop(index)
                prices.pop(index)
                descriptions.pop(index)
                position_items.remove(name)
            else:
                print("Item not found in cart. Nothing removed.")

        elif command == "c":
            print("CHANGE ITEM QUANTITY")
            item2 = ShoppingCart().ItemToPurchase()
            name1 = input("Enter the item name:\n")
            quantity = int(input("Enter the new quantity:\n"))
            if name1 in position_items:
                index = position_items.index(name1)
                cart.cart_items.pop(index)
                item2.item_name = name1
                item2.item_quantity = quantity
                item2.item_price = prices[index]
                item2.item_description = descriptions[index]
                cart.cart_items.insert(index, item2)
            else:
                print("Item not found in cart. Nothing modified.")

        elif command == "i":
            print("OUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()

        elif command == "o":
            print("OUTPUT SHOPPING CART")
            cart.print_total()

        if command in commands:
            print("")
            print("MENU")
            print("a - Add item to cart")
            print("r - Remove item from cart")
            print("c - Change item quantity")
            print("i - Output items' descriptions")
            print("o - Output shopping cart")
            print("q - Quit")
            print("")


if __name__ == "__main__":
    buy = ShoppingCart()
    buy.customer_name = input("Enter customer's name:\n")
    buy.current_date = input("Enter today's date:\n")
    print("")
    print("Customer name:", buy.customer_name)
    print("Today's date:", buy.current_date)
    print("")
    print_menu(buy)
