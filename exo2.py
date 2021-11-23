# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 10:26:19 2021

@author: mathi
"""

def mesImpots(tranche,revenu,totimpot=0):
        if revenu > 158123:
            revenu = revenu - 158123
            totimpot = totimpot + (revenu * (45/100)) + (158122-73516) * 41/100+ (73516-25710) * 30/100+ (25710-10084) * 11/100
        else:
            while i<len(tranche)
                revenu > tranche[i][0]:
                    revenu = revenu - tranche[i][0]-1
                    totimpot = totimpot + revenu - tranche[i+1][0]
                    totimpot = totimpot + (revenu-73516) * 41/100+ (73516-25710) * 30/100+ (25710-10084) * 11/100
                    print(totimpot)
                    i = i+1

tranche = [[158122,45],[73516,41],[25710,30],[10084,11]]
mesImpots(tranche, 50000)