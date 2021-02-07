def write_wiki_juve_with_urlopen():
    """ 
    Scarica la pagina di Wikipedia dedicata alla Juventus F.C. 
    in HTML e salva su file.
    
    Riferimento a docs per eseguire richieste web
    https://docs.python.org/3.8/howto/urllib2.html 
    
    """
    from urllib.request import urlopen
    req = urlopen("https://en.wikipedia.org/wiki/Juventus_F.C.")
    # riferimento a docs per gestire lettura e scrittura su file
    # https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
    fd = open("wiki_juve_urlopen.html", "w+")
    html_bytes = req.read()
    # riferimento a docs per la funzione `decode`
    # https://docs.python.org/3/library/stdtypes.html#bytes.decode
    html_text = html_bytes.decode()
    fd.write(html_text)


def call_function_with_exception(param):
    """
    Una semplice funzione che implementa la gestione di eccezioni
    """
    import handle_except

    try:
        handle_except.funzione_stupida(param)

    except handle_except.SoloIntException as err:
        print(f"`funzione_stupida` con parametro `{param}` è fallita con errore:\n\t", err.message)
        print("Riproviamo a chiamarla con parametro intero: 10")
        call_function_with_exception(10)

    else:
        print(f"Siamo dentro all'else, parametro `{param}`")
    
    finally:
        print(f"Siamo dentro al finally, parametro `{param}`")


def write_wiki_juve_with_requests():
    """ 
    Scarica la pagina di Wikipedia dedicata alla Juventus F.C. 
    in HTML, usando il pacchetto esterno `requests`, e salva su file.
    
    Riferimento a requests
    https://requests.readthedocs.io/ 
    
    """
    import requests
    resp = requests.get("https://en.wikipedia.org/wiki/Juventus_F.C.")
    with open("wiki_juve_requests.html", "w+") as fd:
        fd.write(resp.text)


if __name__ == "__main__":
    from scraping import *
    from apiclient import *

    # download web page
    write_wiki_juve_with_urlopen()
    write_wiki_juve_with_requests()

    # webscraper
    for i in range(3):
        scrape_wiki_juve_links(i)

    # rest api client
    client_wikipedia_api()

    # exception
    call_function_with_exception("pippo")
