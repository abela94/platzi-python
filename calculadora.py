# -*- coding: utf-8 -*-

def foreign_exchange_calculator(amount):
    mex_to_col_rate = 145.97

    return mex_to_col_rate * amount
    
def run():
    print('CALCULADORA DE DIVISAS')
    print('Convierte de pesos mexicanos a pesos colombianos.')
    print('')
    
    amount = float(raw_input('Ingresa la cantidad de pesos mexicanos a convertir: '))
    
    result = foreign_exchange_calculator(amount)

    print('${} pesos mexicanos son ${} pesos colombianos'.format(amount,result))


if __name__ == '__main__':
    run()