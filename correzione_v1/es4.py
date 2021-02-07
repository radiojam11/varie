def esegui_es4():
    str_in1 = input(
        "Inserisci una lista di N numeri separati da virgola (es. 1,2,3,4):\n"
    )
    str_in2 = input(
        "Inserisci una lista di N parole separati da virgola (es. pippo,pluto,paperino,topolino):\n"
    )
    return [
        "|".join([el2] * int(el1))
        for el1, el2 in zip(str_in1.split(","), str_in2.split(","))
    ]
