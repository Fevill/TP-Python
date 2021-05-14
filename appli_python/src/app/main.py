#####PROGRAMME PRINCIPAL######
############################
#   Tcherno 11/05/2021     #
#   menu principal         #
#   Version : beta         #
############################
import json
import os

machines =[];
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(THIS_FOLDER, '../asset/inventaire.json')

#####FONCTIONS######

## Supprimer une machine
def supprimerUneMachine():
    chx=0
    trouve=False
    contenuJSON = open(FILE_PATH, 'r').read()    #lit le contenu du JSON
    machinesObj = json.loads(contenuJSON)       #crée un objet contenant tout le JSON

    nom=input("Entrer le nom de la machine : ")
    for i in range(len(machinesObj['machines'])): #==> récupère le tableau 'machines' dans le JSON (parmi tout ce qu'il y a dans le fichier)
        if machinesObj['machines'][i]['hostname'] == nom: #Si on trouve la machine saisie
            trouve=True
            break
    if trouve == True:
        del machinesObj['machines'][i]      #Supprime la machine à l'itération "i"
        with open(FILE_PATH, 'w') as outfile:   #Ecrit le fichier
            json.dump(machinesObj, outfile)
    else:
        print("Saisie invalide\n")


##  Modifier une machine 
def modifierUneMachine():
    chx=0
    trouve=False
    contenuJSON = open(FILE_PATH, 'r').read()    #lit le contenu du JSON
    machinesObj = json.loads(contenuJSON)       #crée un objet contenant tout le JSON
    
    nom=input("Entrer le nom de la machine : ")    
    for i in range(len(machinesObj['machines'])): #==> récupère le tableau 'machines' dans le JSON (parmi tout ce qu'il y a dans le fichier)
        if machinesObj['machines'][i]['hostname'] == nom: #Si on trouve l'occurence
            trouve=True
            break
    if trouve == True:
        print(machinesObj['machines'][i])  #Affiche les propriétés de la machine à trouvée à l'itération "i"
        while(chx != "N" and chx != "n"):   #tant que l'utilisateur veut continuer
            trouve=False
            print("Choisir l\'element a modifier : \n1 - Nom\n2 - adresse IP\n3 - Nombre de CPU\n4 - Taille de la RAM totale\n5 - Nombre de disques durs\n6 - Taille des disques durs\n7 - Infos OS\n")
            chx=input("Choisir une commande (1,2 ou 3...): ")
            if (chx == "1"):
                machinesObj['machines'][i]['hostname'] = input("Entrer un nouveau nom pour la machine : ")  #affecte la saisie directement au champ du JSON concerné (ici le nom)
            elif (chx == "2"):
                machinesObj['machines'][i]['ip'] = input("Entrer une nouvelle IP pour la machine : ")
            elif (chx == "3"):
                machinesObj['machines'][i]['nbCPU'] = input("Entrer un nouveau nombre de CPU pour la machine : ")
            elif (chx == "4"):
                machinesObj['machines'][i]['tailleRAM'] = input("Entrer un nouvelle taille de RAM pour la machine : ")
            elif (chx == "5"):
                machinesObj['machines'][i]['nbHDD'] = input("Entrer un nouveau nombre de disques durs pour la machine : ")
            elif (chx == "6"):
                trouve=False
                chx=input("Choisir le disque a modifier : ")
                allHDD = machinesObj['machines'][i]['allHDD'] #==> récupère le contenu de la case allHDD dans un objet depuis le tableau 'machines'
                for j in range(len(allHDD)):
                    if allHDD[j]['numHDD'] == chx:  #Si on trouve le numéro de disque saisi
                        trouve=True
                        break
                if trouve == True:
                    allHDD[j]['espHDD'] = input("Entrer un nouvelle taille pour le disque : ") #saisir une nouvelle taille au disque trouvé au disque à l'itération "j"
                else:
                    print("Saisie invalide\n")
            elif (chx == "7"):
                machinesObj['machines'][i]['os'] = input("Entrer les nouvelles infos de l\'OS pour la machine : ")
            else:
                print("Saisie invalide\n")
            chx=input("Modifier un autre parametres ? (O/N) : ")
        with open(FILE_PATH, 'w') as outfile:       #Ecrit le nouvelle inventaire
            json.dump(machinesObj, outfile)
    else:
        print("Saisie invalide\n")



## Lister les machines
def listerLesmachine():
    print("")
    print("\tListe de toutes les machines")
    print("\t----------------------------")
    data = open(FILE_PATH, 'r').read()
    dataObject = json.loads(data)
    #print(dataObject['machines'][1]) 
    for m in dataObject['machines']:
        newM = Machine(m)
        machines.append(newM)

    for m in machines:
        print(m) 

