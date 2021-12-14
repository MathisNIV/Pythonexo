# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 08:14:23 2021

@author: mathi
"""


"""
article = 0
adjectif = 1
nom = 2
verbe = 3
nomP = 4
point = 5
"""


dictionnaire ={"le" : 0, "la" : 0, "chat" : 2, "souris" : 2, "martin" : 4,
"mange" : 3, "la" : 0, "petite" : 1, "joli" : 1, "grosse" : 1, 
"bleu" : 1, "verte" : 1, "dort" : 3,"julie" : 4, "jean" : 4, "." : 5}

phrasedur = "la souris verte dort ."

#tableau des transitions

etat = [
        [1,8,8,8,4,8],#attente 0/4
        [8,1,2,8,8,8],#attente 1/2
        [8,2,8,3,8,8],#attente 3/1
        [5,8,8,8,7,9],#attente 5/0/4
        [8,8,8,3,8,8],#attente 3
        [8,5,6,8,8,8],#attente 2/1
        [8,6,8,8,8,9],#attente 1/5
        [8,8,8,8,8,9],#attente 5
        [8,8,8,8,8,8],#phrase fausse
        [8,8,8,8,8,8] #phrase juste
        ]

def syntaxe(phrase,dictionnaire,etat):
    phrase_indice = []
    etat_p = 0
    
    #convertie la phrase avec les valeur du dictionnaire
    
    for i in phrase: 
        phrase_indice.append(dictionnaire[i])
        
    #recuperer la valeurde l'etat precedent
        
    for k in phrase_indice:
        etat_p = etat[etat_p][k]
    if etat_p == 9:
        print("phrase correcte")
    else:
        print("phrase fausse")
        


def saisie():
    x  = input("rentrer une phrase : ")
    if x[-1] == "." and x[-2] != " ":
        x = x[:-1]
        x = x.split()
        x.append(".")
        return x
    else:
        x = x.split()
        return x

#fonction qui permet de lire un dictionnaire francais complet (j'ai juste utilisé la lettre A car l'alphabet complet etait trop volumineux)

def lecturedico():
    dicofrancais = {}
    for ligne in open("dicoFrancais.txt"):
        ligne = ligne.split()
        ligne.pop(1)
        ligne[1]=ligne[1].split(":")
        if ligne[1][0] == "Ver":
            dicofrancais[ligne[0]]=3
        if ligne[1][0] == "Adj":
            dicofrancais[ligne[0]]=1
        if ligne[1][0] == "Nom":
            dicofrancais[ligne[0]]=2
        if ligne[1][0] == "Det":
            dicofrancais[ligne[0]]=0
        if ligne[1][0] == "NomP":
            dicofrancais[ligne[0]]=4
        
    return dicofrancais
#lecturedico()   


syntaxe(saisie(), dictionnaire,etat)