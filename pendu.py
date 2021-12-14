# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 08:02:04 2021

@author: mathi
"""

import random as random
import unicodedata
import numpy as np
import sys
import tkinter as tk

def mot_random():
    lmot = open('liste_mot_pendu.txt','r',encoding=('utf8'))
    mot = lmot.readlines()
    i = random.randint(0,len(mot))
    return mot[i]


def nettoyage(mot):
    mot_sa = unicodedata.normalize('NFKD', mot)
    b = u"".join([c for c in mot_sa if not unicodedata.combining(c)])
    MOT_SA = b.upper()
    liste_lettre = list(MOT_SA)
    liste_lettre = liste_lettre[:-1]
    return liste_lettre

def saisie(liste_lettre):
    l_input = []
    essaie = input('entrer une lettre : ')
    # if essaie != str():
    #     print("t con")
    #     essaie = input('entrer une lettre : ')
    essaie = essaie.upper()
    l_input.append(essaie)
    return l_input
            
        
def jeu(liste_lettre):
    vie = 0
    taille = 0
    inp = []
    liste_inp = []
    liste_jeu = liste_lettre[0] + " " +"_ " * (len(liste_lettre)-1)
    liste_jeu = liste_jeu.split()
    liste_lettre = liste_lettre[1:]
    print(liste_jeu)
    while vie < 8:
        print('il vous reste ', 8-vie,' vie')
        print('vous avez deja utilisé ces lettres : ' , liste_inp)
        if taille != len(liste_lettre):
            inp = saisie(liste_lettre)
            liste_inp.append(inp[0])
            print(inp)
            if inp[0] in liste_lettre:
                print(taille)
                i = np.where(np.array(liste_lettre) == inp[0])[0]
                for u  in i:
                    liste_jeu[u+1] = inp[0]
                    taille += 1
            else:
                print('mauvaise lettre ! ')
                vie += 1
            print(liste_jeu)
        elif taille == len(liste_lettre):    
            print('victoire')
            sys.exit()
    print('t mort')

def affichage():
    root = tk.Tk()
    boutton_jouer = tk.Button(root,text = "test",command = root.destroy())
    boutton_jouer.pack()
    
    
    root.mainloop()

# listelettrev = nettoyage(mot_random())
# jeu(listelettrev)
affichage()