## Detail d'une machine
def detailMachine():
    
    print("")
    print("\tDétail de la machine ")
    print("\t----------------------")
    hostname = input("Entrer hostname de la machine :")
    for m in machines:
        if(m.hostname==hostname):
            print(m)
            return m
    pass

## Sauvegarde de données
def sauvegarderLesDonnees():

    machinesToSave=[]
    for m in machines:
        newM = m.toDict()
        machinesToSave.append(newM)
    data = {'machines' : machinesToSave}
    with open(FILE_PATH, 'w') as outfile:
        json.dump(data, outfile)

## Ajouter une machine
def ajouterUneMachine():

    machine:Machine = Machine(None)
    machine.hostname = input("1/7 - Entrer Hostname : ")
    machine.ip= input("2/7 - Entrer Ip : ")
    machine.nombreDeCpu = input("3/7 - Entrer NombreDeCpu :")
    machine.tailleDeLaRam = input("4/7 - Entrer TailleDeLaRam :")
    machine.nombreEtTaille = input("5/7 - Entrer NombreEtTaille :")
    machine.osEtversion = input("6/7 - Entrer OsEtversion :")

    # Persistance
    ON=True
    while ON :
        ouiNon = input("7/7 - Voullez-vous sauvegarder ? (Y ou N) ")
        if (ouiNon=="Y"):
           # Sauvegarde dans la mémoire
            machines.append(machine)
            sauvegarderLesDonnees()
            print("7/7 - Données sauvegarder")
            ON=False
        elif (ouiNon=="N"):
            print("7/7 - Sauvegarde annuler")
            ON=False

## Ajouter une application
def ajouterUneApplication():
    print("Ajouter une application ...")
    pass

## Lister les applications
def listerLesApplications():
    print("Lister les applications ...")
    pass




#####CLASSE MACHINE#####
class Machine :

    #Les variables
    hostname=""
    ip=""
    nbCPU=""
    tailleRAM=""
    nbHDD= ""
    allHDD=""
    os=""

    def __init__(self,machine) -> None:
        if machine is not None :
            self.hostname= (machine["hostname"], "")[machine['hostname'] is None]
            self.ip=(machine['ip'], "")[machine['ip'] is None]
            self.nbCPU=(machine['nbCPU'], "")[machine['nbCPU'] is None]
            self.nbHDD=(machine['nbHDD'], "")[machine['nbHDD'] is None]
            self.allHDD=(machine['allHDD'], "")[machine['allHDD'] is None]
            self.tailleRAM=(machine['tailleRAM'], "")[machine['tailleRAM'] is None]
            self.os=(machine['os'], "")[machine['os'] is None]
    
    def toDict(self):
        smachine={}
        smachine["hostname"]=self.hostname
        smachine['ip']=self.ip
        smachine['nbCPU']=self.nbCPU
        smachine['nbHDD']=self.nbHDD
        smachine['allHDD']=self.allHDD
        smachine['tailleRAM']=self.tailleRAM
        smachine['os']=self.os
        return smachine


    # Afficher une machine
    def __str__(self) -> str:
        return "\tHostname : "+self.hostname+"\n\tIP : "+self.ip+"\n\tnbCPU : "+self.nbCPU+"\n\ttailleRAM : "+self.tailleRAM+"\n\tnbHDD : "+self.nbHDD+"\n\tOs : "+self.os+"\n"

#### Main ####
## Menu
chx=0
while (chx != "q"):     #tant qu'on ne quitte pas
    print("*****MENU PRINCIPAL*****")
    print("Programme d\'inventaire des machines et des applications\nChoix des commandes :\n1 - Lister toutes les machines\n2 - Ajouter une machine\n3 - Lire une machine specifique (par nom)\n4 - Modifier une enregistrement (par nom)\n5 - Supprimer un enregistrement (par nom)\n6 - Lister les applis disponibles sur le depot\n7 - Ajouter une appli\n")
    print('Entrer "q" pour quiter\n')
    chx=input("Choisir une commande (1,2 ou 3...): ")
    #Appelle la fonction la fonction correspondant au choix saisi
    if (chx == "1"):
        listerLesmachine()
    elif (chx == "2"):
        ajouterUneMachine()
    elif (chx == "3"):
        detailMachine()
    elif (chx == "4"):
        modifierUneMachine()
    elif (chx == "5"):
        supprimerUneMachine()
    elif (chx == "6"):
        listerLesApplications()
    elif (chx == "7"):
        ajouterUneApplication()
    elif (chx == "q"):  #quitte le programme
        quit()
    else:
        print("Saisie invalide\n")


