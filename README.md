# evidence-pojistencu

Evidence Pojištěnců
Popis projektu
Tento projekt slouží k evidenci pojištěnců. Umožňuje přidávat nové pojištěnce, zobrazovat seznam všech pojištěnců a vyhledávat konkrétní pojištěnce podle jména a příjmení. Projekt je napsán v jazyce Python a využívá jednoduché uživatelské rozhraní pro interakci s uživatelem.

Struktura projektu
main.py: Hlavní soubor, který obsahuje třídu UzivatelskeRozhrani zajišťující interakci s uživatelem. Tento skript umožňuje přidávat pojištěnce, zobrazovat všechny pojištěnce a vyhledávat pojištěnce podle jména a příjmení.
pojistenec.py: Tento soubor obsahuje definici třídy Pojistenec, která reprezentuje jednotlivého pojištěnce. Třída obsahuje atributy jako jméno, příjmení, věk a telefonní číslo.
spravce_pojistencu.py: Tento soubor obsahuje třídu SpravcePojistencu, která spravuje seznam pojištěnců. Zajišťuje přidávání, zobrazování a vyhledávání pojištěnců a také validaci vstupních dat.
Instalace a spuštění
Požadavky
Python 3.x
Instalace
Klonujte repozitář:
bash
Zkopírovat kód
git clone https://github.com/uzivatel/evidence-pojistencu.git
Přejděte do adresáře projektu:
bash
Zkopírovat kód
cd evidence-pojistencu
Spuštění programu
Program spustíte následujícím příkazem:

bash
Zkopírovat kód
python main.py
Použití
Po spuštění programu budete mít k dispozici následující volby:

Přidat pojištěného: Přidá nového pojištěnce do evidence. Budete vyzváni k zadání jména, příjmení, věku a telefonního čísla.
Zobrazit všechny pojištěné: Zobrazí seznam všech evidovaných pojištěnců.
Vyhledat pojištěného: Umožňuje vyhledat konkrétního pojištěnce podle jména a příjmení.
Konec: Ukončí program.
Stručný popis tříd
Pojistenec
Reprezentuje pojištěnce se základními údaji:

jmeno: křestní jméno pojištěnce
prijmeni: příjmení pojištěnce
vek: věk pojištěnce
telefonni_cislo: telefonní číslo pojištěnce
SpravcePojistencu
Spravuje seznam pojištěnců a poskytuje metody pro:

Přidání nového pojištěnce
Zobrazení všech pojištěnců
Vyhledání pojištěnce podle jména a příjmení
Validaci vstupních údajů
UzivatelskeRozhrani
Zajišťuje interakci s uživatelem prostřednictvím konzole. Obsahuje metody pro:

Přidání pojištěnce
Zobrazení všech pojištěnců
Vyhledání pojištěnce
Řízení hlavního menu programu
Tento README by měl uživatelům poskytnout všechny potřebné informace k instalaci, spuštění a používání projektu.
