#####CLASSE MACHINE#####
class Machine:

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
