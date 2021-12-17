from random import *

import numpy as np


class Persona():

    def __init__(self, nombre = "", edad = 0, sexo = 'M', peso = 0, altura = 0):

        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo
        self.__altura = altura
        self.__peso = peso
        self.__DNI = ""

    def calcularIMC(self):

        imc = (float(self.__peso) / (float(self.__altura) * float(self.__altura)))
        if (imc > 18.5 and imc <= 24.9):
            return 0

        if (imc < 18.5):
            return -1
        else:
            return 1

    def esMayorEdad(self):
        if(int(self.__edad) >= 18):
            return True
        else:
            return False

    def introducirSexo(self, sexo):
        if(sexo == 'M' or sexo == 'H'):
            self.__sexo = sexo
        else:
            self.__sexo = 'M'

    def toString(self):
        return "Nombre: " +self.__nombre+" || Edad: " +str(self.__edad)+" || Sexo: " +self.__sexo+" || Peso: "+str(self.__peso)+" || Altura: "+str(self.__altura) + " || DNI:"+self.__DNI


    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_edad(self, edad):
        self.__edad = edad

    def set_sexo(self, sexo):
        self.__sexo = sexo

    def set_peso(self, peso):
        self.__peso = peso

    def set_altura(self, altura):
        self.__altura = altura

    def get_Nombre(self):
        return self.__nombre

    def crearDNI(self):
        array = np.array(["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"])
        n = randint(0000000, 99999999)
        resto = n % 23
        letra = array[resto]
        dni = str(n) + letra
        self.__DNI = dni


nombre = ""
while(nombre == ""):
    nombre = (input("Nombre: "))
    if(nombre != ""):
        break

edad = (input("Edad: "))
while(edad == ""):
    edad = (input("Edad: "))
    if(edad != ""):
        int(edad)
        break

sexo = ''
while(sexo == ""):
    sexo = input("Sexo: ")
    if(nombre != ""):
        break

peso = (input("Peso: "))
while(peso == ""):
    peso = (input("Peso: "))
    if(peso != ""):
        break

altura = (input("Altura: "))
while(altura == ""):
    altura = (input("Altura: "))
    if(altura != ""):
        break


persona = Persona(nombre, edad, sexo , peso, altura)
persona2 = Persona(nombre, edad, sexo , 100, 2)
persona3 = Persona()

persona3.set_nombre("Nosferatu")
persona3.set_edad(999)
persona3.set_sexo("H")
persona3.set_peso(50)
persona3.set_altura(2)

persona.introducirSexo(sexo)
persona2.introducirSexo(sexo)
persona3.introducirSexo("H")

persona.crearDNI()
persona2.crearDNI()
persona3.crearDNI()

if(persona.calcularIMC() == -1):
    print(persona.get_Nombre() + " Estas muy delgado")
if(persona.calcularIMC() == 0):
    print(persona.get_Nombre() + " Estas en tu peso ideal")
if(persona.calcularIMC() == 1):
    print(persona.get_Nombre() + " Estas con sobrepeso")

if(persona2.calcularIMC() == -1):
    print(persona2.get_Nombre() + " Estas muy delgado")
if(persona2.calcularIMC() == 0):
    print(persona2.get_Nombre() + " Estas en tu peso ideal")
if(persona2.calcularIMC() == 1):
    print(persona2.get_Nombre() + " Estas con sobrepeso")

if(persona3.calcularIMC() == -1):
    print(persona3.get_Nombre() + " Esta muy delgado")
if(persona3.calcularIMC() == 0):
    print(persona3.get_Nombre() + " Esta en su peso ideal")
if(persona3.calcularIMC() == 1):
    print(persona3.get_Nombre() + " Esta con sobrepeso")

print("-----------EDAD-------------")
if(persona.esMayorEdad()):
    print(persona.get_Nombre() + " Es mayor de edad")
else:
    print(persona.get_Nombre() + " No es mayor de edad")

if(persona2.esMayorEdad()):
    print(persona2.get_Nombre() + " Es mayor de edad")
else:
    print(persona2.get_Nombre() + " No es mayor de edad")

if(persona3.esMayorEdad()):
    print(persona3.get_Nombre() + " Es mayor de edad")
else:
    print(persona3.get_Nombre() + " No es mayor de edad")


print(persona.toString())
print(persona2.toString())
print(persona3.toString())

