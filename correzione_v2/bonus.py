def esegui_bonus():
    from urllib.request import urlopen
    str_in = input("Inserisci una stringa qualsiasi:\n")
    resp = urlopen(f"https://github.com/search?q={str_in}")
    html = resp.read().decode()
    filename = f"{str_in}.html"
    with open(filename, "w+") as fd:
        fd.write(html)
    return filename