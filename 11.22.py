klients = input('Ievadi savu vārdu un uzvārdu: ')
veltijums = input('Uzraksti savu veltījumu: ')
izmers = input('Lādītes izmēri:\n platums, garums, augstums\n Raksti veselus skaitļus un atdali tos ar komatu: ')
materials = input('Ieraksti materiāla cenu EUR/m^2: ')


class Rekins:
    def __init__(self,klients,veltijums,izmers,materials):

      self.klients = klients
      self.veltijums = veltijums
      self.izmers = izmers
      self.materials = materials

      self.veltijuma_gar = len(self.veltijums)


    
    def izdrukat(self):
      pass

    def aprekins(self):
      darba_samaksa = 15
      PVN = 21
      produkta_cena = (self.veltijuma_gar) * 1.2 + (platums/100 * garums/100 * augstums/100)/ 3 * materiala_cena
      PVN_summa = (produkta_cena + darba_samaksa)*PVN/100
      rekina_summa = (produkta_cena + darba_samaksa) + PVN_summa

a = Rekins(klients,veltijums,izmers,materials)

print(a.veltijuma_gar)