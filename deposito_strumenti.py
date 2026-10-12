from strumenti import Strumento
from prestiti import Prestito
from operator import attrgetter

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self.__nome = nome
        self.__responsabile = responsabile
        self.__strumenti = []
        self.__prestiti = []
        # le liste mi servono nelle ultime funzioni (es. per generare nuovi codici a partire da ultimo presente)

    @property # leggo il valore
    def responsabile(self):
        return self.__responsabile

    @responsabile.setter # modifico il valore
    def responsabile(self, responsabile):
        self.__responsabile = responsabile


    def carica_file_strumenti(self, file_path):

        file_in = open(file_path, 'r')
        for line in file_in:
            lista_elementi = line.strip().split(",")

            codice_str = lista_elementi[0]
            tipo_str = lista_elementi[1]
            marca_str = lista_elementi[2]
            anno_acquisto_str = int(lista_elementi[3])
            prezzo_str = float(lista_elementi[4])

            # creo un nuovo oggetto della classe strumento
            nuovo_strumento = Strumento(codice_str, tipo_str, marca_str, anno_acquisto_str, prezzo_str)

            # aggiungo il nuovo strumento alla lista per poter nelle funzioni successive utilizzarlo (es.ultimo codice)
            self.__strumenti.append(nuovo_strumento)

        file_in.close()



    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        # aggiungo strumento solo nel sistema e non nel file

        # calcolo il nuovo codice
        if len(self.__strumenti) == 0:
            nuovo_numero = 1
        else:
            ultimo_strumento = self.__strumenti[-1]
            # self.strumenti è una lista di oggetti e ultimo_strumento diventa l'ultimo oggetto (strumento) della lista
            ultimo_numero = int(ultimo_strumento.codice[1:])
            nuovo_numero = ultimo_numero + 1

        cod = f"S{nuovo_numero}"

        # creo il nuovo oggetto
        nuovo_strumento = Strumento(cod, tipo, marca, anno_acquisto, valore)

        # inserisco il nuovo oggetto nel sistema cioè nella lista strumenti
        self.__strumenti.append(nuovo_strumento)

        return nuovo_strumento


    def strumenti_ordinati_per_marca(self):
        # attrgetter("attributo")
        return sorted(self.__strumenti, key=attrgetter("marca"))



    def nuovo_prestito(self, data, id_strumento, cognome_allievo):

        # inizializzo con valori booleani
        strumento_mancante = True
        strumento_gia_prestato = False

        # ciclo all'interno della lista strumenti
        for elemento in self.__strumenti:
            if id_strumento == elemento.codice:
                strumento_mancante = False # lo strumento c'è in deposito
                break

        # ciclo all'interno della lista prestiti
        for el in self.__prestiti:
            if el.id_strumento == id_strumento:
                strumento_gia_prestato = True # caso strumento già prestato
                break

        if strumento_mancante or strumento_gia_prestato:
            raise Exception("Errore: strumento non esistente o già in prestito")

        else:
            if len(self.__prestiti) == 0:
                ultimo_cod = 0
            else:
                ultimo_cod = int(self.__prestiti[-1].codice_prestito[1:])
                # prendo l'ultimo valore, di cui estrapolo il numero (cioè il codice senza lettera)

            nuovo_cod = f"P{ultimo_cod + 1}"

            nuovo_prestito = Prestito(nuovo_cod, data, id_strumento, cognome_allievo)
            self.__prestiti.append(nuovo_prestito)

        return nuovo_prestito



    def termina_prestito(self, id_prestito):

        prestito_trovato = False
        prestito_da_rimuovere = None

        for cod in self.__prestiti:
            if id_prestito == cod.codice_prestito: # se id passato corrisponde ad un codice nella lista prestiti
                prestito_trovato = True
                prestito_da_rimuovere = cod
                break

        if not prestito_trovato:
            raise Exception("Errore: il prestito non esiste")

        else:
            self.__prestiti.remove(prestito_da_rimuovere)

        return True
