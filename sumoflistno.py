# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 14:58:57 2019

@author: GaonkarN
"""

listofNos = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    listofNos.append(numbers)
print("Sum of elements in given list is :", sum(listofNos))