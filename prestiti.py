class Prestito:
    def __init__(self, codice_prestito, data, id_strumento, cognome_allievo):
        self.__codice_prestito = codice_prestito
        self.__data = data
        self.__id_strumento = id_strumento
        self.__cognome_allievo = cognome_allievo
        #self.__strumen = []

    @property
    def codice_prestito(self):
        return self.__codice_prestito

    @property
    def id_strumento(self):
        return self.__id_strumento


    def __str__(self):
        return f"Prestito {self.__codice_prestito}: {self.__id_strumento} a {self.__cognome_allievo} in data {self.__data}"