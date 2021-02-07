def esegui_ex5():
    str_in = input("Inserisci una insieme di caratteri (es. abacadabra):\n")
    unici = set(str_in)
    print(unici)
    lista = []
    # abcdr
    # ab ac ad ar
    # ba bc bd br
    # ca cb cd cr
    # ...
    for c1 in unici:
        for c2 in unici:
            if c1 == c2:
                continue
            lista.append(c1 + c2)
    return lista