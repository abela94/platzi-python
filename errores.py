# -*- coding: utf-8 -*-

COUNTRIES = {
    'mexico': 122,
    'colombia': 49,
    'argentina': 43,
    'chile': 29,
    'peru': 31
}

def run():
    
    while True:
        
        country = str(raw_input('Escribe el nombre de un pais: ')).lower()
        
        try:
            print('La poblacion de {} es: {}'.format(country.capitalize(),COUNTRIES[country]))
        except KeyError:
            print('No tenemos la cantidad de poblacion de {}'.format(country.capitalize()))    
      


if __name__ == '__main__':
    run()
    
    pass