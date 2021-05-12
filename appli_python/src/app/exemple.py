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