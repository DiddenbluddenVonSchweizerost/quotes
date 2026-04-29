"""
Projekt 1: Personlig citatbank
Ett menybaserat program för att hantera citat med filhantering.
"""
import json
import random

def ladda_citat_fran_fil(filnamn):
    """
    Laddar citat från en textfil.
    
    Parametrar:
        filnamn (str): Namnet på filen att läsa från
    
    Returnerar:
        list: En lista med alla citat (varje rad är ett citat)
              Returnerar tom lista om filen inte finns.
    """
    f = open(filnamn, "r", encoding= "utf8")
    citat_dict = json.load(f)
    print(citat_dict)


def spara_citat_till_fil(citatlista, filnamn):
    """
    Sparar alla citat till en textfil.
    
    Parametrar:
        citatlista (list): Listan med citat som ska sparas
        filnamn (str): Namnet på filen att skriva till
    """

    # Tips: Använd open() med "w"
    # Tips: Loop'a igenom listan och skriv varje citat + "\n"
    pass


def visa_alla_citat(citatlista):
    """
    Skriver ut alla citat med numrering.
    
    Parametrar:
        citatlista (list): Listan med citat som ska visas
    """

    # Tips: Använd enumerate() för att få index
    # Tips: Använd strip() för att ta bort radbrytningar
    pass


def lagg_till_citat(citatlista):
    """
    Lägger till ett nytt citat i listan.
    Användaren får mata in citat och författare.
    
    Parametrar:
        citatlista (list): Listan som citatet ska läggas till i
    
    Returnerar:
        bool: True om citatet lades till, False annars
    """

    # Tips: Använd input() för att fråga efter citat och författare
    # Tips: Formatet bör vara "Citatet - Författare"
    pass


def slumpa_citat(citatlista):
    """
    Visar ett slumpmässigt citat från listan.
    
    Parametrar:
        citatlista (list): Listan att välja citat från
    """
  
    # Tips: Använd random.randint() eller random.choice()
    # Tips: Kontrollera att listan inte är tom först
    pass


def huvudprogram():
    """
    Huvudprogrammet som styr menyn och programflödet.
    """
    # 1. Ladda befintliga citat med ladda_citat_fran_fil()
    citat = ladda_citat_fran_fil("citatbank\data.json")
    print(citat[5]["person"])
    # 2. Skapa en while-loop som visar menyn
    # 3. Hantera användarens val med if/elif/else
    # 4. Vid val 2: lägg till citat och spara med spara_citat_till_fil()
    # 5. Vid val 4: avsluta loopen
    pass


# Starta programmet om filen körs direkt
if __name__ == "__main__":
    huvudprogram()