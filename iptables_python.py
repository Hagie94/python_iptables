#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk
import subprocess

fenetre = tk.Tk()
fenetre.title('Iptables')
fenetre.geometry('900x600')


def appliquer_regle():
    chaine = listeCombo.get()
    protocole = protocole_entre.get()
    int_entree = interface1.get()
    int_sortie = interface2.get()
    port_entre = port1.get()
    port_sorti = port2.get()
    cible = listeCombo2.get()

    try:
        subprocess.run(
            ["/bin/bash", "./appliquer_regle.sh", chaine, protocole, int_entree, int_sortie, port_entre, port_sorti,
             cible], check=True)
        resultat = tk.Label(text="Avec succès")
    except subprocess.CalledProcessError as e:
        resultat = tk.Label(text="erreur")

def default_policy(): #application de la politique par defaut
    pol_int = listeCombo3.get()
    pol_out = listeCombo4.get()
    pol_forward = listeCombo5.get()
    try:
        subprocess.run(["/bin/bash", "./regle_politique.sh", pol_int, pol_out, pol_forward], check=True)
    finally:
        print("something went wrong or may be")



# chaine
chaine = tk.Label(fenetre, text="Chaîne:")
chaine.place(x=70, y=150)
listeChaine = ["INPUT", "OUTPUT", "FORWARD"]
listeCombo = ttk.Combobox(fenetre, values=listeChaine)
listeCombo.current(0)
listeCombo.place(x=150, y=150)

# protocole
protocole = tk.Label(fenetre, text="Protocole:")
protocole.place(x=70, y=200)
protocole_entre = tk.Entry()
protocole_entre.place(x=150, y=200)

# interface
interface_entre = tk.Label(fenetre, text="Ip Source:")
interface_entre.place(x=70, y=250)
interface1 = tk.Entry()
interface1.place(x=200, y=250)
interface_sortie = tk.Label(fenetre, text="Ip Destination:")
interface_sortie.place(x=430, y=250)
interface2 = tk.Entry()
interface2.place(x=550, y=250)
# port
port_entre = tk.Label(fenetre, text="Port Source:")
port_entre.place(x=70, y=300)
port1 = tk.Entry()
port1.place(x=150, y=300)
port_sorti = tk.Label(fenetre, text="Port Destination")
port_sorti.place(x=350, y=300)
port2 = tk.Entry()
port2.place(x=480, y=300)

# cible
cible = tk.Label(fenetre, text="Cible:")
cible.place(x=70, y=350)
listeCible = ["ACCEPT", "REJECT", "DROP"]
listeCombo2 = ttk.Combobox(fenetre, values=listeCible)
listeCombo2.current(0)
listeCombo2.place(x=150, y=350)

# sauvegarde
bouton3 = tk.Button(fenetre, text=" Sauvegarde", command=appliquer_regle)
bouton3.place(x=200, y=380)

# fenetre politique par defaut
label = tk.Label(fenetre, text='INPUT:')
label1 = tk.Label(fenetre, text='OUTPUT:')
label2 = tk.Label(fenetre, text='FORWARD:')
listeInput = ["ACCEPT", "REJECT", "DROP"]
listeCombo3 = ttk.Combobox(fenetre, values=listeInput)
listeCombo3.current(0)
listeoutput = ["ACCEPT", "REJECT", "DROP"]
listeCombo4 = ttk.Combobox(fenetre, values=listeoutput)
listeCombo4.current(0)
listeForward = ["ACCEPT", "REJECT", "DROP"]
listeCombo5 = ttk.Combobox(fenetre, values=listeForward)
listeCombo5.current(0)
bouton4 = tk.Button(fenetre, text=" Sauvegarde", command=default_policy)


def politique_par_defaut():
    label.place(x=70, y=150)
    label1.place(x=70, y=200)
    label2.place(x=70, y=250)
    listeCombo3.place(x=150, y=150)
    listeCombo4.place(x=180, y=200)
    listeCombo5.place(x=180, y=250)
    bouton4.place(x=200, y=300)

    chaine.place_forget()
    listeCombo.place_forget()
    protocole.place_forget()
    protocole_entre.place_forget()
    interface_entre.place_forget()
    interface1.place_forget()
    interface_sortie.place_forget()
    interface2.place_forget()
    port_entre.place_forget()
    port1.place_forget()
    port_sorti.place_forget()
    port2.place_forget()
    cible.place_forget()
    listeCombo2.place_forget()
    bouton3.place_forget()


def nouvelle_fenetre():
    label.place_forget()
    label1.place_forget()
    label2.place_forget()
    listeCombo3.place_forget()
    listeCombo4.place_forget()
    listeCombo5.place_forget()
    bouton4.place_forget()
    chaine.place(x=70, y=150)
    listeCombo.place(x=150, y=150)
    protocole.place(x=70, y=200)
    protocole_entre.place(x=150, y=200)
    interface_entre.place(x=70, y=250)
    interface1.place(x=200, y=250)
    interface_sortie.place(x=430, y=250)
    interface2.place(x=550, y=250)
    port_entre.place(x=70, y=300)
    port1.place(x=150, y=300)
    port_sorti.place(x=350, y=300)
    port2.place(x=480, y=300)
    cible.place(x=70, y=350)
    listeCombo2.place(x=150, y=350)
    bouton3.place(x=200, y=380)


# politique par defaut
b1 = tk.Button(fenetre, text='Nouvelle règle', command=nouvelle_fenetre)
b1.place(x=20, y=50)

b2 = tk.Button(fenetre, text='Politique par défaut', command=politique_par_defaut)
b2.place(x=200, y=50)

fenetre.mainloop()
