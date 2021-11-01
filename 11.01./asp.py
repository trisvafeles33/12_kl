import random

while True:
  print("Akmens, šķēres, papīrīts - aiziet.")
  izveele = input("Izvēlies - akmens(A), šķēres(S) vai papīrs(P):")
  print("Tu izvēlējies " + izveele)

  defizveeles = ['A','S','P']
  pretizveele = random.choice(defizveeles)
  print("Es izvēlējos " + pretizveele)

  if pretizveele == izveele:
    print("Neizšķirts.")
  elif izveele == "A":
    if pretizveele == "S":
      print("Akmens sasita šķēres. Tu uzvarēji!")
    else:
      print("Papīrs aizklāja akmeni. Tu zaudēji.")
  elif izveele == "P":
    if pretizveele == "S":
      print("Šķēres sagrieza papīru. Tu zaudēji.")
    else:
      print("Papīrs aizklāja akmeni. Tu uzvarēji!")
  elif izveele == "S":
    if pretizveele == "A":
      print("Akmens sasita šķēres. Tu zaudēji.")
    else:
      print("Šķēres sagrieza papīru. Tu uzvarēji!")