# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 10:50:57 2019

@author: GaonkarN
"""


def main():
    print("this prog. is to compute a combination a+aa+aaa+...+a^n where a==n ")
    a = int(input("Enter The Vale OF a :"))
    total = 0
    prod = 1
    for intial in range(1, a+1, 1):
        prod = prod * a
        total = total + prod
    print(" the final value of combination a+aa+aaa+...+a^n where a=",a,"is",total)
main()
