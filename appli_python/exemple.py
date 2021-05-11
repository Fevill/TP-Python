import json
data = open('inventory.json', 'r').read()
dataObject = json.loads(data)
machines = dataObject['machines']
print(machines)
#print(machines[index]) pour en avoir une en particulier

for i in range(len(machines)):
    if machines[i]['hostname'] == 'pc1.lab':
        print(machines[i]['os'])
        
        #==> pour lister les machines par hostname
with open('inventory.json', 'w') as outfile:
    json.dump(dataObject, outfile) #==> permet d'écrire le fichier
    
    import json
data = open('test.json', 'r').read()
dataObject = json.loads(data)
machines = dataObject['machines']

for i in range(len(machines)):
    if machines[i]['hostname'] == 'SRVINFRA12':
        allHDD = machines[i]['allHDD']
        for j in range(len(allHDD)):
            if allHDD[j]['numHDD'] == '2':
                allHDD[j]['espHDD'] = '180'
        print(allHDD)

#autre façon de faire, en agissant direct sur l'objet JSON :
import json
data = open('test.json', 'r').read()
machinesObj = json.loads(data)

for i in range(len(machinesObj['machines'])): #==> récupère le tableau 'machines' dans le JSON (parmi tout ce qu'il y a dans le fichier)
    if machinesObj['machines'][i]['hostname'] == 'SRVINFRA12':
        allHDD = machinesObj['machines'][i]['allHDD'] #==> récupère le contenu de la case allHDD dans un objet depuis le tableau 'machines'
        for j in range(len(allHDD)):
            if allHDD[j]['numHDD'] == '2':
                allHDD[j]['espHDD'] = '180'
        print(allHDD)
