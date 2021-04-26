# -*- coding: utf-8 -*-

import csv

class Contact:
  
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


class ContactBook:
  
    def __init__(self):
        self._contacts = []
    
    def add(self, name, phone, email):
        contact = Contact(name,phone,email)
        self._contacts.append(contact)
        self._save()

    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)
            
    def _print_contact(self,contact):
        print('*----------*----------*----------*')
        print('Nombre: {}'.format(contact.name))
        print('Telefono: {}'.format(contact.phone))
        print('Email:: {}'.format(contact.email))
        print('*----------*----------*----------*')

    def delete(self,name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                break
            
        self._save()
            
    def find(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break
        else:
            self._no_find(name)
    
    def refresh(self, name_old, name, phone, email):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name_old.lower():
                self._contacts[idx].name = name
                self._contacts[idx].phone = phone
                self._contacts[idx].email = email 
                break
        else:
            self._no_find(name_old)
            
        self._save()
  
    
    def _no_find(self, name):
        print('*----------*----------*----------*')
        print('El contacto {}, no fue encontrado'.format(name))
        print('*----------*----------*----------*')
                
    def _save(self):
        with open('contacts.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(('name', 'phone', 'email'))
            
            for contact in self._contacts:
                writer.writerow( (contact.name, contact.phone, contact.email) )

def run():
    
    contact_book = ContactBook()
    
    with open('contacts.csv', 'r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue
            
            contact_book.add(row[0],row[1],row[2])
        

    while True:
        command = str(raw_input('''
            Que deseas hacer?

            [a]Ã±adir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contactos
            [s]alir
        '''))

        if command == 'a':
            name = str(raw_input('Escribe el nombre del contacto: '))
            phone = str(raw_input('Escribe el numero del contacto: '))
            email = str(raw_input('Escribe el email del contacto: '))
            
            contact_book.add(name,phone,email)
            
        elif command == 'ac':
            name_old = str(raw_input('Escribe el nombre del contacto a actualizar: '))
            name = str(raw_input('Escribe el nombre del contacto: '))
            phone = str(raw_input('Escribe el numero del contacto: '))
            email = str(raw_input('Escribe el email del contacto: '))
            contact_book.refresh(name_old, name, phone, email)
            
        elif command == 'b':
            name = str(raw_input('Escribe el nombre del contacto: '))
            contact_book.find(name)

        elif command == 'e':
            name = str(raw_input('Escribe el nombre del contacto: '))
            contact_book.delete(name)


        elif command == 'l':
            contact_book.show_all()

        elif command == 's':
            break
        else:
            print('Comando no encontrado.')


if __name__ == '__main__':
    print('Bienvenido a la agenda de contactos')
    run()