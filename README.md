# TP Python

## Serveur Nexus
l'adresse IP : 192.168.0.12

### Instalation et configuration du serveur nexus

1. Se placer dans le dossier serveur-nexus
2. Effectuer vagrant up pour démarrer la machine
3. Effectuer vagrant ssh pour se connecter à la machine
4. Dans la machine se placer dans le répertoire /home/rsync
5. Dans ce repertoire vous devez trouver le script nexusdeb.sh
6. Executé le script comme suivant "sudo ./nexusdeb.sh"
7. Une fois le mot "Success" affiché dans le terminal, vous pouvez acceder au serveur nexus depuis votre navigateur web (votre machine windows)
   à l'adresse localhost:5012
8. les identifiants :
    - user : admin
    - password: le mot de passe se trouve dans le fichier /opt/nexus/sonatype-work/nexus3/admin.password sur le serveur nexus 


$$$$$$$$$$$ss