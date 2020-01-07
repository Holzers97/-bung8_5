# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 12:49:11 2020

@author: stefa
"""
import numpy as np
from tephigram_python import Tephigram


def ein_lesen():
    """einlesen der Daten"""
    #doc = np.loadtxt('University of Wyoming - Radiosonde Data.dat', unpack=True)
    doc = np.loadtxt('Zadar1.dat', unpack=True)
    P = doc[0]
    T = doc[2]
    RH = doc[4]
    T_dp = doc[3]
    z = doc[1]
    return P, T,T_dp, RH, z


def data():
    """funktion zum plotten der Daten von ein_lesen()"""
    P, T, RH, T_dp, z = ein_lesen()
    tephigram.plot_sounding(P = P , T = T ,T_dp=T_dp)
    tephigram.plot_legend()
    tephigram.plot_test_parcel(z=z, P = P, T = T, T_dp=T_dp, RH = RH/100)

def picture(name):
    """abspeichern des Tephigramms mit Parameter:filename"""
    tephigram.savefig(name)

tephigram = Tephigram(x_range=(-50,80))
data()
picture()