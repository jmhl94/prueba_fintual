'''
Algoritmo para generar datos aleat√≥rios de Stock
'''
import pandas as pd
import numpy as np
from datetime import datetime
from datetime import timedelta

'Variables de control'
stock_market = {}

class Portfolio:
    def __init__(self, path_data):
        self.stock_data = {}
        
    def Profit(self, init_date, final_date):
        pass

    def AddStock(self, symbol, name, purchase_date, purchase_value, units):
        stock_data[symbol] = {'name': name, 'purchase_date': purchase_date,
                              'purchase_value': purchase_value, 'units':units
                              }
    def Assets(self):
        return list(stock_data.keys())

class Stock:
    def __init__(self, stock_name, purchased_price, purchased_date, units ):
        self.stock_name = stock_name
        self.purchased_price = purchased_price
        self.purchased_date = purchased_date
        self.units = units

    def Price(self, date_str):
        return stock_market[self.stock_name][date_str]
    
def create_market(path, start_date, end_date, stock_market, stocks_number = 10):
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
                'pricing_history':date_and_stock_range(start_date,
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

def fill_portfolio(Portfolio, stock_market, asset_numbers):
    'Generador aleatorio de activos en portafolio'
    available_stock = list(stock_market.keys())
    used_stocks = []
    
    while(len(Portfolio.Assets()) < asset_numbers):
        current_stock_symbol = np.random.choice(available_stock)
        if current_stock_symbol in used_stocks:
            continue
        current_stock_information = stock_market[current_stock_symbol]
        purchase_date = np.random.choice(list(current_stock_information['pricing_history'].keys()))
        purchase_value = current_stock_information['pricing_history'][purchase_date]
        'Solo se pueden adquirir hasta 10 acciones usando el generador autom·tico'
        units  = (np.random.rand() * 10) + 1
        Portfolio.AddStock(current_stock_symbol, current_stock_information['name'], 
                           purchase_date, purchase_value, units)
        used_stocks.append(current_stock_symbol)