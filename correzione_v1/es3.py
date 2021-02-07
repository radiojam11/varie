def esegui_es3():
    d = {}
    str_in = input(
        "Inserisci una lista di parole del tipo `parola:parola`, separate da spazio:\n"
    )
    for couple in str_in.split():
        k, v = couple.split(":")
        d[k] = v
    return d
