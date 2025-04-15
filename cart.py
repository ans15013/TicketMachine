from ticket import Bilet
class Cart:
        def __init__(self):
            self.bilety: List[Bilet] = []

        def dodaj_bilet(self, bilet: Bilet):
            self.bilety.append(bilet)

        def suma(self) -> float:
            return sum(bilet.cena for bilet in self.bilety)

        def wyswietl(self):
            if not self.bilety:
                print("Koszyk jest pusty.")
            for bilet in self.bilety:
                print(bilet)
            print(f"SUMA: {self.suma():.2f} zł")