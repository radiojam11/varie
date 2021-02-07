from urllib.request import urlopen
# riferimento a docs per l'utilizzo di json
# https://docs.python.org/3/library/json.html?highlight=json#module-json
import json


def client_wikipedia_api():
    """
    Salva su file il risultato della chiamata alle API di Wikipedia 
    per la pagina dedicata alla Juventus F.C.

    """
    url_call = "https://en.wikipedia.org/w/api.php?action=query&prop=revisions&titles=Juventus_F.C.&rvprop=timestamp|user|comment|content&format=json"
    req = urlopen(url_call)
    json_text = req.read().decode()
    # trasforma il json stringa in oggetti python (list, dict, etc.)
    json_obj = json.loads(json_text)
    fd = open("wiki_juve.json", "w+")
    # salva l'oggetto python su file, con indentazione a 2
    json.dump(json_obj, fd, indent=2)