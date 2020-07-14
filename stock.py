'''
Algoritmo para generar datos aleatórios de Stock
'''
import pandas as pd

class Portfolio:
    stock_data = None
    def __init__(self, path_data):
        stock_data_raw = pd.read_csv(path_data)
        stock_data_raw['Date'] = pd.to_datetime(stock_data_raw['Date'], format= '%Y-%m-%d')
        self.stock_data = stock_data_raw
        
    def Profit(self, init_date, final_date):
        pass
    
    def Price(self):
        pass
        
    