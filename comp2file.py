# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 10:14:57 2019

@author: GaonkarN
"""
import filecmp


def main():
    print("This program is to compare two files if files are same it will print True else False")
    filename1 = str(input("Enter File name : "))
    filename2 = str(input("Enter File Name of file u want to compare : "))
    result = filecmp.cmp(filename1,filename2)
    if bool(result)== True:
        print("Both Files are same")
    else:
        print("Both files are Different")

main()
