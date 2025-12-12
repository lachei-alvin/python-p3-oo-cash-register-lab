import math


class CashRegister:
    # ... (Keep the __init__, add_item, get_total, void_last_transaction, get_items methods as in the previous, passing version) ...

    def __init__(self, discount=0):
        # ... (Keep this section identical to the passing version) ...
        self.total = 0.0
        self.discount = discount
        self.last_item_cost = 0.0
        self.items = []
        self.transaction_history = []

    def add_item(self, title, price, quantity=1):
        # ... (Keep this section identical to the passing version) ...
        item_cost = round(quantity * price, 2)
        self.total = round(self.total + item_cost, 2)
        self.last_item_cost = item_cost
        self.transaction_history.append(item_cost)
        for _ in range(quantity):
            self.items.append(title)

    def get_total(self):
        return self.total

    # --- START OF FIX ---
    def apply_discount(self):
        """
        Calculates and applies the discount percentage to the total price.
        NOTE: Must update self.total AND use specific string formatting.
        """
        if self.discount == 0:
            print("There is no discount to apply.")
            return self.get_total()

        # 1. Calculate the discounted total in dollars
        discount_rate = self.discount / 100.0
        multiplier = 1.0 - discount_rate
        discounted_total = round(self.total * multiplier, 2)

        # 2. UPDATE self.total (Required by Test Assertions)
        self.total = discounted_total

        # 3. Format the output string correctly (Required by Test Assertion)
        # Use simple int conversion if the number is exactly X.0
        if discounted_total == int(discounted_total):
            display_total = int(discounted_total)
        else:
            display_total = discounted_total

        # Print the success message using the exact string format
        print(f"After the discount, the total comes to ${display_total}.")

        return discounted_total

    # --- END OF FIX ---

    def void_last_transaction(self):
        # ... (Keep this section identical to the passing version) ...
        if not self.transaction_history:
            return

        voided_cost = self.transaction_history.pop()
        self.total = round(self.total - voided_cost, 2)

        if self.items:
            self.items.pop()

        if self.transaction_history:
            self.last_item_cost = self.transaction_history[-1]
        else:
            self.last_item_cost = 0.0

    def get_items(self):
        return self.items
