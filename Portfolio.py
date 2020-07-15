'''
Algoritmo para generar datos aleatórios de Stock
'''
import pandas as pd
import numpy as np
from datetime import datetime
from datetime import timedelta
stock_market = {}

class Portfolio:
    stock_data = {}
    def __init__(self, path_data):
        pass
    def Profit(self, init_date, final_date):
        pass

    def Price(self):
        pass

    def AddStock(self):
        pass

class Stock:
    def __init__(self, stock_name, purchased_price, purchased_date, units ):
        self.stock_name = stock_name
        self.purchased_price = purchased_price
        self.purchased_date = purchased_date
        self.units = units

    def Price(self, date_str):
        return stock_market[self.stock_name][date_str]
    
def create_market(path, stocks_number, start_date, end_date, stock_market):
    stoks_names = pd.read_csv(path)
    used_stocks = []
    total_stocks = len(stoks_names)
    while (len(stock_market) < stocks_number):
        index = np.random.randint(0, total_stocks)
        if index in used_stocks:
            continue
        current_stock = stoks_names.iloc[index, :]
        stock_market[current_stock['Symbol']] = {
                'name':current_stock['Name'],
                'Pricing history':date_and_stock_range(start_date,
                                                       end_date,
                                                       step = 1,) }
        used_stocks.append(index)
        
    
def date_and_stock_range(start, end, step=7, date_format="%d-%m-%Y"):
    start = datetime.strptime(start, date_format)
    end = datetime.strptime(end, date_format)
    num_days = (end - start).days
    date_stock = {}
    for d in range(0, num_days + step, step):
        date_i = start + timedelta(days=d)
        date_stock[date_i.strftime(date_format)] = (np.random.rand() * 300 ) + 1
    return date_stock