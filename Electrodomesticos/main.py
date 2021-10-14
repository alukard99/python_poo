class Electrodomesticos():
    def __init__(self, precio = 100, color = "blanco", cEnergetico='F', peso=5 ):
        self._precio = precio
        self._color = color
        self._cEnergetico = cEnergetico
        self._peso = peso

    def get_precio(self):
        return self._precio

    def get_color(self):
        return self._color

    def get_cEnergetico(self):
        return self._cEnergetico

    def get_peso(self):
        return self._peso

    def comprobarColor(self):
        if(self._color == "blanco" or self._color == "negro" or self._color == "rojo" or self._color == "azul" or self._color == "gris"):
            self._color = self._color
        else:
            self._color = "blanco"

    def comprobarConsumoEnergetico(self):
        if(self._cEnergetico == 'A' or self._cEnergetico == 'B' or self._cEnergetico == 'C' or self._cEnergetico == 'D' or self._cEnergetico == 'E' or self._cEnergetico == 'F'):
            self._cEnergetico = self._cEnergetico
        else:
            self._cEnergetico = 'F'

    def preciofinal(self):
        """Esta es la parte en la que se suman dependiendo de su consmo de energia"""
        if(self._cEnergetico == 'A'):
            self._precio = self._precio + 100
        if (self._cEnergetico == 'B'):
            self._precio = self._precio + 80
        if (self._cEnergetico == 'C'):
            self._precio = self._precio + 60
        if (self._cEnergetico == 'D'):
            self._precio = self._precio + 50
        if (self._cEnergetico == 'E'):
            self._precio = self._precio + 30
        if (self._cEnergetico == 'F'):
            self._precio = self._precio + 10

        """Esta es la parte en la que se suma dependiendo de su tamaño"""
        if(self._peso >= 0 and self._peso <= 19):
            self._precio = self._precio + 10
        if (self._peso >= 20 and self._peso <= 49):
            self._precio = self._precio + 50
        if (self._peso >= 50 and self._peso <= 79):
            self._precio = self._precio + 80
        if (self._peso >= 80):
            self._precio = self._precio + 100


class lavadora(Electrodomesticos):
    def __init__(self, carga = 5, precio = 100, color= "blanco" , cEnergetico='F', peso=5):
        Electrodomesticos.__init__(self , precio, color, cEnergetico, peso)
        self._carga = carga

    def get_carga(self):
        return self._carga

    def preciofinal(self):
        Electrodomesticos.preciofinal(self)
        if(self._carga > 30):
            self._precio = self._precio + 50


class Television(Electrodomesticos):
    def __init__(self, resolucion = 20, fourK = False, precio = 100, color = "blanco", cEnergetico = 'F', peso= 5):
        Electrodomesticos.__init__(self, precio, color, cEnergetico, peso)
        self._resolucion = resolucion
        self._fourK = fourK

    def get_resolucion(self):
        return self._resolucion

    def get_fourK(self):
        return self._fourK

    def preciofinal(self):
        Electrodomesticos.preciofinal(self)
        if(self._resolucion > 40):
            self._precio = self._precio + (self._precio * 0.33)
        if(self._fourK):
            self._precio = self._precio + 50


lava1 = lavadora(10, 20, "rojo", 'A', 15)
lava2 = lavadora(5, 20, "blanco", 'F', 20)
lava3 = lavadora(15, 30, "amarillo", 'G', 30)
lava4 = lavadora(5, 10, "gris", 'B', 15)
tele1 = Television(10, True, 100, "negro", 'B', 30)
tele2 = Television(20, False, 300, "blanco", 'E', 80)
tele3 = Television(80, True, 700, "gris", 'F', 70)
tele4 = Television(90, False, 100, "magenta", 'G', 30)
tele5 = Television(20, True, 600, "negro", 'D', 30)
tele6 = Television(20, True, 100, "negro", 'B', 30)

array = {lava1, lava2, lava3, lava4 , tele1, tele2, tele3, tele4, tele5, tele6}

for i in array:
    i.comprobarColor()
    i.comprobarConsumoEnergetico()
    i.preciofinal()


totalElectro = 0
totalLavadora = 0
totalTelevision = 0
for i in array:
    totalElectro = totalElectro + i.get_precio()
    if(type(i) == lavadora):
        totalLavadora = totalLavadora + i.get_precio()
    if(type(i) == Television):
        totalTelevision = totalTelevision + i.get_precio()



print("-------PRECIO TOTAL ELECTRODOMESTICOS------")
print(totalElectro)
print("-------PRECIO TOTAL LAVADORAS------")
print(totalLavadora)
print("-------PRECIO TOTAL TELEVISIONES------")
print(totalTelevision)
