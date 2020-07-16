# Prueba Fintual
### Descripcción
El presente repositorio cuenta con el archivo Portfolio .py, en donde se encuentran la lógica para crear una cartera bursátil usando la clase Portfolio

El código fue escrito en python 3.6.9, es necesario tener instalado python 3 o un entorno como anaconda en su ordenador para ejecutar los códigos, en lo siguientes links están los pasos para instalar python o anaconda:
- [Instalar python 3](https://www.python.org/downloads/)
- [Instalar spyder](https://www.spyder-ide.org/)

### Implementación
Para ejecutar los comandos es necesario abrir una consola de IPython, para ello se debe abrir una terminal, cambiar el directorio a la carpeta en donde están almacenados los códigos y ejecutar el siguiente comando:
```
ipython
```

Desde la terminal de python se deben importar las librerías, se recomienda usar:
```
from Portfolio import *
```

Con este comando se cargará al directorio las clases definidas en el archivo y adicionalmente se creará un prototipo de portafolio con datos de mercado generados aleatoriamente

### Modo de uso
Usando la variables "cartera", generada a partir de los datos aleatorios de mercado se pueden probar cada unos de los metodos de las clases Portfolio y Stock.

Por ejemplo: si se busca la rentabilidad de la cartera para el mes de enero de 2020 se debe ejecutar el siguiente comando
```
cartera.Profit()
```
El resultado es un diccionario, en donde cada elemento representa la rentabilidad de la cartera por cada año del rango. En cada año se presenta la siguiente información:
- Rentabilidad de la cartera
- Valor de la cartera al inicio del rango
- Valor de la cartera al final del rango

A continuación se presenta un ejemplo de la rentabilidad en un periodod de tiempo:
```
{'2012':
    {'Profit': 0.48,
    'Initial value': 871.62,
    'Final value': 1664.12},
 '2013':
    {'Profit': 0.35,
    'Initial value': 2291.03,
    'Final value': 3543.48},
 '2014':
    {'Profit': -0.42,
    'Initial value': 10227.96,
    'Final value': 7212.81},
 '2015':
    {'Profit': -0.12,
    'Initial value': 12514.34,
    'Final value': 11222.08}}
```
