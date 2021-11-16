# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 08:19:48 2021

@author: mathi
"""

def bissextile(dic,j_f,x):
    if len(str(x)) != 4 or x < 1582:
        print(x)
        print ('erreur, entrer une année valide')
        annee_cor=int(input('enter une année correcte'))
        bissextile(dic_annee, jour_fev, annee_cor)
    else:
        if x%100 == 0 and x%4 == 0:
            dic[2] =  29
            return dic
        elif x%400 == 0:
            dic[2] =  29
            return dic
        else:
            return dic
        
def nombre_jour_mois(dic,y):
    if 1<=y<=12:
        return y
    else:
        print("ce mois n'existe pas")
        
def verif_date(dic,y,z):
    if 1 <= y <= dic[z]:
        print('date valide ! ')
    else:
        print("date invalide ! ")


jour_fev = 28
dic_annee = {1:31,2:jour_fev,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

jours = int(input('entrer un jour : '))
mois = int(input('entrer un mois : '))
annee = int(input('entrer une année : '))

verif_date(bissextile(dic_annee, jour_fev, annee),jours,nombre_jour_mois(bissextile(dic_annee, jour_fev, annee),mois))   
