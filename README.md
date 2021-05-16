# TP Python $$$

## Serveur Nexus

l'adresse IP : 192.168.0.12

### Instalation et configuration du serveur nexus

1. Se placer dans le dossier serveur-nexus
2. Effectuer vagrant up pour démarrer la machine
3. Effectuer vagrant ssh pour se connecter à la machine
4. Dans la machine se placer dans le répertoire /home/rsync
    - cd /home/rsync
5. Dans ce repertoire vous devez trouver le script nexusdeb.sh
    - sudo ./nexusdeb.sh
6. Une fois le mot "Success" affiché dans le terminal, vous pouvez acceder au serveur nexus depuis votre navigateur web (votre machine windows)
   à l'adresse localhost:5012
7. les identifiants : cat /opt/nexus/sonatype-work/nexus3/admin.password
    - user : admin
    - password: le mot de passe se trouve dans le fichier /opt/nexus/sonatype-work/nexus3/admin.password sur le serveur nexus 

## Serveur Jenkins

l'adresse IP : 192.168.0.11

### Instalation et configuration du serveur Jenkins

Pour initialiser la VM Jenkins :
Récupérer les fichiers Vagrantfile et install.sh du dossier.
Lancer la console gitbash dans l'emplacement des fichiers
lancer la commande vagrant up
Attendre la fin de l'installation
Supprimer ou renommer le fichier install.sh (il fout la merde si vous redémarrez la VM plus tard).

Si à la fin de l'installation, des erreurs concernant le lancement du service jenkins sont lisibles dans la console, se connecter avec \n
un vagrant ssh et taper la commande : type -p java, si elle ne renvoie rien, c'est que pour d'obscures raisons, les prérequis java ne \n
se sont pas installés, installez-les avec la commande : sudo apt -y install openjdk-11-jdk
Lancer le service : sudo systemctl start jenkins, vérifier qu'il est lancé : sudo systemctl status jenkins.
S'il n'est toujours pas lancé, tant pis, pas la peine de passer à la suite...

Si ça a marcher, se connecter sur 192.168.0.11:8080 doit vous amener sur la page de démarrage de Jenkins.
Lancer un sudo cat /var/lib/jenkins/secrets/initialAdminPassword pour avoir le mot de passe. (6702705af38043a894b558f1f42206dc)

finir la configuration installant les plugins de base, puis en créant un utilisateur admin.

Installer un webhook pour github :
Création de la tâche de build : (se déclenche à chaque màj du git, et lance le build gradle qui fait un zip du projet pour l'envoyer sur \n
Nexus, doi être capable de récupérer le nouveau code avant de ziper)

https://plugins.jenkins.io/generic-webhook-trigger/

