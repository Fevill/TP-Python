#####CLASSE MACHINE#####
class Machine :

    #Les variables
    hostname=""
    ip=""
    nombreDeCpu=""
    tailleDeLaRam=""
    nombreEtTaille= dict()
    osEtversion=""

    def afficher(self):
        print("Hostname {self.hostname}")