# i moduli sono i file che contengono le classi o anche le funzioni (vedi multiplying)
from rocket import Rocket, Shuttle
from multiplaying import funzione1

funzione1(44)

rocket = Rocket(11,22, n="Razzo_1")
print("The rocket %s in at (%d, %d)." % (rocket.name, rocket.x, rocket.y))

shuttle = Shuttle(22,33,n="ShuttleX11")
print("\nThe Shuttle %s is at (%d, %d)" % (shuttle.name, shuttle.x, shuttle.y ))


