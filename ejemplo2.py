# -*- coding: utf-8 -*-
import turtle

def main():
    window = turtle.Screen()
    abe = turtle.Turtle()
    
    make_square(abe)
    
    turtle.mainloop()

def make_square(abe):
    length = int(raw_input('Tamano del cuadrado: '))
    
    for i in range(4):
        make_line_and_turn(abe,length)

def make_line_and_turn(abe, length):
    abe.forward(length)
    abe.left(90)

if __name__ == '__main__':
    main()