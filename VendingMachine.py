from classes.Candy import Candy
from classes.Chips import Chips
from classes.Coin import Coin
from classes.Cola import Cola
from classes.Penny import Penny
from classes.Product import Product

class VendingMachine():
    
    def __init__(self, product_inventory ={'Cola':0, 'Chips':0, 'Candy':0}, coin_inventory = {'Nickel':0, 'Dime':0, 'Quarter':0}) -> None:
        self.product_inventory = product_inventory
        self.coin_inventory = coin_inventory
    
    def stock_product(self, product : Product)->None:
        if type(product) == Cola:
            self.product_inventory['Cola']+=1
        elif type(product) == Chips:
            self.product_inventory['Chips']+=1
        elif type(product) == Candy:
            self.product_inventory['Candy']+=1
        else:
            print("MACHINE WILL NOT ACCEPT THIS ITEM")
    
    def stock_coin(self, coin : Coin)->None:
        if coin.size and coin.weight == 1:
            self.coin_inventory['Dime']+=1
        elif coin.size and coin.weight == 2:
            self.coin_inventory['Nickel']+=1
        if coin.size and coin.weight == 3:
            self.coin_inventory['Quarter']+=1
        else:
            print("MACHINE WILL NOT ACCEPT THIS COIN")
        
    
a = VendingMachine()

b = Cola()

c = Penny()

a.stock_product(b)

a.stock_coin(c)

print(a.product_inventory, f'\n\n{a.coin_inventory}')