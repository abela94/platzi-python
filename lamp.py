# -*- coding: utf-8 -*-

class Lamp:
       
    _LAMPS = ['''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
    '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']
     
    def __init__(self, is_turned_on):
        self.is_turned_on = is_turned_on
        
    def turn_on(self):
        self.is_turned_on = True
        self.display_lamp()
 
    def turn_off(self):
        self.is_turned_on = False
        self.display_lamp()
        
    def display_lamp(self):
        if self.is_turned_on:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])
          

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
    