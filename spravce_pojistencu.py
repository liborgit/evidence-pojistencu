class SpravcePojistencu:
    def __init__(self):
        self.pojistenci = []  # Seznam pojištěných

    def pridat_pojistence(self, pojistenec):
        self.pojistenci.append(pojistenec)

    def zobrazit_pojistence(self):
        if not self.pojistenci:
            print("Žádní pojištění.")
        else:
            for pojistenec in self.pojistenci:
                print(pojistenec)

    def najit_pojistence(self, jmeno, prijmeni):
        for pojistenec in self.pojistenci:
            if pojistenec.jmeno == jmeno and pojistenec.prijmeni == prijmeni:
                return pojistenec
        return None

    def validovat(self, jmeno, prijmeni, vek, telefon):
        if not jmeno or not prijmeni:
            return False, "Jméno a příjmení musí být vyplněny."
        if not isinstance(vek, int) or vek <= 0:
            return False, "Věk musí být uveden ve správném formátu (pouze kladné číslo)."
        if not telefon.isdigit():
            return False, "Uveďte telefonní číslo ve správném formátu (pouze číslo, bez mezer)."
        return True, None  # V případě úspěšné validace