class Book:
    def __init__(self, tytul, autor, rok):
        self.tytul = tytul
        self.autor = autor
        self.rok = rok

    def __str__(self):
        return f"Tytuł: {self.tytul}, Autor: {self.autor}, Rok: {self.rok}"

ks1 = Book("Jak zostać szachistą XXI wieku? Kompendium wiedzy dla początkujących", "Aleksander Radomski", "2020-04-10")

print(ks1)
