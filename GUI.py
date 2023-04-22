import tkinter as tk
from tkinter import *
from queue import Queue
import math
from ivy.ivy import *
from ivy.std_api import *

from RegexCommand import RegexCommand


class GUI():
    def __init__(self, master, queue, endCommand):

        # Import regex commands
        self.regexCommand = RegexCommand()


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
        if re.match(self.regexCommand.avancerRegex, message):
            return True
        elif re.match(self.regexCommand.reculerRegex, message):
            return True
        elif re.match(self.regexCommand.tourneDroiteRegex, message):
            return True
        elif re.match(self.regexCommand.tourneGaucheRegex, message):
            return True
        elif re.match(self.regexCommand.leveCrayonRegex, message):
            return True
        elif re.match(self.regexCommand.baisseCrayonRegex, message):
            return True
        elif re.match(self.regexCommand.origineRegex, message):
            return True
        elif re.match(self.regexCommand.restaureRegex, message):
            return True
        elif re.match(self.regexCommand.nettoieRegex, message):
            return True
        elif re.match(self.regexCommand.fccRegex, message):
            return True
        elif re.match(self.regexCommand.fcapRegex, message):
            return True
        elif re.match(self.regexCommand.fposRegex, message):
            return True
        else:
            return False










