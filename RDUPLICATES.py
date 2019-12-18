# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 17:08:33 2019

@author: GaonkarN
"""


def removeDuplicates(duplicate):
    remdup = []
    str1 = " "
    for num in duplicate:
        if num not in remdup:
            remdup.append(num)
        elif num in remdup:
            remdup.remove(num)
            return str1.join(remdup)


def main():
    print("This program is to remove Duplicates from string")
    dstring = input("Enter the sentence to remove duplicates :")
    duplicate = dstring.split()
    dstring = removeDuplicates(duplicate)
    print("The Sorted String is >> " + dstring)
main()

    

