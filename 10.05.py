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