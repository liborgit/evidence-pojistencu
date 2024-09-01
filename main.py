from src.pojistenec import Pojistenec
from spravce_pojistencu import SpravcePojistencu

class UzivatelskeRozhrani:
    def __init__(self):
        self.spravce = SpravcePojistencu()

    def zadat_jmeno_a_prijmeni(self):
        jmeno = input("Zadejte jméno: ").strip()
        prijmeni = input("Zadejte příjmení: ").strip()
        return jmeno, prijmeni

    def pridat_pojistence(self):
        jmeno, prijmeni = self.zadat_jmeno_a_prijmeni()
        vek = input("Zadejte věk: ").strip()
        telefon = input("Zadejte telefonní číslo: ").strip()

        # Převod věku na číslo
        try:
            vek = int(vek)
        except ValueError:
            vek = 0

        validace, chybova_zprava = self.spravce.validovat(jmeno, prijmeni, vek, telefon)
        if validace:
            pojistenec = Pojistenec(jmeno, prijmeni, vek, telefon)
            self.spravce.pridat_pojistence(pojistenec)
            print("Pojištěný přidán.")
        else:
            print(f"Pojištěný nebyl přidán kvůli chybám v zadání: {chybova_zprava}")

    def zobrazit_vsechny_pojistence(self):
        print("Seznam všech pojištěných:")
        self.spravce.zobrazit_pojistence()

    def vyhledat_pojistence(self):
        jmeno, prijmeni = self.zadat_jmeno_a_prijmeni()
        pojistenec = self.spravce.najit_pojistence(jmeno, prijmeni)
        if pojistenec:
            print("Nalezený pojištěný:")
            print(pojistenec)
        else:
            print("Pojištěný nenalezen.")

    def spustit(self):
        konec = False
        while not konec:
            print("\nEvidence pojištěných")
            print("1. Přidat pojištěného")
            print("2. Zobrazit všechny pojištěné")
            print("3. Vyhledat pojištěného")
            print("4. Konec")

            volba = input("Vyberte akci: ").strip()

            if volba == "1":
                self.pridat_pojistence()
            elif volba == "2":
                self.zobrazit_vsechny_pojistence()
            elif volba == "3":
                self.vyhledat_pojistence()
            elif volba == "4":
                print("Konec.")
                konec = True
            else:
                print("Neplatná volba, zkuste to znovu.")

if __name__ == "__main__":
    ui = UzivatelskeRozhrani()
    ui.spustit()