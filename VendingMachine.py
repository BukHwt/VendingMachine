from classes.Candy import Candy
from classes.Chips import Chips
from classes.Cola import Cola

class VendingMachine():
    
    def __init__(self, product_inventory ={'Cola':0, 'Chips':0, 'Candy':0}, coin_inventory = {'Nickel':0, 'Dime':0, 'Quarter':0}) -> None:
        self.product_inventory = product_inventory
        self.coin_inventory = coin_inventory
    
    def stock_product(self, product)->None:
        if type(product) == Cola:
            self.product_inventory['Cola']+=1
        elif type(product) == Chips:
            self.product_inventory['Chips']+=1
        elif type(product) == Candy:
            self.product_inventory['Candy']+=1
        else:
            print("MACHINE WILL NOT ACCEPT THIS ITEM")
    
    def stock_coin(Coin)->None:
        pass
    
a = VendingMachine()

b = Cola()

a.stock_product(b)

print(a.product_inventory)