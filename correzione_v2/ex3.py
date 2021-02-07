def esegui_ex3():
    str_in = input("Inserisci una lista di coppie del tipo `parola:parola` separate da spazio (es. pippo:franco topolino:paperino):\n")
    dizionario = {}
    # pippo:franco topolino:paperino
    # ["pippo:franco", "topolino:paperino"]
    coppie = str_in.split(" ")
    for coppia in coppie:
        elementi = coppia.split(":")
        chiave = elementi[0]
        valore = elementi[1]
        dizionario[chiave] = valore
    return dizionario