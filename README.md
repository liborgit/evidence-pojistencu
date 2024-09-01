# Evidence Pojištěnců

## Popis projektu
Tento projekt slouží k evidenci pojištěnců. Umožňuje přidávat nové pojištěnce, zobrazovat seznam všech pojištěnců a vyhledávat konkrétní pojištěnce podle jména a příjmení. Projekt je napsán v jazyce Python a využívá jednoduché uživatelské rozhraní pro interakci s uživatelem.

## Struktura projektu

- **`main.py`**: Hlavní soubor, který obsahuje třídu `UzivatelskeRozhrani` zajišťující interakci s uživatelem. Tento skript umožňuje přidávat pojištěnce, zobrazovat všechny pojištěnce a vyhledávat pojištěnce podle jména a příjmení.
- **`pojistenec.py`**: Tento soubor obsahuje definici třídy `Pojistenec`, která reprezentuje jednotlivého pojištěnce. Třída obsahuje atributy jako jméno, příjmení, věk a telefonní číslo.
- **`spravce_pojistencu.py`**: Tento soubor obsahuje třídu `SpravcePojistencu`, která spravuje seznam pojištěnců. Zajišťuje přidávání, zobrazování a vyhledávání pojištěnců a také validaci vstupních dat.

## Instalace a spuštění

### Požadavky
- Python 3.x

### Instalace
1. **Klonujte repozitář**:
    ```bash
    git clone https://github.com/uzivatel/evidence-pojistencu.git
    ```
2. **Přejděte do adresáře projektu**:
    ```bash
    cd evidence-pojistencu
    ```

### Spuštění programu
Program spustíte následujícím příkazem:
```bash
python main.py
