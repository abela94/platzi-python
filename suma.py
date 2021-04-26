# -*- coding: utf-8 -*-

def sum(num1, num2, acum):
    if acum == num2:
        return num1 + acum
    else:
        acum += 1
        return sum(num1, num2, acum)


if __name__ == '__main__':
    num1 = int(raw_input('Give me the first number: '))
    num2 = int(raw_input('Give me the second number: '))
    
    result = sum(num1,num2,0)
    
    print('The result is: {}'.format(result))
    
    pass