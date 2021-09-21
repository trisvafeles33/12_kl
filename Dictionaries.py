#Mainīgais dictionaries jeb bibliotēkas; definē ar {}

pirmais = {'atsl1':'vērt1', 'atsl2':'vērt2'}
print(pirmais)

print(pirmais['atsl1'])

#Var glabāt dažādus datu tipus: string, numbers, lists, dictionaries.

otrais = {'atsl1':[1,2,3], 'atsl2':'vērt2'}
print(otrais)

trešais = {'atsl1':{'atsl2':[1,2,3]}}
print(trešais)

print(trešais['atsl1'])
print(trešais['atsl1']['atsl2'])
print(trešais['atsl1']['atsl2'][0])
print(trešais['atsl1']['atsl2'][1])
print(trešais['atsl1']['atsl2'][2])