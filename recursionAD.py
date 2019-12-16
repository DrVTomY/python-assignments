# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 15:11:44 2019

@author: GaonkarN
"""
def sumdigits(number):
  if number == 0:
    return 0
  else:
    return (number%10) + sumdigits(number//10)

def main():
    number=int(input("Enter a number :"))
    print(sumdigits(number))

main()
