from ivy.ivy import *
from ivy.std_api import *
from GUI import GUI
from queue import Queue

class LigneDeCommande():

    def send(self, message):
        IvySendMsg(message)

    def __init__(self, master):

        self.master = master
        self.queue = Queue()
        self.gui = GUI(self.master, self.queue, self.endApplication)

        self.thread1 = threading.Thread(target=self.workerThread1)
        self.thread1.start()

    def workerThread1(self):
        IvyInit("LigneDeCommandeAgent","Ligne De Commande est pret",0, self.on_connetion_change, self.on_die)
        IvyStart()
        self.periodicCall()

    def endApplication(self):
        IvyStop()
        sys.exit(0)

    def periodicCall(self):
        """
        Handle all the messages currently in the queue (if any).
        """
        if not self.queue.empty():
            msg = self.queue.get()
            self.send(msg)

        self.master.after(100, self.periodicCall)

    def on_connetion_change(agent, event, *args):
        if event == IvyApplicationDisconnected:
            # info("Ivy application %r has disconnected", agent)
            print("Ivy application %r has disconnected", agent)
        else:
            # info("Ivy application %r has connected", agent)
            # info("Ivy application currently on the bus: %s", ",".join(IvyGetApplicationList()))
            print("Ivy application %r has connected", agent)
            print("Ivy application currently on the bus: %s", ",".join(IvyGetApplicationList()))

    def on_die(agent, id):
        #info("Received the order to die from %r with id = %d", agent, id)
        print("Received the order to die from %r with id = %d", agent, id)
        IvyStop()