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
    def print_contacto(self, contacto):
        print(f'***\n{x["nombre"]}\n{x["telefono"]}\n{x["email"]}\n***')

    
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
        if not agenda.agenda_vacia():
            nombre = input('Escribe el nombre del contacto a buscar: ')
            contactos_encontrados = []
            for x in agenda.dato:
                if x['nombre']==nombre:
                    contactos_encontrados.append(x)
            if len(contactos_encontrados)>0:
                print('Contactos encontrados serán listados:')
                [agenda.print_contacto(x) for x in contactos_encontrados]
            else:
                print('No se ha encontrado ningun contacto con el nombre',nombre)
        else:
            print('No tienes contactos, no se puede buscar en la agenda')
    elif opcion==4:
        pass
    elif opcion==5:
        posiciones_contactos = []
        if not(agenda.agenda_vacia()):
            nombre=input('Escribe el nombre del contacto para buscar: ')
            posiciones_contactos = [x for x in range(len(agenda.dato)) if agenda.dato[x]['nombre']==nombre]
            if len(posiciones_contactos)>0:
                print('Se ha encontrado los siguientes contactos que se llamen:', nombre)
                for x in posiciones_contactos:
                    print('**************')
                    print('Posicion',x,'')
                    print(f'{agenda.dato[x]["nombre"]}\n{agenda.dato[x]["telefono"]}\n{agenda.dato[x]["email"]}')
        else:
            print('No se ha encontrado ningun contacto con el nombre',nombre)
    elif opcion==6:
        print('Saliendo de la agenda...')
        exit()

    else:
        pass
