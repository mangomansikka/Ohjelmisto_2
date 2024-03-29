"""
Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti.
Jokaisella julkaisulla on nimi. Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas
lehdellä on päätoimittaja. Kirjoita luokkiin myös tarvittavat alustajat.
Tee aliluokkiin metodi tulosta_tiedot, joka tudostaa kyseisen julkaisun kaikki tiedot.
Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6
(kirjailija Rosa Liksom, 200 sivua). Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.


"""

class Publication:
    book = 0
    magazine = 0
    def __init__(self, nimi):
        self.nimi = nimi

class Book(Publication):
    def __init__(self, name, writer, pages):
        self.name = name
        self.writer = writer
        self.pages = pages
        super().__init__(name)

    def print(self):
        print("------------------------------")
        print("The book's information")
        print(f"Name: {self.name}")
        print(f"Author: {self.writer}")
        print(f"The number of pages: {self.pages}")
        print("------------------------------")

class Magazine(Publication):
    def __init__(self, name, writer, eic):
        self.name = name
        self.writer = writer
        self.eic = eic
        super().__init__(name)

    def print(self):
        print("------------------------------")
        print("The magazine's information")
        print(f"Name: {self.name}")
        print(f"Writer: {self.writer}")
        print(f"Editor-in-chief: {self.eic}")

magazine1 = Magazine("Magazine", "Aku Ankka", "Aki Hyyppä")
book1 = Book("Hytti n:o 6", "Rosa Liksom", 200)


magazine1.print()
book1.print()
