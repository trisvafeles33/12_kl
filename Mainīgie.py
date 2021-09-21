insect = "Bee"

print(insect)
print(insect[0:2])
print(insect[0], end = "\n\n")

print(insect)
print(insect, insect)
print(insect, end = " ")
print(insect, insect, end = "\n\n")

print(insect.upper())
print(insect.lower(), end = "\n\n")

print(insect[3::-1])
print(insect, end = "\n\n")

tree1 = "egle"
tree2 = "bērzs"
#string
print(f"Ārā pie celtnes aug {tree1} un {tree2}.")
#teksta un mainīgā savienošana
print("Ārā pie celtnes aug " + tree1 + " un " + tree2 + ".")
#.format
print("Ārā pie celtnes aug {0} un {1}." .format("egle", "bērzs"))
#%s
print("Ārā pie celtnes aug %s" %tree1, end = " ")
print("un %s." %tree2)