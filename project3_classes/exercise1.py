class Pracownik:
    def __init__(self, imie, nazwisko, wiek, stanowisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.stanowisko = stanowisko

    def przedstaw_sie(self):
        print(f"Nazywam sie {self.imie}, {self.nazwisko}, mam {self.wiek} i pracuje jako {self.stanowisko}")

    def zmien_stanowisko(self,nowe_stanowisko):
        self.stanowisko = nowe_stanowisko

    def zwieksz_wiek(self, lata):
        self.wiek = self.wiek + lata

    def czy_jest_pelnoletni(self):
        if self.wiek >= 18:
            print("osoba jest pelnoletnia")
        else:
            print("osoba nie jest pelnoletnia")
        
if __name__ == "__main__":
    pracownik1 = Pracownik("Jan", "Kowalski", 30, "Inzynier")
    pracownik1.przedstaw_sie()
    pracownik1.zmien_stanowisko("Mechanik")
    pracownik1.przedstaw_sie()
    pracownik1.zwieksz_wiek(1)
    pracownik1.przedstaw_sie()
    pracownik1.czy_jest_pelnoletni()

    
    