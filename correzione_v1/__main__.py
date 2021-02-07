class WrongArgException(Exception):
    def __init__(self):
        self.message = "Il numero dell'esercizio inserito non è valido. Riprova."

    def __str__(self):
        return self.message


if __name__ == "__main__":
    import sys
    from es3 import esegui_es3
    from es4 import esegui_es4
    from es5 import esegui_es5
    from bonus import esegui_bonus

    if len(sys.argv) != 2:
        raise WrongArgException

    try:
        es_num = int(sys.argv[1])
    except TypeError:
        raise WrongArgException

    if es_num == 3:
        print(esegui_es3())
    elif es_num == 4:
        print(esegui_es4())
    elif es_num == 5:
        print(esegui_es5())
    elif es_num == 6:
        print(esegui_bonus())
    else:
        raise WrongArgException
