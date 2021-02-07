

import sys
import math
class Calcolatrice():
    """La Classe Calcolatrice() si aspetta tre dati NUM1  NUM2  e operatore (+ - * / Sqr Esp) e restituisce il risultato della operazione NUM1 operatore NUM2  """
    # dichiaro il tipo di dato che la classe si aspetta di ricevere
        
    primo_termine: float
    secondo_termine: float
    ultimo_risultato: float


    def __init__(self, primo_termine=None, secondo_termine=None, terzo_termine=None):
        """ Riceve il termini e li registra  """
        self.primo_termine = 0
        self.secondo_termine = 0
        self.ultimo_risultato = 0


    def cambia_primo_termine(self, nuovo_primo_termine):
        """  funzione che cambia il primo termine """
        self.primo_termine = nuovo_primo_termine

    def cambia_secondo_termine(self, nuovo_secondo_termine):
        """ funzione che cambia il secondo termine """
        self.secondo_termine = nuovo_secondo_termine

    def calcolo(self,operatore):
        """ funzione che esegue il calcolo in funzione dell operatore """
        if operatore == "+":
            self.ultimo_risultato = self.primo_termine+self.secondo_termine
        elif operatore == "-":
            self.ultimo_risultato = self.primo_termine-self.secondo_termine
        elif operatore == "/":
            self.ultimo_risultato = self.primo_termine/self.secondo_termine
        elif operatore == "*":
            self.ultimo_risultato = self.primo_termine*self.secondo_termine
        elif operatore == "Sqr":
            self.ultimo_risultato = self.primo_termine*(math.sqrt(self.secondo_termine))
        elif operatore == "Esp":
            self.ultimo_risultato = self.primo_termine**self.secondo_termine
        else:
            print("scegli un operatore giusto")


    def calcola(self,t1,t2,op):
        """ coordina le varie funzioni per effettuare il calcolo e rendere il risultato """
        self.cambia_primo_termine(t1)
        self.cambia_secondo_termine(t2)
        self.calcolo(op)




if __name__ == "__main__":
    #prende il valore dall'utente che digita  come parametri del file alla chiamata.
    # si aspetta  numero1 operatore numero2
    #rende ilrisultato come una calcolatrice
    


    #if sys.argv[1] == True:
    aa = Calcolatrice()

    #print(aa.primo_termine , aa.secondo_termine, aa.ultimo_risultato)

    # aa.cambia_primo_termine(10)
    # print(aa.primo_termine)

    # aa.cambia_secondo_termine(10)
    # print(aa.secondo_termine)

    # aa.calcola("+")
    # print(aa.ultimo_risultato)

    #aa.calcola(5,6,"*")
    aa.calcola(int(sys.argv[1]),int(sys.argv[3]),sys.argv[2])
    print(aa.ultimo_risultato)