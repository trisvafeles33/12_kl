'''
Uzrakstīt funkciju, kura atgriež vērtību true, ja abi dotie vārdi sākas ar vienu burtu

sakas_vienadi("Liela lama") ----> True
sakas_vienadi("Maza lama") ----> False
'''

#Metode, kuru atradu internetā
def sakas_vienadi(teksts):
    pirmais = teksts.split(" ")[0].lower()
    otrais = teksts.split(" ")[1].lower()
    if pirmais[0] == otrais[0]:
        return True
    else:
        return False

#Skolotājas metode
def sakas_vienadi(teksts):
  teksts = teksts.lower().split()

  return teksts[0][0] == teksts[1][0]



'''
Uzrakstīt funkciju, kura atgriež mazāko skaitli, ja abi skaitļi ir pāra skaitļi. Ja viens no skaitļiem vai abi skaitļi ir nepāra, tad funkcija atgriež lielāko skaitli.

atgriez_skaitli(2,4) ----> True
atgriez_skaitli(1,3) ----> False
'''

#Metode, kuru atradu internetā
def atgriez_skaitli(x):
  return x % 2 != 0
atgriez_skaitli(2)
True
atgriez_skaitli(1)
False

print(atgriez_skaitli(2))
print(atgriez_skaitli(1))

#Skolotājas metode
def atgriez_skaitli(a,b):
  if a % 2 = 0 and b % 2 = 0
   return min(a,b)
  else:
    return max(a,b)