# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 15:33:46 2019

@author: GaonkarN
"""
def listToString(words):  
    
    str1 = " " 
    return (str1.join(words))



def main():
    sentence = str(input("Enter The Sentence You need to sort >> "))
    print("String is >> " + sentence)
    words = sentence.split()
    words.sort()
    sentence = listToString(words)
    print("The Sorted String is >> " + sentence)
main()

