# 2) fare una funzione per il calcolo dell'area del trinagolo

def areaTriangolo(a,b):
  """questa funzione riceve una lista contenente, base ed altezza, lista[b,a] e
  calcola l'area di un triangolo e rende la soluzione come float area """
  area = b*a/2
  return area

def ricevi_dati():
  b = int(input("Dammi la lunghezza della base del trinagolo rettangolo  "))
  a = int(input("Dammi la lunghezza dell'altezza del triangolo "))
  lista = [a,b]
  return lista

#start main  
lista = ricevi_dati()
area = areaTriangolo(lista[0],lista[1])
print(area)
#print(f"L'area del tuo triangolo e' {area}")



