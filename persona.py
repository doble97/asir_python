from random import randint
from urllib import response


class Persona:
    def __init__(self, nombre:str, edad: int, sexo:str, peso:float=82.3, altura:float=1.92):
        self.nombre = nombre
        self.edad = edad
        self.dni = self.generaDNI()
        self.sexo = sexo
        self.peso = peso
        self.altura = altura

    def calcularIMC(self):
        operacion = self.peso/(self.altura**2)
        if operacion < 20:
            return -1
        elif operacion >= 20 and operacion <= 25:
            return 0
        else:
            return 1

    def esMayorDeEdad(self):
        return self.edad >= 18

    def comprobarSexo(self, sexo):
        respuesta=''
        if sexo=='M' or sexo=='m':
            respuesta = 'Es mujer' if self.sexo==sexo else 'Es hombre'
        else:
            respuesta = 'Es hombre'
        print(respuesta)

    def mostrar(self):
        atributos = self.__dict__
        print('INFORMACION DE LA PERSONA\n***************************************')
        for key in atributos:
            print(f'{key}->{atributos[key]}')

    def generaDNI(self):
        letras = ("T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C", "K","E","T")
        numeros= randint(10000000,99999999)
        letra = letras[numeros%23]
        dni = f'{numeros}{letra}'
        return dni

nombre = input('Nombre: ')
edad = int(input('Edad: '))
sexo = input('Sexo: ')
altura = float(input('Altura: '))
peso = float(input('Peso: '))

p1 = Persona(nombre,edad,sexo,peso,altura)
p2 = Persona(nombre,edad,sexo)
personas = [p1,p2]
contador = 1
for x in personas:
    p_temp = f'{contador}.{x.nombre}'
    if x.calcularIMC()==-1:
        print(p_temp,' peso ideal')
    elif x.calcularIMC()==1:
        print(p_temp,' tiene sobrepeso')
    else:
        print(p_temp,' por debajo de su peso ideal')
    if x.esMayorDeEdad():
        print(p_temp,' es mayor de edad')
    else:
        print(p_temp,' es menor de edad')
    contador = contador+1

[x.mostrar() for x in personas]
