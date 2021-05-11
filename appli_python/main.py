#####PROGRAMME PRINCIPAL######

chx=0
while (chx != "q"):
    print("*****MENU PRINCIPAL*****")
    print("Programme d\'inventaire des machines et des applications\nChoix des commandes :\n1 - Lister toutes les machines\n2 - Ajouter une machine\n3 - Lire une machine specifique (par nom)\n4 - Modifier une enregistrement (par nom)\n5 - Supprimer un enregistrement (par nom)\n6 - Lister les applis disponibles sur le depot\n7 - Ajouter une appli\n")
    print('Entrer "q" pour quiter\n')
    chx=input("Choisir une commande (1,2 ou 3...): ")
    
    if (chx == "1"):
        print("fonction listerLesmachine")
        #listerLesmachine()
    elif (chx == "2"):
        print("fonction ajouterUneMachine")
        #ajouterUneMachine()
    elif (chx == "3"):
        print("fonction detailMachine")
        #detailMachine()
    elif (chx == "4"):
        print("fonction modifierUneMachine")
        #modifierUneMachine()
    elif (chx == "5"):
        print("fonction supprimerUneMachine")
        #supprimerUneMachine()
    elif (chx == "6"):
        print("fonction listerLesApplications")
        #listerLesApplications()
    elif (chx == "7"):
        print("fonction ajouterUneApplication")
        #ajouterUneApplication()
    elif (chx == "q"):
        quit()
    else:
        print("Saisie invalide\n")