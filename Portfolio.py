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
    '''Clase Portfolio
    Genera la base para una cartera de acciones Simple

    Atributos:
    - stock_data = diccionario que contiene toda la informacion relevante de las acciones
    almacenada en objetos tipo Stock

    Metodos:
    - Profit   = calcula la rentabilidad de la cartera
    - AddStock = agrega acciones a la cartera existente
    - Assets   = retorna una lista con todas las acciones poseidas por el cliente
    '''
    def __init__(self):
        self.stock_data = {}

    def Profit(self, init_date_str, final_date_str):
        init_date = datetime.strptime(init_date_str, '%d-%m-%Y')
        final_date = datetime.strptime(final_date_str, '%d-%m-%Y')
        delta_years = final_date.year - init_date.year
        annualized_profit = {}
        if delta_years == 0:
            annualized_profit[str(init_date.year)] = self.AnualProfit(init_date_str, final_date_str)
        else:
            for year in range(delta_years + 1):
                current_year = str(init_date.year + year)
                if year == 0:
                    annualized_profit[current_year] = self.AnualProfit(init_date_str, '31-12-' + current_year)
                elif year == delta_years:
                    annualized_profit[current_year] = self.AnualProfit('01-01-' + current_year, final_date_str)
                else:
                    annualized_profit[current_year] = self.AnualProfit('01-01-' + current_year, '31-12-' + current_year)
        return annualized_profit

    def AnualProfit(self, init_date_str, final_date_str):
        init_date = datetime.strptime(init_date_str, '%d-%m-%Y')
        final_date = datetime.strptime(final_date_str, '%d-%m-%Y')
        init_value = 0
        final_value = 0
        for stock in self.stock_data:
            purchased_date = datetime.strptime(self.stock_data[stock].purchased_date, '%d-%m-%Y')
            # Descarta acciones compradas despues del rango buscado
            if purchased_date > final_date:
                continue
            elif purchased_date < init_date:
                init_value += self.stock_data[stock].Price(init_date_str) * self.stock_data[stock].units
                final_value += self.stock_data[stock].Price(final_date_str) * self.stock_data[stock].units
            # Solo calcula la rentabilidad desde el momento de compra de la acción
            else:
                init_value += self.stock_data[stock].purchased_price * self.stock_data[stock].units
                final_value += self.stock_data[stock].Price(final_date_str) * self.stock_data[stock].units

        if init_value == 0 or final_value == 0:
            return {'Profit':None, 'Initial value':None, 'Final value':None}
        else:
            return  {'Profit':round((final_value - init_value) / final_value, 2),
                     'Initial value':round(init_value, 2),
                     'Final value':round(final_value, 2)}

    def AddStock(self, symbol, name, purchase_date, purchase_value, units):
        self.stock_data[symbol] = Stock(name, symbol, purchase_date, purchase_value, units)

    def Assets(self):
        return list(self.stock_data.keys())

class Stock:
    '''Clase "Stock"
    Atributos:
    - stock_name      = nombre de la acción
    - symbol          = simbolo que representa la acción
    - purchased_price = precio de compra
    - purchased_date  = fecha de compra
    - units           = cantidad de acciones poseida

    '''
    def __init__(self, stock_name, symbol, purchased_date, purchased_price, units ):
        self.stock_name = stock_name
        self.symbol = symbol
        self.purchased_price = purchased_price
        self.purchased_date = purchased_date
        self.units = units

    def Price(self, date_str):
        return stock_market[self.symbol]['pricing_history'][date_str]

'''Creación de datos de mercado'''
def create_market(path, start_date, end_date, stock_market, market_share = 10):
    '''
    Función para datos de mercado de valores de forma aleatoria

    Variables de entrada:
    - path         = direccion en memoría del archivo con los nombres de compañias
    - start_date   = fecha inicial en formato %d-%m-%Y (ejemplo = 01-02-2020)
    - end_date     = fecha final en formato %d-%m-%Y (ejemplo = 31-12-2020)
    - stock_market = archivo que almacenará los datos de mercado
    - market_share = numero de empresas que constituiran el mercado
    '''
    stoks_names = pd.read_csv(path)
    used_stocks = []
    total_stocks = len(stoks_names)
    while (len(stock_market) < market_share):
        index = np.random.randint(0, total_stocks)
        if index in used_stocks:
            continue
        current_stock = stoks_names.iloc[index, :]
        stock_market[current_stock['Symbol']] = {
                'name':current_stock['Name'],
                'pricing_history':date_and_stock_range(start_date,
                                                       end_date,
                                                       step = 1,)}
        used_stocks.append(index)


def date_and_stock_range(start, end, step=7, date_format="%d-%m-%Y"):
    '''
    Función para generar el registro de acciones de un activo individual

    Variables de entrada
    - start       = fecha inicial
    - end         = fecha final
    - step        = frecuencia de registros en días
    - date_format = formato de fechas
    '''
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

'''Prueba de los algoritmos'''
path = 'constituents_csv.csv'
create_market(path, '01-01-2010', '01-01-2021', stock_market, market_share = 100)
cartera = Portfolio()
fill_portfolio(cartera, stock_market, 20)
