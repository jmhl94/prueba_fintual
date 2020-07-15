'''
Algoritmo para generar datos aleatorios de Stock
'''
import pandas as pd
import numpy as np
from datetime import datetime
from datetime import timedelta
import ipdb

'Variables de control'
stock_market = {}

class Portfolio:
    def __init__(self):
        self.stock_data = {}
        
    def Profit(self, init_date_str, final_date_str):
        init_date = datetime.strptime(init_date_str, '%d-%m-%Y')
        final_date = datetime.strptime(final_date_str, '%d-%m-%Y')
        init_value = 0
        final_value = 0
        for stock in self.stock_data:
            purchased_date = datetime.strptime(self.stock_data[stock].purchased_date, '%d-%m-%Y')
            if purchased_date > final_date:
                continue
            elif purchased_date < init_date:
                #profit_stock = stock.ProfitValue(init_date_str, final_date_str)
                init_value += self.stock_data[stock].Price(init_date_str) * self.stock_data[stock].units
                final_value += self.stock_data[stock].Price(final_date_str) * self.stock_data[stock].units
            else:
                init_value += self.stock_data[stock].purchased_price * self.stock_data[stock].units
                final_value += self.stock_data[stock].Price(final_date_str) * self.stock_data[stock].units
        return  (final_value - init_value) / final_value
            
    def AddStock(self, symbol, name, purchase_date, purchase_value, units):
        self.stock_data[symbol] = Stock(name, symbol, purchase_date, purchase_value, units)
        
    def Assets(self):
        return list(self.stock_data.keys())

class Stock:
    def __init__(self, stock_name, symbol, purchased_date, purchased_price, units ):
        self.stock_name = stock_name
        self.symbol = symbol
        self.purchased_price = purchased_price
        self.purchased_date = purchased_date
        self.units = units

    def Price(self, date_str):
        return stock_market[self.symbol]['pricing_history'][date_str]
    '''
    def ProfitValue(self, init_date_str, final_date_str):
        init_values = self.Price(init_date_str)
        final_value = self.Price(final_date_str)
        return (final_value - init_values) / init_values'''
    
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
        units  = (np.random.rand() * 10) + 1
        Portfolio.AddStock(current_stock_symbol, current_stock_information['name'], 
                           purchase_date, purchase_value, units)
        used_stocks.append(current_stock_symbol)
        
'Prueba '
path = 'constituents_csv.csv'
create_market(path, '01-01-2020', '01-01-2021', stock_market, stocks_number = 100)
cartera = Portfolio()
fill_portfolio(cartera, stock_market, 10)