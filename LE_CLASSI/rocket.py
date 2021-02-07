from math import sqrt
class Rocket():
  def __init__(self, x=0, y=0, h=4, crew=5, n="Razzo Tipo", s=30):
    self.x = x
    self.y = y
    self.height = h
    self.name = n
    self.speed= s
    self.crew = crew
  def move_up(self):
    self.y += 1
  def move_rocket(self, x_increment=0,y_increment=0):
    self.x += x_increment
    self.y += y_increment

  def get_distance(self, rock):
    a = abs(self.x - rock.x)
    b = abs(self.y - rock.y)
    distance = sqrt(a**2+b**2)
    return distance
  def lunch(self):
    print( "IL Razzo e' partito.....!")
  def safety_check(self, rock):
    distance = self.get_distance(rock)
    if distance == 0:
      print("Danger!! CRASH")
    elif distance<2:
      print("Attenzione sei Troppo vicino a ", rock.name)
    else:
      print("Tutto bene volo sereno!")

  def land_rocket(self):
    self.y = 0
    self.x = 0


class Shuttle(Rocket):
  def __init__(self, x=0, y=0, h=4, crew=5, n="Razzo9 Tipo", s=30, flight_completed=0, issD=True):
    super().__init__(x, y, h, crew, n, s)
    self.flight_completed = flight_completed
    self.issD=issD
  def dock_ISS(self):
    print("Docking with ISS!!")
  def tutto(self):
    print()
  def land_rocket(self):
    #qui riscrivo lo stesso metodo della classe super (overriding) con calcoli modificati come
    self.y = 0
    self.x = 0
    self.flight_completed += 1
    print("Shuttle landed")
