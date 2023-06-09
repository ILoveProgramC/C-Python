from ctypes import *
# import os       --> Ako koristimo drugi nacin za odredjivanje putanje potrebno je importovati
# import ctypes   --> Ako koristimo drugi nacin za odredjivanje putanje potrebno je importovati

so_file = "/Users/Stefan/Desktop/C pokrenut u Pajtonu/C-program.so" #definiste svoju putanju na vasem racunaru

#Drugi nacin definisanja putanje: 
"""
trenutna_putanja = os.path.abspath(os.path.dirname(__file__))
putanja_do_izvrsne_datoteke = os.path.join(trenutna_putanja, 'C-program.so')

osnovna_funkcija = ctypes.CDLL(putanja_do_izvrsne_datoteke)
"""

osnovna_funkcija= CDLL(so_file)
osnovna_funkcija.ispis.restype = None #posto je u pitanju void funkcija i ne vraca nikakav rezultat postavljena je vrijednost None
print("Tip: ",type(osnovna_funkcija))
print("Funkcija ispisa obicnog teksta: ",osnovna_funkcija.ispis()) # ispis na standardnom izlazu
print("Funkcija kvadrat: ", osnovna_funkcija.kvadrat(5)) #s obzirom da je u pitanju funkcija u C-u koja jednostavno vraca
#kvadrat broja koji navedemo u argumentu, rezultat ce biti prikazan u Python/u u tipu podatka int
#Ne smijemo koristiti realan broj jer u C funkciji se koristi podatak tipa int
osnovna_funkcija.unos()  #Funkcija kojom se vrsi unos sa tastature i ispis

