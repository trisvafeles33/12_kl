"""
Katrīna Ogņennaja
27.09.2021.
"""
#Cikli
saraksts = [1,2,3,4,5,6,7,8,9,10]
for cipari in saraksts:
  print(cipari)

for cipari in saraksts:
  if cipari %2 == 0:
    print(cipari)

for cipari in saraksts:
  if cipari %2 == 0:
    print(cipari)
  else:
    print('Nepāra skaitlis')

saraksts2 = ['suns','kaķis','varde']
for dzīvnieki in saraksts2:
  print('Mans mīļākais dzīvnieks ir', dzīvnieki)

for cipari in range(1,2,3):
  print(cipari)