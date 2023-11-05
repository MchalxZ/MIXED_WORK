class BillItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = round(price, 2)
        self.quantity = quantity
        self.tax_rate = 6

    def total_cost(self):
        subtotal = self.price * self.quantity
        tax = round(subtotal * (self.tax_rate / 100), 2)
        total = round(subtotal + tax, 2)
        return total

class BillCalculator:
    def __init__(self):
        self.items = []
        self.item_names = set()

    def add_item(self):
        name = input("Enter the item name: ")
        while not name[0].isalpha() or name in self.item_names:
            if not name[0].isalpha():
                print("Item name must start with an alphabet. Please try again.")
            else:
                print("Item name is already in use. Please enter a different name.")
            name = input("Enter the item name: ")

        self.item_names.add(name)

        price = float(input("Enter the price (RM): "))
        price = round(price, 2)
        quantity = int(input("Enter the quantity: "))
        item = BillItem(name, price, quantity)
        self.items.append(item)

    def calculate_item_total(self):
        return round(sum(item.total_cost() for item in self.items), 2)

    def calculate_sst(self):
        item_total = self.calculate_item_total()
        sst = round(item_total * (6 / 100), 2)
        return sst

    def calculate_total_cost(self):
        item_total = self.calculate_item_total()
        sst = self.calculate_sst()
        total_cost = round(item_total + sst, 2)
        return total_cost

    def generate_bill(self):
        print("\n---- Receipt ----")
        for item in self.items:
            print(f"{item.name} ({item.quantity} x RM{round(item.price, 2)} each):")
            print(f"  Subtotal: RM{round(item.price * item.quantity, 2)}")
            print(f"  Tax (SST 6%): RM{round(item.price * item.quantity * 0.06, 2)}")
            print(f"  Total: RM{item.total_cost()}")

        item_total = self.calculate_item_total()
        sst = self.calculate_sst()

        print(f"\nSubtotal: RM{item_total}")
        print(f"SST (6%): RM{sst}")
        print(f"Total: RM{item_total + sst}")
        print("\nThank you, have a nice day!")

def rate_stars():
    while True:
        stars = input("Rate your experience (1 to 5 stars): ")
        if stars.isdigit():
            stars = int(stars)
            if 1 <= stars <= 5:
                print(f"Thank you for your {stars} star rating!")
                break
            else:
                print("Invalid rating. Please enter a rating from 1 to 5.")
        else:
            print("Invalid input. Please enter a rating between 1 to 5.")

def main():
    print("Welcome to the Self-service payment machine!")

    bill_calculator = BillCalculator()

    while True:
        print("\nChoose category:")
        print("1 - Food")
        print("2 - Beverage")
        print("3 - Quit")
        category_choice = int(input("Enter your choice: "))

        if category_choice == 1:
            bill_calculator.add_item()
        elif category_choice == 2:
            bill_calculator.add_item()
        elif category_choice == 3:
            break
        else:
            print("Invalid choice. Please enter valid input.")

    bill_calculator.generate_bill()
    rate_stars()

if __name__ == "__main__":
    main()
