# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 23:50:29 2021

@author: user
"""

def factorial(n):
    if n == 1:
        r = 1
        return r

    f = factorial(n-1)
    r = n * f
    return r

if __name__ == '__main__':
    factorial(5)