#####PROGRAMME PRINCIPAL######
import json
import pickle
import os

machines =[];
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(THIS_FOLDER, '../asset/exemple.json')

## Lister les machines
def listerMachine():

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
    print("Ajoute une application 121")
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
listerMachine()


