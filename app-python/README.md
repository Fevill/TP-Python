# APP Python

Menu()
afficher le choix entre les différentes fonctionnalités
L'utilisateur entre un numéro pour sélectionner la fonctionnalité
Le menu appelle la fonction correspondant au choix

listerMachines()
Affiche le contenu du fichier quand appelée depuis le main()

ajoutMachine()
Demande à l'utilisateur le nom
Demande à l'utilisateur l'IP
Demande à l'utilisateur le nombre de CPU
Demande à l'utilisateur la quantité de RAM
Demande à l'utilisateur le nombre de disques
	Pour chaque disque : demande la taille du disque
Demande à l'utilisateur l'OS et sa version
Pour chaque ligne, modifie la propriété de l'objet en conséquence
Ecrit l'objet dans le JSON

listerMachineParHostname()
Demande à l'utilisateur le nom
Lit les propriétés dans le JSON
Affiche les propriétés

modifMachine()
Demande à l'utilisateur le nom
Lit les propriétés dans le JSON
Affiche les propriétés
Affiche un menu de choix pour demander quelle propriété modifier
Demande d'entrer une option
	En fonction de l'option, demande la nouvelle valeur de propriété
	Demande si la modification est terminée
		Si oui :
			écrit le fichier
		Si non :
			revient au menu de choix

supprimerMachine()
Demande le nom de la machine à supprimer
Supprime les entrées de la machine dans le fichier

listerApplications()
Fait un appel à l'URL de l'API
Récupère le résultat dans une variable
Affiche les propriétés récupérées
