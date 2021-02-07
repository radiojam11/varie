from urllib.request import urlopen


__all__ = ["scrape_wiki_juve_links"]


def scrape_wiki_juve_links(mode=0):
    """
    Scarica la pagina HTML dedicata alla Juventus F.C. 
    e salva su file tutti i link che ha all'interno.

    Parameters
    ----------
    mode : int
        Seleziona la modalità di scraping:
            * 0 per utilizzare le regex;
            * 1 per utilizzare il primo approccio con la split;
            * 2 per utilizzare il secondo approccio con la split;
    """
    req = urlopen("https://en.wikipedia.org/wiki/Juventus_F.C.")
    html_text = req.read().decode()
    links = []
    if mode == 0:
        links = _scrape_links_with_regex(html_text)
    elif mode == 1:
        links = _scrape_links_with_split_v1(html_text)
    elif mode == 2:
        links = _scrape_links_with_split_v2(html_text)
    else:
        # riferimento a docs per il `raise` di una eccezione
        # https://docs.python.org/3/tutorial/errors.html?highlight=raise#raising-exceptions
        raise ValueError("La modalità di scraping inserita non è corretta")
    filename = f"wiki_juve_links_m{mode}.txt"
    fd = open(filename, "w+")
    links_as_text = "\n".join(links)
    fd.write(links_as_text)


def _scrape_links_with_regex(html):
    # riferimento a docs alle regex
    # https://docs.python.org/3/library/re.html
    import re
    pattern = re.compile(r'href="(.*?)"')
    links = pattern.findall(html)
    return links


def _scrape_links_with_split_v1(html):
    links = []
    links_raw = html.split("href=\"")
    for link in links_raw[1:]:
        l = link.split("\"")[0]
        links.append(l)
    return links


def _scrape_links_with_split_v2(html):
    links = []
    href = "href=\""
    links_raw = html.split("\n")
    for link in links_raw:
        index = link.find(href)
        if index == -1:
            continue
        start = index + len(href)
        stop = link.find("\"", start)
        links.append(link[start:stop])
    return links