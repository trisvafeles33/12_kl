#OOP jeb objektorientēta programmēšana

saraksts = [1,2,3]

print(type(saraksts))

#class
#self
#__str__


class Piem:   #Klases definē ar lielo burtu stila dēļ
  pass

a = Piem()

print(type(a))


class Car:
  def ___init__(self, model):
    self.model = model

ford = Car(model = "Focus")

opel = Car(model = "Astra")

print(ford.model)
print(opel.model)