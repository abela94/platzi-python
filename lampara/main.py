# -*- coding: utf-8 -*-

from lampara import Lamp

def run():

    lamp = Lamp(is_turned_on = True)
    
    while True:
        command = str(raw_input('''
            Â¿QuÃ© deseas hacer?

            [p]render
            [a]pagar
            [s]alir
        '''))

        if command == 'p':
            lamp.turn_on()
        elif command == 'a':
            lamp.turn_off()
        else:
            break
    
if __name__ == '__main__':
    run()