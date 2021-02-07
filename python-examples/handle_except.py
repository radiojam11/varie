class SoloIntException(Exception):
    def __init__(self):
        self.message = "VOLEVO UN INT!"


def funzione_stupida(parametro_int):
    if not isinstance(parametro_int, int):
        raise SoloIntException()
    return "ok"