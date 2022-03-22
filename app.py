from pickle import TRUE


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
        
    def add_contacto(self):
        pass
    def lista_contacto(self):
        pass
    def buscar_contacto(self):
        pass
    def editar_contacto(self):
        pass
    def eliminar_contacto(self):
        pass
    
agenda = Agenda()
agenda.menu()
while True:
    opcion = 1
    if opcion==1:
        pass
    elif opcion==2:
        pass
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
