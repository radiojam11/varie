def esegui_ex4():
    str_in1 = input("Inserisci una lista N numeri separati da virgola (es. 1,2,3,4):\n")
    str_in2 = input("Inserisci una lista N parole separate da virgola (es. pippo,pluto,paperino,topolino):\n")
    lista_numeri = str_in1.split(",")
    lista_parole = str_in2.split(",")
    lista = []
    for parola, numero in zip(lista_parole, lista_numeri):
        numero = int(numero)
        stringa = ""
        for i in range(numero):
            stringa += parola
            if i == numero - 1:
                continue
            stringa += "|"
        # elemento = [parola] * numero
        # lista.append("|".join(elemento))
        lista.append(stringa)
    return lista