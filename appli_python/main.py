#####PROGRAMME PRINCIPAL######

############################
#   Tcherno 11/05/2021     #
#   menu principal         #
#   Version : beta         #
############################
import json


#####FONCTIONS######
def supprimerUneMachine():
    chx=0
    trouve=False
    contenuJSON = open('inventaire.json', 'r').read()    #lit le contenu du JSON
    machinesObj = json.loads(contenuJSON)       #crée un objet contenant tout le JSON

    nom=input("Entrer le nom de la machine : ")
    for i in range(len(machinesObj['machines'])): #==> récupère le tableau 'machines' dans le JSON (parmi tout ce qu'il y a dans le fichier)
        if machinesObj['machines'][i]['hostname'] == nom: #Si on trouve la machine saisie
            trouve=True
            break
    if trouve == True:
        del machinesObj['machines'][i]      #Supprime la machine à l'itération "i"
        with open('inventaire.json', 'w') as outfile:   #Ecrit le fichier
            json.dump(machinesObj, outfile)
    else:
        print("Saisie invalide\n")

def modifierUneMachine():
    chx=0
    trouve=False
    contenuJSON = open('inventaire.json', 'r').read()    #lit le contenu du JSON
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
        with open('inventaire.json', 'w') as outfile:       #Ecrit le nouvelle inventaire
            json.dump(machinesObj, outfile)
    else:
        print("Saisie invalide\n")

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