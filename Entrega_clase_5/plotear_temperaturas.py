# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 10:53:10 2021

@author: user
"""
import numpy as np
import matplotlib.pyplot as plt 
def plotear_temperaturas():
    temperaturas = np.load('../Data/temperaturas.npy')
    plt.hist(temperaturas, bins = 25)
    plt.show()


if __name__ == '__main__':
    plotear = plotear_temperaturas()