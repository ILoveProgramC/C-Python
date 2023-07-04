from ctypes import *
# import os    --> Ako koristimo drugi nacin za odredjivanje putanje potrebno je importovati


#Prvi nacin definisanja putanje:
so_file = "/Users/PutanjaDoDatoteke/C pokrenut u Pajtonu/C-program.so" #definiste svoju putanju na vasem racunaru
osnovna_funkcija = CDLL(so_file)

#Drugi nacin definisanja putanje: 
"""
trenutna_putanja = os.path.abspath(os.path.dirname(__file__))
putanja_do_izvrsne_datoteke = os.path.join(trenutna_putanja, 'C-program.so')
osnovna_funkcija = CDLL(putanja_do_izvrsne_datoteke)
"""

print("Tip: ",type(osnovna_funkcija))
osnovna_funkcija.ispis() # ispis na standardnom izlazu
print("Funkcija kvadrat: ", osnovna_funkcija.kvadrat(5)) #s obzirom da je u pitanju funkcija u C-u koja jednostavno vraca
#kvadrat broja koji navedemo u argumentu, rezultat ce biti prikazan u Python/u u tipu podatka int
#Ne smijemo koristiti realan broj jer u C funkciji se koristi podatak tipa int

osnovna_funkcija.unos()  #Funkcija kojom se vrsi unos sa tastature i ispis

osnovna_funkcija.main() #Glavna funkcija u C-u, u njoj sam ubacio kreiranje tekstualne datoteke.


