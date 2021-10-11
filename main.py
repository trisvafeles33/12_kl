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