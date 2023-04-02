import tkinter as tk
from tkinter import *
from queue import Queue
import math
from ivy.ivy import *
from ivy.std_api import *


class GUI():
    def __init__(self, master, queue, endCommand):

        self.queue = queue
        self.master = master

        self.sv = StringVar()

        self.entry = tk.Entry(self.master, textvariable =self.sv)
        self.entry.bind('<Return>', self.readFromKeyboard)
        self.entry.pack()

        self.label = tk.Label(self.master)
        self.label.pack()

        close = tk.Button(self.master, text='Close', command=endCommand)
        close.pack()


    def readFromKeyboard(self, event):
        cmd = self.sv.get().strip()
        if self.checkRegex(cmd) :
            self.addToQueue(cmd)
            self.label.config(text="")
            self.sv.set("")
        else:
            self.label.config(text="Commande incorrecte")


    def addToQueue(self, message):
        self.queue.put(message)

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
        elif re.match("^FPOS*", message):
            return True
        else:
            return False










