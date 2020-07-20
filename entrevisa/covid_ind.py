import json
from datetime import datetime

# Carga de datos
file = open('covid.json')
data_json = json.load(file)

prev_metro = None
prev_total = None
prev_total_date = None
prev_metro_date = None

percent_total = {}
percent_metro = {}

for i in reversed(range(len(data_json))):
    if data_json[i]['state'] == 'Metropolitana'and not prev_metro:
        prev_metro = data_json[i]['totalCases']
        prev_metro_date = datetime.strptime(data_json[i]['date'], '%Y-%m-%d')
        continue
    if data_json[i]['state'] == 'Total' and not prev_total:
        prev_total = data_json[i]['totalCases']
        prev_total_date = datetime.strptime(data_json[i]['date'], '%Y-%m-%d')
        continue
    if data_json[i]['state'] == 'Metropolitana':
        percent_metro[data_json[i]['date']] = (data_json[i]['newCases'] / prev_metro) * 100
        prev_metro = data_json[i]['totalCases']
        prev_metro_date = datetime.strptime(data_json[i]['date'], '%Y-%m-%d')
        percent_total[data_json[i]['date']] = (data_json[i]['newCases']  / prev_total) * 100
    if (data_json[i]['state'] == 'Total'):
        prev_total = data_json[i]['totalCases']
        prev_metro_date = datetime.strptime(data_json[i]['date'], '%Y-%m-%d')