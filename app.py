import os
from pickle import TRUE

limpiar_pantalla=lambda: os.system('cls' if os.name=='nt' else 'clear')
class Agenda:
    def __init__(self):
        self.dato=list()

    def menu(self):
        print()
        menu=[
        ['Agenda Personal'],
        ['1. Añadir Contacto',"anadir"],
        ['2. Lista de contactos'],
        ['3. Buscar contacto'],
        ['4. Editar contacto'],
        ['5. Eliminar contacto'],
        ['6. Cerrar agenda']
        ]
        for x in range(7):
            print(menu[x][0])
        
    def add_contacto(self, contacto):
        self.dato.append(contacto)
    def lista_contacto(self)->None:
        if not self.agenda_vacia():
            for x in self.dato:
                print(f'***\n{x["nombre"]}\n{x["telefono"]}\n{x["email"]}\n***')
        else:
            print('No tienes contactos todavía')
    def buscar_contacto(self):
        pass
    def editar_contacto(self):
        pass
    def eliminar_contacto(self):
        pass
    def agenda_vacia(self)->bool:
        return len(self.dato)==0
    
agenda = Agenda()
while True:
    agenda.menu()
    opcion = int(input('Opcion 1-6: '))
    limpiar_pantalla()
    if opcion==1:
        contacto= dict()
        contacto['nombre']=input('Nombre del contacto: ')
        contacto['telefono']=int(input('Telefono del contacto: '))
        contacto['email'] = input('Correo del contacto: ')
        agenda.add_contacto(contacto)
        pass
    elif opcion==2:
        agenda.lista_contacto()
    elif opcion==3:
        pass
    elif opcion==4:
        pass
    elif opcion==5:
        pass
    elif opcion==6:
        pass
    else:
        pass
