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

class Book(Publication):
    def __init__(self, name, writer, pages):
        self.name = name
        self.writer = writer
        self.pages = pages

    def print(self):
        print(f"Book's name: {self.name}")
        print(f"Book's author: {self.writer}")
        print(f"The number of pages: {self.pages}")

class Magazine(Publication):
    def __init__(self, name, writer, eic):
        self.name = name
        self.writer = writer
        self.eic = eic

    def print(self):
        print(f"Magazine's name: {self.name}")
        print(f"Magazine's writer: {self.writer}")
        print(f"Magazine's editor-in-chief: {self.eic}")

magazine1 = Magazine("Magazine", "Aku Ankka", "Aki Hyyppä")
book1 = Book("Hytti n:o 6", "Rosa Liksom", 200)


magazine1.print()
book1.print()
