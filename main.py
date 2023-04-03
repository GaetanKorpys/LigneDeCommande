from LigneDeCommande import LigneDeCommande
import tkinter as tk
from ivy.ivy import *

if __name__ == '__main__':

    root = tk.Tk()
    root.title("Ligne De Commande")
    root.geometry("350x80")
    ligneDeCommande = LigneDeCommande(root)
    root.mainloop()


