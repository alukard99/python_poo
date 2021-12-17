class Series():
    _entregado = False

    def __init__(self, titulo = "", numeroTemporada = 3, genero ="", creador =""):
        self._titulo = titulo
        self._numeroTemporada = numeroTemporada
        self._genero = genero
        self._creador = creador

    def get_titulo(self):
        return self._titulo

    def get_numTemp(self):
        return self._numeroTemporada

    def get_genero(self):
        return self._genero

    def get_Entregado(self):
        return self._entregado

    def get_creador(self):
        return self._creador

    def set_titulo(self, titulo):
        self._titulo = titulo

    def set_numTemp(self, numTemp):
        self._numeroTemporada = numTemp

    def set_genero(self, genero):
        self._genero = genero

    def set_creador(self, creador):
        self._creador = creador


    def toString(self):
        return "Titulo:" + self._titulo + ", Numero de temporada: " + str(self._numeroTemporada) + ", Genero: " + self._genero + ", Creador: " + self._creador

    def entregados(self):
        self._entregado = True

class Videojuegos():
    _entregado = False

    def __init__(self, titulo ="", horasEstimadas = 0, genero = "", compañia = ""):
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

serie1 = Series("Brooklyn 99", 7, "Comedia", "Netflix")
serie2 = Series("Doctor Who", 11, "Aventura", "BBC")
serie3 = Series("La casa de papel", 6, "Accion", "Netflix")
serie4 = Series("Malviviendo", 3, "Drama", "Entertainment")
serie5 = Series("Padre de familia", 8, "Comedia", "Fuzzy Door")

videogame1 = Videojuegos("The Elder Scrolls: Arena", 100, "Accion", "Bethesda")
videogame2 = Videojuegos("The Elder Scrolls II: Daggerfall", 100, "Accion", "Bethesda")
videogame3 = Videojuegos("The Elder Scrolls III: Morrowind", 150, "Accion", "Bethesda")
videogame4 = Videojuegos("The Elder Scrolls IV: Oblivion", 200, "Accion", "Bethesda")
videogame5 = Videojuegos("The Elder Scrolls V: Skyrim", 300, "Accion", "Bethesda")

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

print("La serie con mas temporadas es " +nombreSerie + " con " +str(mayorTemporadas) + " temporadas")
print("El videojuego con mas horas es " +nombreVideojuego + " con " +str(mayorHoras) + " horas de duracion.")