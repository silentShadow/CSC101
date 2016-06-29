'''\
rev: 1
author: jonathan reiter
description: 
reference: listing 7.2
page: 236 (PDF 256)
'''
import ystockquote


class Stock():
    def __init__(self, symbol="TSLA", name="Tesla", previous_closing_price=0, current_price=0):
        self.__symbol = symbol
        self.__name = name
        self.__previous_closing_price = previous_closing_price
        self.__current_price = current_price
    
    def get_name( self):
        return self.__name
    
    def get_symbol( self):
        return self.__symbol
    
    def get_previous_closing_price( self):
        return self.__previous_closing_price
    
    def get_current_price( self):
        return self.__current_price

    def get_change_percent( self):
        change = self.__current_price - self.__previous_closing_price
        return ( change / self.__previous_closing_price ) * 100.0
    
    def set_previous_closing_price( self, previous_closing_price):
        self.__previous_closing_price = previous_closing_price
    
    def set_current_price( self, current_price):
        self.__current_price = current_price


class GetStockInfo():
    def __init__( self, symbol="TSLA"):
        self.symbol = symbol
        self.all_info = ystockquote.get_all( self.symbol)
    
    def get_current_price( self):
        return self.all_info["price"]
    
    def get_change( self):
        return self.all_info["change"]

    def get_fifty_two_week_high( self):
        return self.all_info["fifty_two_week_high"]
        
    def get_fifty_two_week_low( self):
        return self.all_info["fifty_two_week_low"]
    
    def get_price_earnings_growth_ratio( self):
        return self.all_info["price_earnings_growth_ratio"]



def main():
    stock = GetStockInfo()
    



if __name__ == '__main__': main()