# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 10:26:19 2021

@author: mathi
"""

def mesImpots(tranche,revenu,totimpot=0):
    if len(tranche) !=0:
        if revenu > 158123:
            revenu = revenu - 158123
            totimpot = totimpot + (revenu * (45/100))
            return mesImpots(tranche,revenu,totimpot)
        elif revenu > tranche[0][0]:
            print(revenu)
            revenu = revenu - tranche[0][0]-1
            totimpot = totimpot + (revenu * (tranche[0][1]/100))
            print(totimpot)
            del tranche[0]
            return mesImpots(tranche,revenu,totimpot)
        else:
            del tranche[0]
            return mesImpots(tranche,revenu,totimpot)
    else:
        print(totimpot)
        

tranche = [[158122,45],[73516,41],[25710,30],[10084,11]]
mesImpots(tranche, 50000)