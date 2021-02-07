#crea una specie di piccolo DB con ordinamento kiave - valore
import shelve
fav_cryptos = ["unalista di cose"]
fav_colors = ["una lista di colori"]
with shelve.open("test_shelf") as shelf:
    shelf['cryptos'] = fav_cryptos
    shelf['colors'] = fav_colors
#il sistema crea un file e lo salva sul disco con una estenzione che sceglie lui, a noi non interessa
#questo e' una specie di database che possiamo costruire noi come ci pare
