# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 08:19:48 2021

@author: mathi
"""

def bissextile ():
    jour_fev = 28
    annee = {'janvier':31,'février':jour_fev,'mars':31,'avril':30,'mai':31,'juin':30,'juillet':31,'aout':31,'sptembre':30,'octobre':31,'novembre':30,'décembre':31}

    x = int(input('Année ? : '))
    if len(str(x)) != 4 or x < 1582:
        print ('erreur, entrer une année valide')
        bissextile()
    else:
        if str(x)[2] != 0 and str(x)[3] != 0 and x%4 == 0:
            annee['février'] =  29
            print('True')
            return True
        elif x%400 == 0:
            annee['février'] =  29
            print('True')
            return True
        else:
            print('False')
            return False

bissextile()