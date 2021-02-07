from random import *
from pickle import *

seed()

try:
    f = open("records.dat", "rb")     # apre il file "records.dat"
    record = load(f)                  # carica il record
    nome = load(f)                    # carica il nome del giocatore
    f.close()
except FileNotFoundError:
    record = 1000000000               # se il file non esiste inizializza come prima
    nome = ""
risp = "s"                            # da qui il programma prosegue come prima
while risp == "s":
    num = randrange(1, 21)
    tentativi = 0
    print ("Ho pensato un numero da 1 a 20. Prova ad indovinarlo!")
    mio_num = -1
    while mio_num != num:
        tentativi += 1
        mio_num = int(input("??? "))
        if mio_num < num:
            print("Troppo basso")
        elif mio_num > num:
            print("Troppo alto")
    print("Hai indovinato! Hai impiegato", tentativi, "tentativi")
    if tentativi < record:
        print("Hai battuto il record!")
        record = tentativi
        nome = input("Inserisci il tuo nome: ")
                                        # chiede anche il nome del giocatore
    risp = input("Vuoi giocare ancora (s/n)? ")
                                        # uscita dal programma
f = open("records.dat", "wb")           # riapre il file in scrittura ...
dump(record, f)                         # ... salva il record ...
dump(nome, f)                           # ... ed il nome
f.close()