from Candy import Candy
from Chips import Chips
from Cola import Cola
from Product import Product


class ProductInventory():
    def __init__(self) -> None:  
        self.chip_inventory= 0
        self.cola_inventory = 0
        self.candy_inventory= 0     

    def stock_product(self, products = [Product])->None:
        for product in products:
            if type(product) == Cola:
                self.cola_inventory +=1            
            elif type(product) == Chips:
                self.chip_inventory += 1
            elif type(product) == Candy:
                self.candy_inventory += 1
            else:
                print("MACHINE WILL NOT ACCEPT THIS ITEM")
