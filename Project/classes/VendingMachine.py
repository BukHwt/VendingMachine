from Candy import Candy
from Chips import Chips
from Coin import Coin
from Cola import Cola
from Penny import Penny
from Product import Product
from Quarter import Quarter
from Dime import Dime
from Nickel import Nickel


class VendingMachine():
    
    def __init__(self, coin_inventory = {Nickel:0, Dime:0, Quarter:0}) -> None:
        self.coin_inventory = coin_inventory
    
    def stock_coin(self, coin : Coin)->None:
        if coin.size and coin.weight == 1:
            self.coin_inventory[Dime]+=1
        elif coin.size and coin.weight == 2:
            self.coin_inventory[Nickel]+=1
        if coin.size and coin.weight == 3:
            self.coin_inventory[Quarter]+=1
        else:
            print("MACHINE WILL NOT ACCEPT THIS COIN")
        