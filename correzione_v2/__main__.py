class WrongArgException(Exception):
    def __init__(self):
        self.message = "L'argomento inserito non è valido. Riprova!"

    def __str__(self):
        return self.message

if __name__ == "__main__":
    import sys
    from ex3 import esegui_ex3
    from ex4 import esegui_ex4
    from ex5 import esegui_ex5
    from bonus import esegui_bonus

    if len(sys.argv) != 2:
        raise WrongArgException

    try:
        ex_num = int(sys.argv[1])
    except TypeError:
        raise WrongArgException

    if ex_num == 3:
        print(esegui_ex3())
    elif ex_num == 4:
        print(esegui_ex4())
    elif ex_num == 5:
        print(esegui_ex5())
    elif ex_num == 6:
        print(esegui_bonus())
    else:
        raise WrongArgException