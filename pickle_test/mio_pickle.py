from pickle import *



try:
    f = open("miofile.dat", "rb")     # apre il file "records.dat"
    nome = load(f)                  # carica il nome
    cognome = load(f)                    # carica il cognome 
    f.close()
except FileNotFoundError:
    nome = "Aristide"              # se il file non esiste inizializza come prima
    cognome = "Ponchielli"
print(nome, cognome)
nome = ["Mario", "Beppe"]
cognome = "Verzicoli"
f = open("miofile.dat", "wb")           # riapre il file in scrittura ...
dump(nome, f)                         # ... salva il nome
dump(cognome, f)                           # ... ed il cognome
f.close()