class Series():
    _entregado = False

    def __init__(self, titulo = "", numTemp = 3, genero = "", creador = ""):
        self._titulo = titulo
        self._numTemp = numTemp
        self._genero = genero
        self._creador = creador

    def get_titulo(self):
        return self._titulo

    def get_numTemp(self):
        return self._numTemp

    def get_genero(self):
        return self._genero

    def get_Entregado(self):
        return self._entregado

    def get_creador(self):
        return self._creador

    def set_titulo(self, titulo):
        self._titulo = titulo

    def set_numTemp(self, numTemp):
        self._numTemp = numTemp

    def set_genero(self, genero):
        self._genero = genero

    def set_creador(self, creador):
        self._creador = creador


    def toString(self):
        return "Titulo :" +self._titulo + " Numero Temporada : "+ str(self._numTemp) + " Genero : " +self._genero + " Creador : " +self._creador

    def entregados(self):
        self._entregado = True

class Videojuegos():
    _entregado = False

    def __init__(self, titulo ="", horasEstimadas = 10, genero = "", compañia = ""):
        self._titulo = titulo
        self._horasEstimadas = horasEstimadas
        self._genero = genero
        self._compañia = compañia

    def get_titulo(self):
        return self._titulo

    def get_horasEstimadas(self):
        return self._horasEstimadas

    def get_Entregado(self):
        return self._entregado

    def get_genero(self):
        return self._genero

    def get_compañia(self):
        return self._compañia

    def set_titulo(self, titulo):
        self._titulo = titulo

    def set_numTemp(self, horas):
        self._horasEstimadas = horas

    def set_genero(self, genero):
        self._genero = genero

    def set_creador(self, compañia):
        self._compañia = compañia


    def toString(self):
        return "Titulo :" +self._titulo + " Horas Estimadas : "+ str(self._horasEstimadas) + " Genero : " +str(self._genero) + " Compañia : " +self._compañia

    def entregados(self):
        self._entregado = True

serie1 = Series("El Juego", 3, "Terror", "A.M")
serie2 = Series("En busca de eso", 1, "Drama", "J.M")
serie3 = Series("La vida", 2, "Drama", "P.M")
serie4 = Series("Si o no", 1, "Accion", "A.M")
serie5 = Series("El", 3, "Drama", "L.M")

videogame1 = Videojuegos("Dark Soul", 40, "Accion", "From Software")
videogame2 = Videojuegos("Dark Soul II", 30, "Accion", "From Software")
videogame3 = Videojuegos("Dark Soul III", 50, "Accion", "From Software")
videogame4 = Videojuegos("League of Legend", 80, "Accion", "Riot Games")
videogame5 = Videojuegos("Hollow Kigth", 20, "Accion", "A")

series = {serie5, serie4, serie3, serie2, serie1}
videojuegos = {videogame5, videogame4, videogame3, videogame2, videogame1}

serie2.entregados()
serie3.entregados()
serie5.entregados()

videogame1.entregados()
videogame3.entregados()
videogame5.entregados()

for i in series:
    if(i.get_Entregado()):
        print(i.toString())

print("")
for i in videojuegos:
    if(i.get_Entregado()):
        print(i.toString())

nombreSerie = ""
mayorTemporadas = 0

for i in series:
    if(i.get_numTemp() > mayorTemporadas):
        nombreSerie = i.get_titulo()
        mayorTemporadas = i.get_numTemp()

nombreVideojuego = ""
mayorHoras = 0
for i in videojuegos:
    if(i.get_horasEstimadas() > mayorHoras):
        nombreVideojuego = i.get_titulo()
        mayorHoras = i.get_horasEstimadas()

print("")
print("La serie con mas temporadas es " +nombreSerie + " con un numero de " +str(mayorTemporadas))
print("El videojuego con mas horas es " +nombreVideojuego + " con un numero de " +str(mayorHoras))