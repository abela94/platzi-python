# -*- coding: utf-8 -*-
import random


IMAGE = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#Word bank of animals
WORDS = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

def random_word():
    idx = random.randint(0, len(WORDS) - 1)
    
    return WORDS[idx]
    
def display_board(hidden_word,tries):
    print(IMAGE[tries])
    print{''}
    print(hidden_word)
    print('---*---*---*---*---*---*')

def run():
    word =  random_word()
    hidden_word = ['-'] * len(word)
    tries = 0
    
    while True:
        display_board(hidden_word,tries)
        current_letter = str(raw_input('Introduce una letra: '))
        letter_indexes = []
        
        for idx in range(len(word)):
            if word[idx] == current_letter:
                letter_indexes.append(idx)
        
        if len(letter_indexes) == 0:
            tries += 1
            
            if tries == 6:
                display_board(hidden_word,tries-1)
                print('')
                print('You Lost. The correct word was: {}'.format(word))
                break
        
        else:
            for idx in letter_indexes:
                hidden_word[idx] = current_letter
            letter_indexes = []

        try:
            hidden_word.index('-')
        except ValueError:
            print('You won! The word was {}'.format(word))
            break
    pass

if __name__ == '__main__':
    print('A H O R C A D O S')
    
    run()
    
    pass