# -*- coding: utf-8 -*-

def run():
    
    counter = 0
    
    with open('aleph.txt', 'r') as f:
        for line in f:
            counter += line.count('Beatriz')

    
    print('La palabra Beatriz tiene {} ocurrencias'.format(counter))

if __name__ == '__main__':
    run()
    