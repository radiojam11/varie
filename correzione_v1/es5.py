def esegui_es5():
    unique_chars = set(input("Inserisci una lista di caratteri (es. abacadabra):\n"))
    return [
        "".join([el1, el2])
        for el1 in unique_chars
        for el2 in unique_chars
        if el1 != el2
    ]
