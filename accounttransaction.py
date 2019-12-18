# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 11:35:37 2019

@author: GaonkarN
"""


class Bank_Account():

    def __init__(self, name):
        self.balance = 0
        self.name = name
        print("Hello Ur account in XYZ Bank is opened under the name of :" + name)

    def deposit(self, amt_d):
        print(" Amount Deposited:", amt_d)
        self.balance += amt_d

    def withdraw(self, amt_wd):
        if self.balance >= amt_wd:
            self.balance -= amt_wd
            print("\n You Withdrew:", amt_wd)
        else:
            print("\n Insufficient balance  ")

    def display(self):
        print("\n Net Available Balance=", self.balance)
