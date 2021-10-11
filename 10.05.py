'''
Ja ir jau dota cena
'''
#1 kg
āboli = 1.50
cukurs = 0.80
garšvielas = 3.50

#Ja receptē ir nepieciešams 3 kg ābolu, 2 kg cukura un 1 kg garšvielu
recepte = [3,2,1]
#Produktu summa (daudzums)
sum1 = sum(recepte)
print("Ievārījuma receptē ir nepiecišami", sum1, "ingredienti.")
#Produktu summa (cena)
cena = 1.50+1.50+1.50+0.80+0.80+3.50
print("Ingredienti maksās", cena, "eiro.")



'''
Ja cenu vajag ievadīt pašam
'''
a = int(input("Ābolu skaits kg: "))
c = int(input("Cukura skaits kg: "))
g = int(input("Garšvielu skaits kg: "))
sum1 = a+c+g
print("Receptē būs nepieciešams", sum1, "kg produktu.", end = "\n\n")

a_c = float(input("Ābolu cena: "))
c_c = float(input("Cukura cena: "))
g_c = float(input("Garšvielu cena: "))
sum2 = a_c*a+c_c*c+g_c*g
print("Ievārījums maksās:", sum2, "eiro.")



'''
Skolotājas metode
'''
#Izmantot bibliotēkas
recepte1 = {"cukurs":2.65, "kanēlis":0.43, "āboli":5.50, "ūdens":5.40}
cenas1 = {"cukurs":1.50, "kanēlis":2.15, "āboli":3.00, "ūdens":0.40}

def izmaksas_receptei(recepte,cenas):

  summa=0
  for sastāvdaļa in recepte:
    daudzums = recepte[sastāvdaļa]
  summa = daudzums*cenas[sastāvdaļa]
  return summa

def izmaksas_receptei(abolu_svars, recepte, cena):
  izmaksas_kg=izmaksas_receptei(recepte, cenas)
  recepte['āboli']

  ievarijuma_izmaksas = abolu_svars + izmaksas_kg

  return ievarijuma_izmaksas

  print(izmaksas_kopa(15.0, recepte1, cenas1))