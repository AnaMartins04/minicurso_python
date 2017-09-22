#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 11:28:29 2017

@author: labsim
"""

import numpy as np
import matplotlib.pyplot as plt

#CONDIÇOES INICIAIS
i1, i2 = 0.8, 0.3
theta = np.linspace(-3, 3, 1000)

#INDUTANCIAS
L11 = (3 + np.cos(2*theta))*10e-3
L22 = 0.3*np.cos(theta)
L12 = (30 + 10*np.cos(2*theta))

#COENERGIA
W = 0.5*L11*i1**2 + L12*i1*i2 + 0.5*L22*i2**2
W_relutancia = 0.5*L11*i1**2 + 0.5*L22*i2**2
W_mutuo = L12*i1*i2 

#TORQUE
T_total = np.diff(W)
T_relutancia = np.diff(W_relutancia)
T_mutuo = np.diff(W_mutuo)

#PLOT 
plt.figure(1, [10, 7])
plt.subplot(311)
plt.title("TORQUE TOTAL")
plt.xlabel("$\Theta$(radianos)")
plt.plot(theta[0:len(theta)-1], T_total)

plt.subplot(312)
plt.title("TORQUE MUTUO")
plt.plot(theta[0:len(theta)-1], T_mutuo, 'm')
plt.xlabel("$\Theta$(radianos)")

plt.subplot(313)
plt.title("TORQUE RELUTANCIA")
plt.plot(theta[0:len(theta)-1], T_relutancia, 'r')
plt.xlabel("$\Theta$(radianos)")

plt.tight_layout()
plt.show()
