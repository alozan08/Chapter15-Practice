'''
    Given two integers as user inputs that represent the number of drinks to buy and the number of bottles
    to restock, create a VendingMachine object that performs the following operations:
        - Purchase input number of drinks
        - Restocks input number of bottles
        - Reports inventory
    A VendingMachine'ss initial inventory is 20 drinks.
    ex.
        input:
            5
            2
        output:
            Inventory: 17 bottles
'''


class VendingMachine:
    def __init__(self):
        self.bottles = 20

    def purchase(self, amount):
        self.bottles = self.bottles - amount

    def restock(self, amount):
        self.bottles = self.bottles + amount

    def get_inventory(self):
        return self.bottles

    def report(self):
        print(f'Inventory: {self.bottles} bottles')


if __name__ == "__main__":
    machine = VendingMachine()
    purchase = int(input())
    restock = int(input())

    machine.purchase(purchase)
    machine.restock(restock)
    machine.report()