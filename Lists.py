#Mainīgais saraksts; definē ar []

my_list = [1,2,3]
print(my_list)

my_list = ['Teksts', 3, 2.5]
print(my_list)

#Funkcija len()

print("Mana saraksta mainīgo daudzums:", len(my_list))

#Index

print(my_list[0:2])

#Elementa maiņa

my_list[0] = "Saruna"
print(my_list)

#Elementa pievienošana

print(my_list + ['Sanāca'])
print(my_list)

my_list = my_list + ['Nesanāca']
print(my_list)

#Reizināšana

print(my_list *2)

#Append

my_list.append('Varbūt sanāca')
print(my_list)

#Pop

my_list.pop(0)
print(my_list)

#Parādīt .pop elementu

popped_item = my_list.pop()
print(popped_item)