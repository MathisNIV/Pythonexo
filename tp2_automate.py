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

phrase = "la souris verte dort ."
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
    phrase = phrase.split()
    phrase_indice = []
    etat_p = 0
    for i in phrase:
        phrase_indice.append(dictionnaire[i])
        print(phrase_indice)
    for k in phrase_indice:
        print(etat_p)
        etat_p = etat[etat_p][k]
    print("etat p : " ,etat_p)
    if etat_p == 9:
        print("phrase correcte")
    else:
        print("phrase fausse")
syntaxe(phrase, dictionnaire,etat)