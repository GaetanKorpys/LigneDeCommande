from ivy.ivy import *
from ivy.std_api import *
import re

class LigneDeCommande():

    def on_message(agent):
        info("Received from %r: %s", agent)

    def on_connetion_change(agent, event, *args):
        if event == IvyApplicationDisconnected:
            #info("Ivy application %r has disconnected", agent)
            print("Ivy application %r has disconnected", agent)
        else:
            #info("Ivy application %r has connected", agent)
            #info("Ivy application currently on the bus: %s", ",".join(IvyGetApplicationList()))
            print("Ivy application %r has connected", agent)
            print("Ivy application currently on the bus: %s", ",".join(IvyGetApplicationList()))

    def on_die(agent, id):
        #info("Received the order to die from %r with id = %d", agent, id)
        print("Received the order to die from %r with id = %d", agent, id)
        IvyStop()

    def send(self, message):
        IvySendMsg(message)

    def checkRegex(self, message):
        if re.match("^AVANCE [1-9][0-9]?$|^AVANCE 100$", message):
            return True
        elif re.match("^RECULE [1-9][0-9]?$|^RECULE 100$", message):
            return True
        elif re.match("^TOURNEDROITE (?:36[0]|3[0-5][0-9]|[12][0-9][0-9]|[1-9]?[0-9])?$", message):
            return True
        elif re.match("^TOURNEGAUCHE (?:36[0]|3[0-5][0-9]|[12][0-9][0-9]|[1-9]?[0-9])?$", message):
            return True
        elif re.match("^LEVECRAYON$", message):
            return True
        elif re.match("^BAISSECRAYON$", message):
            return True
        elif re.match("^ORIGINE$", message):
            return True
        elif re.match("^RESTAURE", message):
            return True
        elif re.match("^NETTOIE$", message):
            return True
        elif re.match("^FCC (?:1?[0-9]{1,2}|2[0-4][0-9]|25[0-5]) (?:1?[0-9]{1,2}|2[0-4][0-9]|25[0-5]) (?:1?[0-9]{1,2}|2[0-4][0-9]|25[0-5])$", message):
            return True
        elif re.match("^FCAP (?:36[0]|3[0-5][0-9]|[12][0-9][0-9]|[1-9]?[0-9])?$", message):
            return True
        elif re.match("^FPOS [1-9][0-9]?$|^FPOS 100$", message):
            return True
        else:
            return False

    def __init__(self, agent_name):

        IvyInit(agent_name, "Ligne De Commande est pret", 0, self.on_connetion_change, self.on_die)
        IvyStart("127.0.0.1:2010")
        time.sleep(0.5)

        while(1):
            self.input = input("Entrer une commande : ")
            if self.checkRegex(self.input):
                self.send(self.input)
            else:
                print("Erreur : commande incorrecte")


